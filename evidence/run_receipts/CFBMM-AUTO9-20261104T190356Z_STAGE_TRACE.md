# Structured stage trace
correlation_id: CFBMM-AUTO9-20261104T190356Z
classifier_execution: NOT_RUN
- timestamp_utc: 2026-11-04T19:03:56Z; stage: CONNECTOR_ATTEMPT; outcome: PASS; failure_category: NONE; sanitized_error_excerpt: none; fallback_attempted: false; fallback_result: not_needed; required_for_this_invocation: true
- stage: RUN_STARTED_READBACK; outcome: PASS; blob: 08dab89d69d7d1cc2c034293f3d1194ff4ae0164; required_for_this_invocation: true
- stage: AUTHORITY_RECOVERY; outcome: PARTIAL; index_v1_252: a5995cccca420ccde82e37dbc0a6a7e6d4623ed7; original_prompt: fb81b86d0b438fb9e84ce34b618c2c6919ededcd; fallback_attempted: false; required_for_this_invocation: true
- stage: WEDNESDAY_RECHECK; outcome: INCOMPLETE; failure_category: MISSING_INPUT; sanitized_error_excerpt: authenticated offer/update clock and game-day QB material absent; fallback_attempted: true; fallback_result: public aggregator historical market observations only; required_for_this_invocation: true
- stage: PRODUCER_AND_PUBLICATION; outcome: BLOCKED; failure_category: MISSING_INPUT; fallback_attempted: false; fallback_result: not_applicable; required_for_this_invocation: true
