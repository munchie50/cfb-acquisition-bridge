# CFB Engine — Challenger B Corrected Feature Diagnostic Review v1.168

Status: NOT ACCEPTED / PRODUCER CLASSIFICATION DEFECT ISOLATED

Run 36210213910 completed SUCCESS at head ffaf87f3a9496af63175f2c71ef96ab18380d16c.
Artifact 10895043563; digest sha256:dc73b08becd58d9f834da3093f3d804ab4b64bbb0efe24361e7a0e27464e6543.

Independent readback confirmed:
- 7,701 target games / 15,402 target team-sides, no duplicate target keys;
- all seasons limited to 2016-2024; no 2025 access; no fit or score;
- exact 1,342 newly admitted v1.158 games represented;
- 1,922 opening/no-prior team-sides separately ledgered;
- fail-closed prior-history propagation is present.

Acceptance is withheld because v1.168 conflates game-level PBP availability with team-side primitive materialization. It marks 55 games / 100 team-sides as own mechanical/derived primitive incomplete, whereas accepted v1.165 proves exactly 45 game IDs lack cfbfastR PBP.

The ten extra games are PBP-present FBS-vs-non-FBS games in which the non-FBS team name is not materialized as a matching pos_team/def_pos_team primitive row:
400869356, 400869808, 400944831, 401013102, 401014979, 401309541, 401416568, 401532393, 401644732, 401644737.

This is a classification/identity-materialization issue, not evidence that those ten game IDs lack PBP. v1.165 remains authoritative for game-level source availability. v1.168 output is diagnostic only and must not be accepted as Challenger-B feature substrate until source availability and team-side primitive qualification are represented separately and the ten identities are reconciled without synthetic zero substitution.

No model fitting/scoring or 2025 access authorized.