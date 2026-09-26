# CFB Engine — 2025 Outcome Source Reproducibility Addendum v1.219

Status: **PASS — RAW 2025 OUTCOME SOURCE IDENTITY RECOVERED FROM ACCEPTED EXECUTION LOG**
Parents: v1.196, v1.197, v1.198
This is an append-only reproducibility checkpoint. It does not rewrite or supersede v1.198's evaluation conclusions.

## Recovered source identity
Accepted scoring run **36215340850**, job **108330081156**, explicitly acquired:
`https://raw.githubusercontent.com/sportsdataverse/cfbfastR-cfb-data/main/cfb/cfb_schedules/parquet/cfb_schedules_2025.parquet`

The run printed the raw file SHA-256 before scoring:
`a9b131aec16fa32540882f9438c81feb5a57c3279ee4b9fa6c95d91675e02a3c`

That is the exact raw 2025 schedule/outcome source byte identity used by the accepted v1.196 scorer.

Independent audit run **36215607213**, job **108330856606**, reacquired the same named raw source and used it to independently audit the frozen predictions and accepted scoring artifact. Its accepted audit artifact remains **10896839520**, digest `sha256:33a2efbc3dde5cd0376c926f14155d64bd02c76959dcf9999ea06d791ec14ae0`.

## Authority effect
The previously noted reproducibility omission in v1.198 is now closed by exact execution-log recovery. No outcome was rescored, no prediction was regenerated, and no model/feature/calibration/threshold/market/promotion decision changed.

The raw source SHA above also matches the raw 2025 SHA already frozen in the earlier v1.157 corrected-population authority, providing additional identity consistency.
