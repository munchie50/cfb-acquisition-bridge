# Production Market Monitor scheduled Git checkout test — November 9 CT

User-authorized prompt-only update on task 6ae766e788d881919726d0eeb44450dd. Independent scheduler readback verified the full prompt and original identity, title, enabled state, schedule, time zone, timing mode and inherited environment selection. No new task.

After verified startup and authenticated main/helper identity, the scheduled worker tries one ordinary noninteractive Git remote probe, bounded to 10 seconds. If it can reach main, it attempts one full clone with a 180-second timeout and one 50-second verification phase for pinning, nonshallow ancestry, helper identity, required scripts and exact retained reviews via the existing validator. The same verified checkout feeds production. If the probe fails before a clone, the existing transport fallback remains available. A clone attempt cannot be followed by a second clone.

This verifies installation only. Next evidence is the natural November 10 07:00 CT production cycle, with distinct probe, clone, review validation and full workflow outcomes. If ordinary Git succeeds, a maintained single pinned checkout path can replace helper transport discovery after end-to-end scheduled proof. If the worker cannot reach Git, a supported scheduled execution environment with reliable authorized Git access is required. The prompt cannot provision that environment.

Nominal incremental shell probe cap is 10 seconds; clone and verification replace the existing bootstrap on the successful path, with 240 seconds of combined configured bounds. Actual scheduled latency is unmeasured. No extra scheduled invocation or paid market-data request is part of the test.

Prior controlled test and ancestry: f7616aac7d0328e5f8f3b2a237ba9c5f0d0699e6. Monday failing production: 7fdc64d09f88aaf4528cd77020232c42d73ceb9c.
