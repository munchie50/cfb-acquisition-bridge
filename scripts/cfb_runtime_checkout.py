"""Prepare a real, pinned CFB Git worktree before research; never publish or write back."""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPOSITORY = 'https://github.com/munchie50/cfb-acquisition-bridge.git'
REQUIRED = ('cfb_week9_publication.py', 'cfb_hot_sheet_readiness.py',
            'cfb_neutral_publication_gate.py', 'cfb_recovery_consumer_preflight.py')


def prepare(destination, expected_head):
    if not re.fullmatch(r'[0-9a-f]{40}', expected_head):
        raise ValueError('exact connector-observed main commit required')
    destination = Path(destination).resolve()
    if destination.exists():
        raise ValueError('destination must be new; never reset an existing worktree')
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    def git(*args):
        return subprocess.check_output(['git', *args], env=env, stderr=subprocess.PIPE,
                                       timeout=180).decode('utf-8').strip()
    # A normal full clone preserves genuine commit/tree/blob ancestry. No graft,
    # replacement object, forged commit, synthetic ref or validator patch is used.
    git('clone', '--no-checkout', REPOSITORY, str(destination))
    git('-C', str(destination), 'cat-file', '-e', expected_head + '^{commit}')
    git('-C', str(destination), 'merge-base', '--is-ancestor', expected_head, 'origin/main')
    git('-C', str(destination), 'checkout', '--detach', expected_head)
    if git('-C', str(destination), 'rev-parse', 'HEAD') != expected_head:
        raise ValueError('checkout HEAD differs from connector authority')
    if git('-C', str(destination), 'rev-parse', '--is-shallow-repository') != 'false':
        raise ValueError('full accepted ancestry required')
    for name in REQUIRED:
        if not (destination / 'scripts' / name).is_file():
            raise ValueError('missing governed compiler: ' + name)
    sys.path.insert(0, str(destination / 'scripts'))
    from cfb_conditional_recommendation_profile import load_review
    # Verify every immutable ref in retained canonical history, including closed
    # reviews; those objects remain necessary to validate later typed packets.
    refs = {}
    ledger = destination / 'evidence/operational/CFB_DECISION_WAIT_LEDGER.md'
    for body in re.findall(r'^```cfb-[^\n]+\n(.*?)^```\s*$', ledger.read_text(), re.M | re.S):
        packet = json.loads(body)
        for row in packet.get('rows', []):
            ref = row.get('review_ref')
            if ref:
                refs[(ref['commit'], ref['path'], ref['blob'])] = ref
    if not refs:
        raise ValueError('no governed immutable review refs recovered')
    verified = []
    for ref in refs.values():
        _, committed = load_review(ref)
        verified.append(dict(ref, committed_at=committed))
    return {'status': 'SUPPORTED_GIT_RUNTIME_VERIFIED', 'repository': REPOSITORY,
            'head': expected_head, 'worktree': str(destination),
            'python': sys.version.split()[0], 'immutable_reviews': verified,
            'scope': 'runtime and ancestry only; no research, publication or run acceptance'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destination', type=Path, required=True)
    p.add_argument('--expected-head', required=True)
    a = p.parse_args()
    try:
        print(json.dumps(prepare(a.destination, a.expected_head), indent=2))
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({'status': 'COMPUTATION_RUNTIME_UNAVAILABLE',
                          'error_type': type(exc).__name__,
                          'scope': 'no publication attempted; preserve task schedules'}))
        sys.exit(1)
