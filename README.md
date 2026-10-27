# Zero-Trust Physics: targets

Zero-Trust Physics is a physics verifier for Super Intelligence (SI). Most of its models are models of one real thing, compared with measurements of that thing. A target is the number that comparison is stated against.

**When each target was posted.** GitHub's date on a target witnesses when it was posted, and nothing earlier. The 35 targets added on 13 October 2026 were posted after the comparisons they state: by our own records, 33 of them were scored between 6 and 11 October; the TRIGA fuel element (`fuel_rod_triga_jsi`) was scored after it was posted, on 18 October; for `fusion_pb11_thermal` our records give no scoring date. Since 16 October every new target is posted before its data are opened or exist: the LAGEOS forecast (posted 17 October, scored 22 October against orbits published 21 October, 34 of 34 inside) and Curiosity's generator (`generator_mmrtg_seebeck`, posted 17 October, waiting for its data).

Each `.json` file under `marks/` is one model's target:

- `model`: the model's name, as the verifier serves it.
- `pass_mark`: the target, in the words of the model's own description.
- `sha256`: the SHA-256 of the document that fixes the target.

From 16 October 2026, a new model's target is added here before the model is compared with the measurements kept out of its fit.

## Results

Once a target has been compared with its measurements, the result is added in a folder of the same name beside the target: `RESULT.md` with the numbers against each target, the SHA-256 fingerprints of the data taken before the data were opened, and the scoring program's own output.

| Target | Result |
|---|---|
| [`aerospace/satellite_lageos1__ledger_2026-10-16`](marks/aerospace/satellite_lageos1__ledger_2026-10-16.json) | [34 of 34 inside their targets](marks/aerospace/satellite_lageos1__ledger_2026-10-16/RESULT.md). LAGEOS-1 0.097 m after one revolution (target 1 m), 0.274 m after one day (10 m), 3.526 m after seven days (100 m), against orbits published three and four days after the target. [Replay it](marks/aerospace/satellite_lageos1__ledger_2026-10-16/REPLAY.md): the one call, and the distance from the published orbit. |

## Replays

A replay is a result put in calls an agent can make at the open address, with the files that join each call to what it is compared with.

| Model | Replay |
|---|---|
| `aerospace/satellite_lageos1` | [The LAGEOS forecast](marks/aerospace/satellite_lageos1__ledger_2026-10-16/REPLAY.md): the call that reproduces the sealed forecast's final position to the bit, and `distance.py` against the ILRS orbit. |
| `ablator_slab` | [Against NASA's FIAT and the Stardust flight](marks/ablator_slab/REPLAY.md): Ablation Workshop Test Case 1 within 0.633 percent root mean square of FIAT; Stardust wear 7.58 and 3.32 mm against 5.7 and 3.2 measured. No target was posted for these. |

## Verifying a target's date

Every target here is added through GitHub itself, one target to a commit, so the commit that adds it is made, dated and signed by GitHub. Open a target's file and choose **History**: the commit is marked **Verified**, and its date is GitHub's.

## Where the rest is

- The address: `https://mcp.zerotrustphysics.com/mcp`. Open to any agent.
- The site: https://zerotrustphysics.com
- The paper: https://doi.org/10.5281/zenodo.23517223
- The verifier's source: https://github.com/johnkruze/zero-trust-physics-engine
- John Kruze: kruze@zerotrustphysics.com
