# CFB Engine — Adam Screenshot Ingestion Boundary v1.224

Status: **ACTIVE PROCEDURAL INPUT CONTROL — NO MODEL/FEATURE/SCIENTIFIC CONTRACT CHANGE**
Date: 2026-09-26
Parents: v1.133, v1.144, v1.187, v1.198, v1.216, v1.223
Scope: Adam-provided screenshots only

## Finding

Current CFB contracts already protect downstream model, market, chronology, outcome, and frozen-state boundaries, but they do not explicitly define how a mixed-content screenshot supplied by Adam must be decomposed before routing observations into those governed destinations.

This is a narrow ingestion-boundary gap. It does not justify a universal quarantine subsystem for historical data, public research, model datasets, or all external inputs.

## Core invariants

1. **Adam-provided screenshots are evidence containers, not trusted model-input containers.**
2. **Successful extraction does not grant downstream permission.** Every extracted observation remains subject to the destination contract's source authority, chronology, provenance, freshness, and permitted-use rules.
3. A screenshot is classified observation-by-observation. Do not trust or reject the entire image as one semantic unit.
4. Ambiguous observations remain unresolved. Do not infer missing line direction, odds, stake, ticket status, timestamp, recommendation meaning, game identity, or result.
5. Screenshot-derived information never silently mutates frozen Champion model state, FIRST_FROZEN predictions, model coefficients, scaling, feature definitions, or prior recommendations.

## Boundary flow

Adam screenshot -> boundary/quarantine -> parse individual observations -> classify -> attach available provenance/time -> route only contract-authorized observations -> quarantine/ignore unresolved or unauthorized material

"Quarantine" here means semantic isolation during interpretation. It does not require a new storage subsystem.

## Classification and routing

### A. Execution facts

Examples:
- sportsbook;
- wager/game identity;
- side, total, moneyline, or other wager type;
- accepted execution line/price/odds;
- stake;
- ticket/open/completed status;
- displayed or otherwise established execution time.

Routing:
- May enter the appropriate execution/actual-bet ledger only when the existing execution contract considers the observation sufficiently established.
- A candidate bet slip, proposed selection, or screenshot showing no completed wager must not be silently promoted to an actual wager.
- Preserve source as Adam-provided screenshot and preserve the best available observation/execution time.

### B. Market information

Examples:
- displayed sportsbook spread, total, moneyline, price, movement, or market snapshot.

Routing:
- Remains market/execution evidence under v1.144 and later market contracts.
- It may be compared with an already independent/frozen Champion prediction when otherwise qualified.
- It must not feed back into or alter the Champion fair line, win probability, features, scaling, coefficients, or prediction construction.

### C. Independent factual observations

Examples:
- displayed kickoff information, team/game identity, player status, weather, or other factual claims.

Routing:
- Extraction alone does not make the claim authoritative.
- Apply existing CFB source-authority, freshness, timestamp, and verification requirements before operational use.
- A screenshot does not silently supersede a more authoritative qualified source.

### D. Third-party predictive/evaluative information

Examples:
- sportsbook/AI/media picks;
- third-party win probabilities;
- ratings or power rankings;
- trends;
- public-betting percentages;
- consensus opinions;
- implied recommendations or other evaluative material.

Routing:
- Quarantine from the independent Champion model path.
- Do not use as features, priors, targets, calibration inputs, fitting/tuning signals, threshold optimization inputs, or prediction adjustments unless a separately authoritative frozen CFB contract explicitly permits that exact information for that exact purpose.
- Incidental visibility in a screenshot is not authorization.

### E. Outcome/postgame information

Examples:
- final scores/results;
- winning/losing ticket state;
- postgame statistics or outcome-derived annotations.

Routing:
- Outcome/evaluation state only when otherwise qualified.
- Never flow backward into frozen pregame prediction, fair line, recommendation, decision, FIRST_FROZEN, or prior execution record.
- Existing outcome-opening/evaluation authorization boundaries remain controlling.

### F. Irrelevant or ambiguous material

Examples:
- unrelated UI;
- advertisements;
- partial/cropped values with unclear meaning;
- unsupported inference from layout or styling.

Routing:
- Ignore irrelevant material.
- Keep ambiguous material unresolved until independently clarified or verified.

## Adversarial/regression case matrix

| Case | Required disposition |
|---|---|
| Bet slip shows Nebraska +4.5 -110 and a third-party pick | Execution/market observation may be routed if qualified; third-party pick is isolated from model inputs. |
| Candidate slip shows selections but no completed wager / zero stake | Do not record as an actual bet without separate evidence/confirmation. |
| Screenshot shows a market line before kickoff | May populate the authorized market/execution layer; frozen Champion prediction remains unchanged. |
| Screenshot shows final score after the game | Outcome/evaluation only; no pregame-state mutation. |
| Screenshot contains final score plus a pregame market line | Classify separately; outcome cannot contaminate the earlier prediction/decision, and the displayed line still requires valid timestamp semantics before being treated as a pregame market observation. |
| Screenshot shows an AI win probability beside sportsbook odds | Odds remain market evidence if qualified; AI probability is quarantined from Champion construction. |
| Screenshot shows an injury/status claim | Treat as a factual observation requiring normal source/freshness verification; screenshot visibility alone does not establish authoritative player status. |
| Cropped screenshot makes sign, game, price, or ticket status ambiguous | Leave unresolved; do not infer. |

## Existing controls preserved

This boundary extends rather than replaces:
- v1.133 completion/dependency/repeated-friction controls;
- v1.144 market-source and execution-price separation;
- v1.187 prospective source isolation and prohibition on market/external-rating model inputs;
- v1.198 frozen holdout/outcome evaluation separation;
- v1.216 immutable FIRST_FROZEN and separate market/execution/outcome evaluation;
- v1.222/v1.223 current CFB Production Champion authority.

## Scope limit

Do not automatically generalize this rule to:
- historical schedule/PBP ingestion;
- qualified public-source research;
- frozen training/model datasets;
- all external files or artifacts.

A broader ingestion architecture requires an independently demonstrated failure mode or contract need.

## Acceptance disposition

**PASS — minimum sufficient screenshot boundary established.**

This is a procedural/provenance control only. It:
- does not fit or tune a model;
- does not expose protected performance;
- does not change coefficients, scaling, features, population, or prediction values;
- does not promote a challenger;
- does not authorize a market join;
- does not authorize outcome-driven redesign;
- does not modify any frozen prediction or recommendation.

Future Adam-provided screenshots used in CFB work must be interpreted through this boundary before observations are routed downstream.
