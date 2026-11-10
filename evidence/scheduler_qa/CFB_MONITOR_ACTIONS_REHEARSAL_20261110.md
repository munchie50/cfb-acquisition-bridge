# Market Monitor GitHub Actions rehearsal — November 10, 2026

Status: isolated fixture execution demonstrated and independently verified. Production migration remains open.

- Initial run 42893797543 failed the ancestry gate because the QA workflow commit was supplied as the production checkout pin. The correction separated the workflow commit from the authenticated fixture revision. The existing ancestry check remained active.
- Run 42893819934, job 130101544031, workflow commit a6af1b82347ddb1b26198d16197ae2df89f04c95: read-only hosted runner passed checkout and pinned production ancestry at 37d692d65b05632a376d31cdefbd3ec23ef5103e, validating 51 immutable reviews. All three existing Week 11 tests passed. The real compiler and renderer produced and read back the 67-game controlled fixture.
- Artifact 13799352356 was separately downloaded. Its ZIP SHA-256 matched GitHub (c9e8e923869b1ce2d1e299abbce34a4fbcea5240efc50d88ee03f79b73d62e71). The five expected files, pinned revision, 51 reviews, 67 games and actual sheet Git blob 69644e57c80f691ee11527b74024be21ac95a93d were independently verified.

The runner passed the checkout boundary that blocked the scheduled ChatGPT Monitor. The run used retained source evidence and synthetic decision rows. Next proof: approved live-source access and a real reviewed input packet handed to this runner for a shadow compile, render and independent output verification. Existing production cadence and publisher authority were not changed.
