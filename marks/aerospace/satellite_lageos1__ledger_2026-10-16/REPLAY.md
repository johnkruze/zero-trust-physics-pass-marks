# Replay the LAGEOS forecast

The forecast in `RESULT.md`, in two steps an agent can run: the engine's call, then the distance from the published orbit. Every number below was reproduced from these files and the open address on 26 October 2026.

## 1. The call

Send this as the arguments of `run_trajectory` to `https://mcp.zerotrustphysics.com/mcp` (open, no key). It is LAGEOS-1 from GFZ's published state of 4 October 2026, 0 h UTC, seven days of 10 s steps, nothing fitted, and it returns the final state alone (about 10 kB):

```json
{"domain": "aerospace", "card": "satellite_lageos1", "initial": {"epoch_utc_s": 844344000.0, "forecast_elapsed_s": 0.0, "position_m": [10037279.556667194, 1762618.1980166798, -6799582.533745239], "velocity_m_s": [-2335.484193752763, -3527.6049343930795, -4324.697780872672]}, "dt_s": 10.0, "segments": [{"steps": 60480, "load": {}}], "record_every": 60480}
```

The answer, on engine 0.15.2 (`genesis_kernel_v0.13.1`): `outcome` `completed`, 60,480 steps landed, final `position_m_hex` `["41435c0e93758e13", "41535a4efdf479df", "4164db00a3432eb3"]`, run seal `fb8f811d1a8a3f673e6b6cd6d12683883ac9fea07e51a7ee4879bc0edd5ff153b95d4486dd98268ffc5dcd2f9913449a`, signed ML-DSA-87. `verify_tape` with `{"request": <the request above>, "run_seal": <that seal>}` holds.

That final position is the sealed forecast's to the bit: `forecast/lageos1_forecast_answer.json`, computed on 16 October on engine 0.12.0 (`genesis_kernel_v0.11.0`). The forecast as it was sent, a frame every 120 s, is `forecast/lageos1_forecast_request.json` (answer about 1.6 MB). On engine 0.15.2 every one of its 5,040 frames carries the same first 48 bytes as the sealed forecast: time, position, velocity, residual and flags. The last 16 bytes of each frame, its proof slot, and the run seal bind the engine version, so they differ.

LAGEOS-2: `forecast/lageos2_forecast_request.json` with `record_every` 60480 gives final `position_m_hex` `["c166e729d3804b6f", "c123474e07ec4eca", "41431c6c42a288a1"]`, run seal `d67f040c856e1eddd5db5ec1ac566621d56ab0c858e7b38091296c1e99eb61459b6a1a54ef5fa34dd07519a6a793dd53`, the sealed forecast's final position to the bit.

## 2. The distance from the published orbit

The ILRS combined orbit of week 261010, published at the EUROLAS Data Center on 21 October, after the target was dated by GitHub on 17 October (`ftp_listing_*.txt` in this folder):

| File | SHA-256 |
|---|---|
| `ftp://edc.dgfi.tum.de/pub/slr/products/orbits/TRF/lageos1/2026/261010/ilrsa.orb.lageos1.261010.v80.sp3.gz` | `0c95e694376ac111dc502b71225951c8c4d47b96dfbd0339da60ca3e3d4aad4f` |
| `ftp://edc.dgfi.tum.de/pub/slr/products/orbits/TRF/lageos2/2026/261010/ilrsa.orb.lageos2.261010.v80.sp3.gz` | `92bfec1a2372cdf16b945e34edf191a5dc572f723849d815b8a2131ff67de103` |

`python3 distance.py forecast/lageos1_forecast_positions.csv ilrsa.orb.lageos1.261010.v80.sp3.gz` prints:

```
one revolution     0.097 m over  113 epochs (target 1 m)
one day            0.274 m over  720 epochs (target 10 m)
three days         0.853 m over 2160 epochs (target reported only)
seven days         3.526 m over 5039 epochs (target 100 m)
```

and for LAGEOS-2, 0.355, 1.348, 4.419 and 11.148 m over the same epochs. `distance.py` is 53 lines of Python with nothing imported beyond the standard library.

## 3. What joins the two steps

- **The start.** `validation_protocol.md` §3 gives GFZ's position and velocity at 2026-10-04 0 h, the last epoch of `gfz.orb.<satellite>.261003.v80.sp3.gz` (SHA-256 in §9), both Earth-fixed and turned into the card's frame. The request above holds the card-frame numbers.
- **The positions.** `forecast/<satellite>_forecast_positions.csv` is the sealed answer's frames, every 120 s, turned into the Earth-fixed frame (`itrf_*`) and the celestial frame (`gcrs_*`): IAU 2006/2000A precession and nutation ported from ERFA, the Earth rotation angle and polar motion from IERS Bulletin A (`finals2000A.daily`, SHA-256 `3a90113339dc3dd726867d9541d4a8468535b7e1ec9d3966d6c01166a81b6d89`), and the IERS sub-daily terms. Both frames are written, so the turn can be verified with any implementation of those standards (ERFA, SOFA, Astropy).
- **The fingerprints.** `validation_protocol.md` has SHA-256 `92cfb3802f77a398ae9b37c89e64a338aa55d14a368c58dc8ecd5ed1ee34659b`, the `sha256` of the target `../satellite_lageos1__ledger_2026-10-16.json`, added and dated by GitHub in commit `50ceb1d`. It names `forecast/forecast_manifest.json` by its SHA-256 (`d2ccadba…03a5`), and the manifest names every forecast file by its SHA-256, the requests, answers and positions here among them.

The orbit files are the ILRS's. Citation the ILRS asks for: Pearlman, M.R., Noll, C.E., Pavlis, E.C. et al., "The ILRS: approaching 20 years and planning for the future", J Geod 93, 2161–2180 (2019), doi:10.1007/s00190-019-01241-1. Keyword: SLR.

Super Intelligence on behalf of Protocol Company, 26 October 2026.
