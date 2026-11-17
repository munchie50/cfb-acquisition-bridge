# Monitor startup order troubleshooting

Revision: CFB_EMBEDDED_STARTUP_ORDER_20261117_R2

## Observed evidence

Production invocation e6cae0de-771c-8321-aaf6-7914ba46fbda closed RUN_INCOMPLETE. Its terminal candidate at dbc140eaed6f2e75c7dff38417cfa86bd1308e76 records authenticated helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898 and embedded helper execution NOT_EXECUTED, followed by REST DNS failure. The startup trace contains no delivered prompt revision or command rejection. Existing API tools expose run metadata and result, but no delivered prompt snapshot or internal command transcript.

The freshly fetched production and successful canary task prompts contain identical literal embedded payloads. Current task settings alone do not prove the exact prompt delivered to the failed invocation. Both task environments report inherited settings without selected worker identities. The passing canary used Python 3.12.14 / Git 2.52.0; failed production reported Python 3.13.5 / Git 2.47.3. A provisioning difference is possible but its cause is unverified.

## Correction installed and independently read back

Production prompt previously requested current authority/index recovery before runtime startup and again after startup. Startup now explicitly orders receipt/readback, authenticated main pin, helper blob metadata, version probe, embedded command, then complete authority recovery before live producer work. Added revision marker and payload-presence/length evidence and actual-command-error requirement for diagnosing future skipped execution.

Exact previous prompt: evidence/scheduler_qa/CFB_MONITOR_STARTUP_ORDER_20261117T190207Z_BEFORE.md at c7e342d69917af374879af4f0ce5822545e7bb10, independently read back in full. Complete updated task prompt independently matched the installed value. Embedded payload bytes and all text from the existing Trace embedded paragraph onward were preserved exactly, and the authority audit paragraph was retained. Schedule and enabled state verified equal after update.

## Limits and next proof

Installed instruction correction verified. Startup-order ambiguity is an identified defect and a candidate contributor, not a proven sole cause of the failed production invocation. Prior scheduled canary remains valid startup evidence. No duplicate manual checkout was run. New revision has not executed in a scheduled invocation. Next production receipt must show revision marker and actual embedded command result, followed by current authority recovery and due live producer work. Production completion remains unproved.
