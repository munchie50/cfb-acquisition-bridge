# Current Hot Sheet source-binding automation — October9

Manual Test Routine run CFB_CURRENT_PUBLICATION_CI_QA_20261010T022024Z; measured start 2026-10-10T02:20:24Z. Existing current binding helper was built/localtested but not independently enforced in repository QA. The old workflow's dated historical projection could succeed while latest decision state changed.

## Implemented correction
scripts/cfb_hot_sheet_current_decision_binding_gate.py now supports --index plus freshly supplied --current-ledger. It consumes the existing qualified navigation reader, requires one literal CURRENT_HOT_SHEET: purpose in the last reconciled checkpoint, verifies selected sheet bytes against its blob, verifies canonical decision pointer against current ledger bytes, and compares the sheet's declared decision identity. No filename/date ordering or historical replay is used as current-state proof. Missing/ambiguous/stale/future/trailing checkpoint and unsupported publication path fail closed. Repository file loading prevents resolved path escape. Selection metadata remains navigation, not authority.

Active accepted index v1.245 has a new final explicit current-role checkpoint; older bytes/pointers preserved. Existing workflow now triggers on decision-ledger/recovery/helper/test changes and runs14regressions plus actualcurrentpublicationcheck. Historical2012projection step renamed to identify its retained scope; preserved priorsection/frozen/total/fullscope/navigation checks. No duplicateworkflow or dispatch. The workflow's recoveryauthority is explicitly qualified acceptedv1.245; a future acceptedauthority/schema change needs explicit qualification/update, not highest-version inference.

## Executed and independently verified proof
14localtests PASS: validselector,UTF8hash,staledeclaration,duplicate/missingbinding,emptystate,no/multiplecurrentrole,pointerbytesmismatch,stalecanonicalnavigation,newerhistoricalfilenamedoesnotselect,unsupportedpath,uncheckpointedtail,futureclock.
Authentic fullindex CLIselected2114CTsheet db109dbee1a509c894a2eceef153e9812b96b4a3 and currentdecision414655435785070be2fd7531e859799863e9a082. Index8b532b8981c6e872a3aff633a5fb8e1489251638. Source/tests/contract/index/workflow exactcreationcommit andmainreadbacks verified. Codee6f42fa5d9776d56690e2401e8be44f6b7330234/test7c74c79f3fcfc2b620ea93a5d4024a0dfea39bd2; contract6e020ebf07ef08555d8df366e59d126d3184e260; workflow6d90409ae8e6b3baa04d4030eb6874da8d131d51.

Independent GitHubrun38016732746 completedSUCCESS on exactworkflowcommit7040beacad92696cddb6dbdda7a087dd511ed51a. Exposed jobsteps independently read, including newregressions and authenticcurrentbinding; no rawjoblogclaim. Planned contract/index proposal/deltaSHA256, UTF8bytes/chars and priorpreservation computed beforewrites; exactresultingblobmatches.

## Boundaries and remaining work
Binding alone doesnot inspect renderedverdictsemantics or establish freshfootball/sourcequalification,calibratedEV,actualCaesars,injury/weatherverification or bets. A matching header with an incorrect row still requires the existing semantic checks. This repair closes automaticlatestsourcebinding detection gap, not every currentdecisionpresentation parser. A later decision append can temporarilyfail CI untilcurrentview/checkpoint reconciled; that detection must not be hidden or mistaken for model failure. Prospective producers must reconcile beforeRUNPASS; postwriteCI cannot retroactivelyqualify naturalclosure.

Natural evening20:19run originalclaimedRUNPASS remainsindependently current-outputRUN_INCOMPLETE; manual2114viewrepair separate. Currentcard2conditional App-10/UMass+4.5max-115 plusFresnoWAIT atretained+6.5,requiresactual+7orbettermax-115byrecordedSaturday20:30cutoff; earlierpracticalconstraintsstillapply. No market/decision/frozen/wager/taskmutation/newdispatch or scientific/Champion/Productionv5change. Naturalcorrectedproduceruse pending; actualexecution/finalavailability andolderfailures remainOPEN.

Candidate/holisticintegration, finalreconciledrecoverycheckpoint andseparatemanualterminalclosure remain distinctrequiredreadbacks. Report acceptance is boundedautomationQA, not bettingreadiness.
