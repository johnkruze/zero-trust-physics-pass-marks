# Zero-Trust Physics: validation targets and replays

Zero-Trust Physics is a deterministic physics runtime with a proof on every answer. Most models represent one real physical system and state comparison targets and out-of-sample error against published measurements.

Each `.json` file under `marks/` holds one model's target:

- `model`: the model's name, as served by the runtime.
- `pass_mark`: the validation target stated in the model's description.
- `sha256`: the SHA-256 of the document fixing the target.

## Results

Once a target has been compared with its measurements, the result lives beside it in `RESULT.md`, together with the SHA-256 fingerprints of the input datasets and the scoring program output.

| Target | Result |
|---|---|
| [`aerospace/satellite_lageos1__ledger_2026-10-16`](marks/aerospace/satellite_lageos1__ledger_2026-10-16.json) | [34 of 34 inside their targets](marks/aerospace/satellite_lageos1__ledger_2026-10-16/RESULT.md). LAGEOS-1 0.097 m after one revolution (target 1 m), 0.274 m after one day (target 10 m), 3.526 m after seven days (target 100 m), compared against the published ILRS orbit. [Replay it](marks/aerospace/satellite_lageos1__ledger_2026-10-16/REPLAY.md). |

## Replays

A replay pairs exact MCP tool requests against reference measurements and comparison scripts.

| Model | Replay |
|---|---|
| `aerospace/satellite_lageos1` | [The LAGEOS forecast](marks/aerospace/satellite_lageos1__ledger_2026-10-16/REPLAY.md): exact `run_trajectory` call and `distance.py` against the ILRS orbit. |
| `ablator_slab` | [Against NASA's FIAT and the Stardust flight](marks/ablator_slab/REPLAY.md): Ablation Workshop Test Case 1 within 0.633% RMS of FIAT; Stardust wear 7.58 and 3.32 mm against 5.7 and 3.2 measured. |

## Links

- Open MCP endpoint: `https://mcp.zerotrustphysics.com/mcp`
- Website & `/llms.txt`: https://zerotrustphysics.com
- Self-serve RLVR Domain Packs ($9,500) & Bundle ($39,500): https://zerotrustphysics.com/offers/fast-start/
- Hugging Face organization: https://huggingface.co/zero-trust-physics
- Paper (version 2.0): https://doi.org/10.5281/zenodo.23517223
- Engine reference source (`v0.15.2`, Apache-2.0): https://github.com/johnkruze/zero-trust-physics-engine
- John Kruze, CEO: kruze@zerotrustphysics.com

---

Protocol Company.
