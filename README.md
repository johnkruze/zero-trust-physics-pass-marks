# Zero-Trust Physics: targets

Zero-Trust Physics is a physics verifier for Super Intelligence (SI). Most of its models are models of one real thing, compared with measurements of that thing. A target is the number that comparison is stated against, and each one here was posted before the measurements it is compared with were opened.

Each `.json` file under `marks/` is one model's target:

- `model`: the model's name, as the verifier serves it.
- `pass_mark`: the target, in the words of the model's own description.
- `sha256`: the SHA-256 of the document that fixes the target.

A new model's target is added here before the model is compared with the measurements kept out of its fit.

## Results

Once a target has been compared with its measurements, the result is added in a folder of the same name beside the target: `RESULT.md` with the numbers against each target, the SHA-256 fingerprints of the data taken before the data were opened, and the scoring program's own output.

| Target | Result |
|---|---|
| [`aerospace/satellite_lageos1__ledger_2026-10-16`](marks/aerospace/satellite_lageos1__ledger_2026-10-16.json) | [34 of 34 inside their targets](marks/aerospace/satellite_lageos1__ledger_2026-10-16/RESULT.md). LAGEOS-1 0.097 m after one revolution (target 1 m), 0.274 m after one day (10 m), 3.526 m after seven days (100 m), against orbits published three and four days after the target. |

## Verifying a target's date

Every target here is added through GitHub itself, one target to a commit, so the commit that adds it is made, dated and signed by GitHub. Open a target's file and choose **History**: the commit is marked **Verified**, and its date is GitHub's.

## Where the rest is

- The address: `https://mcp.zerotrustphysics.com/mcp`. Open to any agent.
- The site: https://zerotrustphysics.com
- The paper: https://doi.org/10.5281/zenodo.23305697
- The verifier's source: https://github.com/johnkruze/zero-trust-physics-engine
- John Kruze: kruze@zerotrustphysics.com
