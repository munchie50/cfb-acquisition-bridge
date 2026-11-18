# Verified local Git bundle checkout candidate

Proposed rule: The producer may obtain a new Git worktree from normal HTTPS Git or from a verified local Git bundle. Before using a bundle, independently authenticate fresh GitHub main and the expected digest from trusted transport metadata. Require the bundle's main ref and resulting detached HEAD to equal the pinned commit, a non-shallow worktree with genuine ancestry, required current-task files, and existing retained immutable-review validation. Missing, corrupt, or stale transport fails closed. Preserve canonical ownership and live acceptance gates.

Status: candidate, exercised in Work Mode. Existing production helper and automation instructions remain in use. The candidate adds an optional local-bundle source to the helper. Production integration would need coordinated helper blob verification and an updated embedded payload or equivalent verified transport, plus the procedure/recovery authority update.

Local proof: connector-pinned main 1172e07f4cf48deda474ea27149394171cda3a4c; exact existing helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898. Candidate accepted the 14,541,382-byte bundle and returned SUPPORTED_GIT_RUNTIME_VERIFIED, with the exact pin and 64 retained review references. Git connectivity passed. The candidate rejected a wrong SHA-256 and a genuine older full bundle before creating a checkout.

Next scheduled evidence: read the November 18 16:30 CT Engine Health bundle test receipt. On pass, plan a current-main delivery test using authenticated bundle metadata and a verified full bundle, or a tested persistent seed plus a matching delta. Measure the actual delivery byte limit and prove the exact current pin in the scheduled worker before promoting the rule. A historical fixture pass alone does not prove production-sized delivery or unattended refresh.

## Candidate patch

```diff
--- a/scripts/cfb_runtime_checkout.py
+++ b/scripts/cfb_runtime_checkout.py
@@ -1,5 +1,6 @@
 """Prepare a real, pinned CFB Git worktree before research; never publish or write back."""
 import argparse
+import hashlib
 import json
 import os
 import re
@@ -12,7 +13,7 @@
             'cfb_neutral_publication_gate.py', 'cfb_recovery_consumer_preflight.py')
 
 
-def prepare(destination, expected_head):
+def prepare(destination, expected_head, *, bundle=None, bundle_sha256=None):
     if not re.fullmatch(r'[0-9a-f]{40}', expected_head):
         raise ValueError('exact connector-observed main commit required')
     destination = Path(destination).resolve()
@@ -22,9 +23,22 @@
     def git(*args):
         return subprocess.check_output(['git', *args], env=env, stderr=subprocess.PIPE,
                                        timeout=180).decode('utf-8').strip()
-    # A normal full clone preserves genuine commit/tree/blob ancestry. No graft,
-    # replacement object, forged commit, synthetic ref or validator patch is used.
-    git('clone', '--no-checkout', REPOSITORY, str(destination))
+    repository = REPOSITORY
+    if (bundle is None) != (bundle_sha256 is None):
+        raise ValueError('bundle and expected SHA-256 must be supplied together')
+    if bundle is not None:
+        bundle = Path(bundle).resolve(strict=True)
+        if not bundle.is_file():
+            raise ValueError('bundle must be a local regular file')
+        with bundle.open('rb') as stream:
+            actual_sha256 = hashlib.file_digest(stream, 'sha256').hexdigest()
+        if actual_sha256 != bundle_sha256:
+            raise ValueError('bundle SHA-256 differs from accepted transport metadata')
+        if git('bundle', 'list-heads', str(bundle), 'refs/heads/main') != expected_head + ' refs/heads/main':
+            raise ValueError('bundle main must match connector-observed main exactly')
+        repository = str(bundle)
+    # Both source paths must produce genuine, complete Git ancestry.
+    git('clone', '--no-checkout', repository, str(destination))
     git('-C', str(destination), 'cat-file', '-e', expected_head + '^{commit}')
     git('-C', str(destination), 'merge-base', '--is-ancestor', expected_head, 'origin/main')
     git('-C', str(destination), 'checkout', '--detach', expected_head)
@@ -55,6 +69,7 @@
         verified.append(dict(ref, committed_at=committed))
     return {'status': 'SUPPORTED_GIT_RUNTIME_VERIFIED', 'repository': REPOSITORY,
             'head': expected_head, 'worktree': str(destination),
+            'checkout_source': 'local_git_bundle' if bundle else 'github_https',
             'python': sys.version.split()[0], 'immutable_reviews': verified,
             'scope': 'runtime and ancestry only; no research, publication or run acceptance'}
 
@@ -63,9 +78,12 @@
     p = argparse.ArgumentParser(description=__doc__)
     p.add_argument('--destination', type=Path, required=True)
     p.add_argument('--expected-head', required=True)
+    p.add_argument('--bundle', type=Path)
+    p.add_argument('--bundle-sha256')
     a = p.parse_args()
     try:
-        print(json.dumps(prepare(a.destination, a.expected_head), indent=2))
+        print(json.dumps(prepare(a.destination, a.expected_head, bundle=a.bundle,
+                                 bundle_sha256=a.bundle_sha256), indent=2))
     except (ValueError, OSError, subprocess.SubprocessError) as exc:
         print(json.dumps({'status': 'COMPUTATION_RUNTIME_UNAVAILABLE',
                           'error_type': type(exc).__name__,
```
