# Market Monitor preflight failure containment

Main commit ea61418bd3679197f9917c7deae01b61e6855771 preserves the existing source upload and makes subsequent read-only preflight verification, compilation and upload individually optional and time-bounded. Raw step outcomes gate dependent work and produce an explicit warning and job summary on failure. Collection and its upload remain required. Job ceiling is eight minutes; source collection has a two-minute step ceiling. Existing schedules and consumer eligibility rules are preserved.

Production push run 43356325560 passed collection, verification, compilation and both uploads. Source artifact 14006640840 and preflight artifact 14005633943 independently confirmed by Actions metadata.

Isolated QA run 43356349146 injected compiler exit 19. Logs confirmed verify=success, compile=failure, upload=skipped, and the warning ran. Job succeeded and only the source artifact 14005509702 was returned. This proves optional compiler failure does not spoil collector success. Schedule-origin eligibility, actual worker consumption, authored decision transport and final canonical publication remain open. The next existing daytime schedule pair is Friday 06:52/07:00 CT.
