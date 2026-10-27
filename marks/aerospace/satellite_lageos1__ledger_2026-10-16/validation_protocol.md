# Validation protocol: `satellite_lageos1`, forecast from the latest published orbit (ledger of 2026-10-16)

**Ledger name:** `satellite_lageos1__ledger_2026-10-16`, a registration of `protocol_mcp_gateway/kit/forecast.py`
in the gateway Git of the build copy `genesis_workspace/.build_2026-10-15/prospective/` (branch
`feat/prospective-forecasts-013`). It is not the served card's registration (`kit/forecasts/satellite_lageos1.json`)
and the served sweep does not read it: `forecast_findings` reads only `kit/forecasts/<served name>.json`.
**Written:** 2026-10-16 (UTC) by Claude, before any orbit of the days it forecasts is published.
**Data:** the ILRS weekly orbit product, EUROLAS Data Center (EDC), product doi 10.5067/SLR/SLR_ILRSORB_001. Citation the
ILRS asks for: Pearlman, Noll, Pavlis et al. (2019), J Geod 93, 2161-2180, doi 10.1007/s00190-019-01241-1. Keyword: SLR.
**The original comparison:** `../validation_protocol.md`, scored on 2026-10-06 (`../analysis/out/10_engine_comparison_sealed.log`):
42 held-back runs, every line met, worst 0.646 m at one revolution, 3.821 m at one day, 31.924 m at seven days (LAGEOS-1);
0.342, 2.907 and 21.510 m (LAGEOS-2).

## 1. What is tested

The served card `satellite_lageos1` as it is: kernel source unchanged from engine 0.12.0, served at the open address
(`evidence/verification/engine_0.12.0_served/mcp_stdio`, SHA-256 `fec124af6940a02d2eb617423f4cb00f8c503ce432be0864a02cc6dd7453d241`).
The forecast was computed with the `cargo build --release` of the build copy (`mcp_stdio`, SHA-256
`511327569d0689f12f2b4d1026de0d1a45f5aad0a729a337e603be8649ee3a54`, kept as
`evidence/research/momentum_jwst_srp/ledger_2026-10-16/engine/mcp_stdio`); the served binary, asked the same two requests,
gave the same answers byte for byte and verifies them in both forms. Both satellites, as the original did: LAGEOS-1, the card's
satellite, and LAGEOS-2, its second tier. Nothing is fitted; no constant, line or rule of the original is changed.

## 2. When the data exist

The EDC moved the LAGEOS orbits on 2026-10-08 from `orbits/rapid/<satellite>/<week>/` to
`orbits/TRF/<satellite>/<year>/<week>/` (listings in `raw/listings/`, 2026-10-16 05:20Z). A week runs Sunday 0 h to Saturday,
named by its Saturday. The product comes about ten days after its week: week 260919, GFZ 09-29 19:04, combined 09-30 12:07;
week 261003, GFZ 10-13 19:01, combined 10-14 12:55 UTC.

So on 2026-10-16 **the latest published state is the last epoch of GFZ's orbit of week 261003, 2026-10-04 0 h UTC**, and no
orbit of any later day is published. The seven days after it, 2026-10-04 0 h to 2026-10-11 0 h, are past dates whose orbit no
one has published: the task's premise that they lie in the future does not hold; the premise that no one has read them does.
Their orbit is the product of week **261010**, expected about 2026-10-20 19:00 (GFZ) and 2026-10-21 13:00 UTC (combined).
A combined orbit can be missing: week 260926's `ilrsa` is a 308-byte file, and a stray folder 261001 holds another.

**The held-back files, named before they exist** (`forecast.py register` fingerprints a file on disk and cannot register one
by name, so they are fingerprinted when fetched, section 7):
`ftp://edc.dgfi.tum.de/pub/slr/products/orbits/TRF/<satellite>/2026/261010/<centre>.orb.<satellite>.261010.v80.sp3.gz` for
satellite `lageos1` and `lageos2` and centre `gfz`, `ilrsa` and `ilrsb`: six files.

## 3. Part A: the forecast, computed now

From the last epoch of `gfz.orb.<satellite>.261003.v80.sp3.gz` (fetched 2026-10-16 05:28Z, `raw/edc_start_week_261003/`),
GFZ's position and velocity at 2026-10-04 0 h UTC are turned into the card's frame exactly as the original comparison does it
(the true pole and Earth Rotation Angle of the start epoch, velocity by the full derivative, the frame's turning removed;
`analysis/lageos_ledger.py`, the original's `earth_orientation.py` and `subdaily_earth_rotation.py` unchanged), with IERS
Bulletin A `raw/iers/finals2000A.daily` (fetched 2026-10-16 05:28Z; every row from MJD 61313 to 61328 observed, flag I). The
velocity-record check of the original (section 9, step 3) passes on both start files (shares within 0.0040 of zero against 0.05).
One run each: `run_trajectory`, `dt_s` 10, 60,480 steps, a frame every 12 steps, completed; both forms of `verify_tape` hold.

| | LAGEOS-1 | LAGEOS-2 |
|---|---|---|
| Start, crust-fixed (m) | 10037273.879, 1762628.864, -6799588.150 | 1505230.256, 7337643.748, -9393076.103 |
| Start velocity, crust-fixed (m/s) | -2335.4877696, -3527.5981470, -4324.7013112 | -5194.1069346, 25.6624847, -855.0214915 |
| `initial.position_m` (card frame) | 10037279.556667194, 1762618.1980166798, -6799582.533745239 | 1505238.0995434925, 7337629.01456205, -9393086.355465433 |
| `initial.velocity_m_s` | -2335.484193752763, -3527.6049343930795, -4324.697780872672 | -5194.1062674226705, 25.661142223977933, -855.0258775506326 |
| `epoch_utc_s`, `forecast_elapsed_s` | 844344000.0, 0.0 | 844344000.0, 0.0 |
| `run_seal` | `9bcfff3508039acd262f90c4439a223ecd0af6944db86728a853e036a3fd9b72` | `f9905867dab9b04a8edcbefc0493d0cd78651fffe8bcb744e2332400e55287e8` |
| `receipt_sha256` | `8224ebaf96326cd5904cbffe181bba0c51ebd4c38056a09303ed4eb797edcaf7` | `e8240d4686e7780db99df42891a4ec465a740b8c5405c17c3289e47e27bfd720` |
| Frames; in the Earth's shadow | 5,040; 529 | 5,040; 869 |
| Forecast crust-fixed position at 2026-10-04 03:46 (one revolution) | 6883145.320, -7392819.305, -6931057.853 | 6276372.780, 3791790.725, -9526550.837 |
| at 2026-10-05 00:00 (one day) | -11122719.374, -5094385.501, -810805.422 | -3919429.574, -7248836.008, 9156643.368 |
| at 2026-10-10 23:58 (seven days) | 1859119.610, 4940964.923, 11129893.747 | -12111627.008, -321403.432, 1977357.348 |

The forecast is the sealed answer itself (`analysis/out/forecast/<satellite>_forecast_answer.json`), every 120 s epoch from
2026-10-04 00:02 to 2026-10-11 00:00, also written crust-fixed and celestial in `<satellite>_forecast_positions.csv`; every
file's SHA-256 is in `analysis/out/forecast/forecast_manifest.json`, SHA-256
**`d2ccadba5feef0deb8de36e83111ea0dc634b22c890ae38aca31ceb1bb7903a5`**, which the scoring program checks before it reads anything.

**What the distances will be.** The same design run on the spent weeks (`analysis/30_forecast.py hindcast`,
`analysis/out/hindcast.json`: the end of GFZ's week N, scored on the combined orbit of week N+1), largest 3-D distance:

| | N | one revolution | one day | three days | seven days | the original's run from week N+1's own start |
|---|---|---|---|---|---|---|
| LAGEOS-1 | 260829 / 260905 / 260912 | 0.197 / 0.422 / 0.289 m | 0.847 / 3.666 / 1.319 | 3.42 / 12.56 / 4.15 | 7.77 / 31.78 / 10.92 | 0.65 m, 3.82 m, 31.9 m at worst |
| LAGEOS-2 | 260829 / 260905 / 260912 | 0.120 / 0.095 / 0.187 m | 1.352 / 1.630 / 0.709 | 6.15 / 5.79 / 2.82 | 21.22 / 14.96 / 8.92 | 0.25 m, 1.82 m, 21.5 m at worst |

Starting from the end of the previous week's fit costs little against the week's own start. What is new in this week:
**both satellites cross the Earth's shadow** (529 and 869 of 5,040 frames). LAGEOS-1 was in sunlight in every week it was
compared on; LAGEOS-2 was in shadow in week 260919 (338 frames) and met every line there.

**Forecast, part A**, largest 3-D distance from the combined orbit:

| | one revolution | one day | three days (reported) | seven days | every line met |
|---|---|---|---|---|---|
| LAGEOS-1 | 0.2 to 0.8 m | 1 to 7 m | 3 to 25 m | 8 to 50 m | yes, about 4 chances in 5 |
| LAGEOS-2 | 0.1 to 0.5 m | 0.5 to 4 m | 2 to 15 m | 5 to 35 m | yes, about 9 in 10 |

The line most likely to be missed is LAGEOS-1's one revolution (1 m), from the shadow and the end-of-fit start.

## 4. Part B: the original's seven starts on the new week

The original comparison, unchanged, on week 261010: GFZ's own position and velocity at 0 h of each day d = 0 to 6 of the week,
turned the same way, run 60,480 steps (d = 0), 25,920 (d = 1 to 3), 8,640 (d = 4, 5) and 1,356 (d = 6), scored at the
horizons of `../analysis/prereg.json`. Computed at scoring, from a file that does not exist yet; the engine is deterministic, so
the card's answer to each start is fixed by the card as served. Forecast, from the original's 42 runs and the shadow:

| | one revolution, 7 starts | one day, 6 starts | seven days, 1 start | every line met |
|---|---|---|---|---|
| LAGEOS-1 | each 0.1 to 0.9 m | each 0.5 to 7 m | 8 to 50 m | yes, about 3 chances in 4 |
| LAGEOS-2 | each 0.05 to 0.5 m | each 0.3 to 4 m | 5 to 35 m | yes, about 9 in 10 |

Forecast verdict, parts A and B, both satellites: **met**, about two chances in three.

## 5. The marks

As the original (`../validation_protocol.md` sections 5 and 6), unchanged:

- One quantity: the 3-D distance between the card's position, rebuilt from the sealed frames only (`pos[i] + vel[i]` as 64-bit
  numbers), turned back by the exact inverse of the card's uniform turning, and the reference orbit's position at the same epoch,
  turned by the full Earth-orientation model with the Bulletin A file of section 3.
- Gated: the largest distance over every 120 s epoch up to the horizon: **at most 1 m within one revolution (13,560 s), 10 m
  within one day (86,400 s), 100 m within seven days (604,680 s)**; three days (259,200 s) reported only. A horizon passes when
  the run reached it, every epoch up to it was scored, the distance is inside the line and both forms of `verify_tape` hold
  (part A: and the card's frame recomputes bit for bit).
- The reference: the primary combined orbit `ilrsa` v80, when it holds 5,040 epochs from 2026-10-04 0 h every 120 s; if not,
  the backup combination `ilrsb` v80 by the same test; if neither, the satellite is **void** (no score, no pass).
- Part B is void for a satellite when its GFZ file is missing or incomplete, or a share of its velocity-record check is beyond 0.05.
- Verdict: **met** when every gated line of parts A and B is met on both satellites; **missed** when any gated line of
  LAGEOS-1 is missed or a LAGEOS-1 part is void while the other is scored; **met in part** when LAGEOS-1 meets every line and
  LAGEOS-2 misses one or is void; **void** when LAGEOS-1 has no reference. Every run is reported, pass or fail.

## 6. The scoring program

`analysis/31_score.py` (with `analysis/lageos_ledger.py`), run once. Rehearsed before registration on the design moved back to
spent weeks (`analysis/32_rehearse_scoring.py`, `analysis/out/rehearsal_260912_to_260919/`): part A gave the hindcast's numbers
(0.289, 1.319, 10.923 m for LAGEOS-1) and part B the original sealed runs of week 260919 on all 14 starts to the millimetre
(LAGEOS-1 d0: 0.252, 0.967, 8.752 m), from the served binary.

## 7. To open and score, on John's word

From the Spectrum folder, `G=genesis_workspace/.build_2026-10-15/prospective`, `F=evidence/research/lageos1_orbit/ledger_2026-10-16`:

1. From 2026-10-21 14:00 UTC, once the folder `TRF/<satellite>/2026/261010/` lists `gfz` and `ilrsa` v80 for both satellites
   (or on 2026-10-28 with whatever it lists): `python3 -I -B $F/analysis/33_fetch_unread.py $F/raw/week_261010`. It keeps the
   listing, size and SHA-256 and reads nothing.
2. `python3 $G/protocol_mcp_gateway/kit/forecast.py register satellite_lageos1__ledger_<date of the fetch> --protocol $F/validation_protocol.md --held-back $F/raw/week_261010/*/*.sp3.gz`
   fingerprints the fetched files in a second registration of this same protocol, committed before any is opened.
3. Each file: `python3 $G/protocol_mcp_gateway/kit/forecast.py open satellite_lageos1__ledger_<date of the fetch> <file>`.
4. `python3 -I -B $F/analysis/31_score.py evidence/verification/engine_0.12.0_served/mcp_stdio $F/raw/week_261010 $F/analysis/out/scored`.
5. `python3 $G/protocol_mcp_gateway/kit/forecast.py score satellite_lageos1__ledger_2026-10-16 --output $F/analysis/out/scored/score.json --program $F/analysis/31_score.py`,
   and the same for the fetch-date name. The result goes in a `RESULT.md` beside this file, as it comes out.

If a program stops on an error before writing its output, the error and any change made to let it finish are reported; no line,
constant or rule changes.

## 8. Exposure

Seen before this was written: the EDC listings of `orbits/`, `orbits/rapid/`, `orbits/TRF/lageos1|2/`, their 2026 folders and
the files of weeks 260919, 260926, 261001 and 261003 (names, sizes, dates); the two GFZ files of week 261003, read whole for
the start state; Bulletin A to 2026-10-15 and the leap-second file (identical to the original's); for the hindcast, the spent
weeks 260829 to 260919 already on disk from the original (opened in its runs of 2026-10-06). No file of week 261010 exists; no
laser range and no orbit of 2026-10-04 or later has been read. The ILRS normal points of those days are public at the data
centres and were not fetched. The combined orbit of week 261003 was not fetched.

## 9. Files, SHA-256 at registration

| File (this folder) | SHA-256 |
|---|---|
| `analysis/lageos_ledger.py` | `476b107820e44f6758c5bc83d2fdef486d3960bfa2bc0490bbeb59486afd50ab` |
| `analysis/30_forecast.py` | `202a0552ea2a5c7c779f2666093acc65b65bb06144d9b2865db835c52da54463` |
| `analysis/31_score.py` | `4461faad90b2c14c6033401f97dd4cdf7a031622e6fc198c116151cb83b366fe` |
| `analysis/32_rehearse_scoring.py` | `9cfed5c617185e5a1c36ed08b7f1747275ef655b50a3c65ae28a260307ba93d8` |
| `analysis/33_fetch_unread.py` | `05ee39bca78af41e41794da11195072cf29d3d4d254b8f3d2d1a357baf8635c6` |
| `analysis/out/forecast/forecast_manifest.json` | `d2ccadba5feef0deb8de36e83111ea0dc634b22c890ae38aca31ceb1bb7903a5` |
| `analysis/out/forecast/lageos1_forecast_answer.json` | `7ceac42b1c77faf14e80a3e12478a6242c31dfc5155ea2a8ac8664f1ace88b6e` |
| `analysis/out/forecast/lageos2_forecast_answer.json` | `9325c87cf9e3d7d240359816054ab96e35a5c33a614bb234c8282461bee9c436` |
| `analysis/out/forecast/lageos1_forecast_positions.csv` | `e41fbd6aad2703ae1bbe8644cf72a0340b071191617e9460b41a091122df90fd` |
| `analysis/out/forecast/lageos2_forecast_positions.csv` | `57647739e1053c648d9d8d9ea772340ed455cbc7031f386dc232bc9508a42fd3` |
| `analysis/out/hindcast.json` | `24e1167a7400fb780abca279a4a2b63d717c036bda53f5b306e30cd7dd7aaf48` |
| `raw/edc_start_week_261003/lageos1/gfz.orb.lageos1.261003.v80.sp3.gz` | `66f171d347d0de7316ab29815fca287689b79a5ed16082a6a1ae9907a534a3db` |
| `raw/edc_start_week_261003/lageos2/gfz.orb.lageos2.261003.v80.sp3.gz` | `584768128f770fde70befe98ccc8ff9b57ffc3f012393c46e59aa0817bf577af` |
| `raw/iers/finals2000A.daily` | `3a90113339dc3dd726867d9541d4a8468535b7e1ec9d3966d6c01166a81b6d89` |
| `raw/iers/Leap_Second.dat` | `6cb6f5d4b819f2e568e25db4b0b26d89dedf031fdffb18bc94d40f4e94e268d7` |
| `../analysis/earth_orientation.py`, `subdaily_earth_rotation.py`, `common.py` (unchanged) | `acf21ea8…f3334`, `34896f18…a9815`, `439db804…49cca` |
