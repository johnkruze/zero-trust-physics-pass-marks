# LAGEOS-1 and LAGEOS-2, 4 to 11 October 2026: the forecast against the published orbits

**34 of 34 gated distances inside their targets.** LAGEOS-1, forecast from one published state of 4 October 2026, 0 h: **0.097 m** after one revolution (target 1 m), **0.274 m** after one day (target 10 m), **3.526 m** after seven days (target 100 m).

The forecast and its targets are fixed by the target beside this folder, `../satellite_lageos1__ledger_2026-10-16.json`, added in commit [`50ceb1d`](https://github.com/johnkruze/zero-trust-physics-pass-marks/commit/50ceb1df95cdd8334e1f642d8a4c731ab39926db), made, dated and signed by GitHub at 2026-10-17 04:04:59 UTC. The orbits it is compared with were published afterwards: the week's first orbit files appear in the EDC listing on 20 October, GFZ's at 19:04 on 20 October and the ILRS combined orbit at 12:07 on 21 October (the listings are in this folder). Scored 2026-10-22, 03:04:11 to 03:04:17 UTC.

## Part A: the forecast run, sealed on 16 October

Largest 3-D distance from the ILRS combined orbit (`ilrsa` v80), over every 120 s epoch up to the horizon.

| | one revolution (target 1 m) | one day (target 10 m) | three days (reported only) | seven days (target 100 m) |
|---|---|---|---|---|
| LAGEOS-1 | **0.097 m** | **0.274 m** | 0.853 m | **3.526 m** |
| LAGEOS-2 | **0.355 m** | **1.348 m** | 4.419 m | **11.148 m** |

Every run reached every horizon, every epoch was scored (113, 720, 2,160 and 5,039 epochs), both forms of `verify_tape` hold, and both card frames recompute bit for bit. Run seals: LAGEOS-1 `9bcfff35…9b72`, LAGEOS-2 `f9905867…87e8` (in full in `score.json`). The forecast stated a seven-day range of 8 to 50 m for LAGEOS-1 and 5 to 35 m for LAGEOS-2; LAGEOS-1 came in under the low end of its range at every horizon, LAGEOS-2 inside its range at every horizon.

## Part B: seven daily starts from GFZ's orbit of the same week

| Start | LAGEOS-1 one revolution / one day / seven days (m) | LAGEOS-2 one revolution / one day / seven days (m) |
|---|---|---|
| day 0 | 0.120 / 0.318 / 4.275 | 0.287 / 0.913 / 7.923 |
| day 1 | 0.103 / 0.698 | 0.116 / 0.479 |
| day 2 | 0.183 / 1.067 | 0.150 / 0.507 |
| day 3 | 0.538 / 2.525 | 0.139 / 0.717 |
| day 4 | 0.376 / 2.102 | 0.313 / 1.446 |
| day 5 | 0.171 / 0.786 | 0.144 / 0.916 |
| day 6 | 0.214 | 0.141 |
| inside the target | 7 of 7, 6 of 6, 1 of 1 | 7 of 7, 6 of 6, 1 of 1 |

Largest LAGEOS-1 distance of any run: 4.275 m at seven days, 23 times inside its 100 m target. The velocity-record test on the GFZ files: largest share 0.0017 (LAGEOS-1) and 0.0044 (LAGEOS-2) against 0.05.

Part A, 6 gated distances; part B, 28. The scoring program's last line, as it printed it (`score_run.log`): `verdict: met | lageos1: pass | lageos2: pass`.

## The data, fingerprinted before opening

Fetched anonymously from the EUROLAS Data Center (DGFI-TUM), ILRS weekly orbit product, doi:10.5067/SLR/SLR_ILRSORB_001, week 261010, SP3 v80. SHA-256 computed while each file streamed to disk; `FINGERPRINTS.txt` written at 2026-10-22 03:04:04 UTC, before any byte was parsed.

| File | Bytes | SHA-256 |
|---|---|---|
| `lageos1/gfz.orb.lageos1.261010.v80.sp3.gz` | 237,333 | `ef5e1f298d5c9932458ae5aa705f6a22dc3c738cb469e1f785f9c9afeaa9d805` |
| `lageos1/ilrsa.orb.lageos1.261010.v80.sp3.gz` | 243,989 | `0c95e694376ac111dc502b71225951c8c4d47b96dfbd0339da60ca3e3d4aad4f` |
| `lageos2/gfz.orb.lageos2.261010.v80.sp3.gz` | 236,799 | `c386f18c51328cc3c2d862314e3180be56907347606ec89eea8c26becf6f0a0f` |
| `lageos2/ilrsa.orb.lageos2.261010.v80.sp3.gz` | 243,882 | `92bfec1a2372cdf16b945e34edf191a5dc572f723849d815b8a2131ff67de103` |

From `ftp://edc.dgfi.tum.de/pub/slr/products/orbits/TRF/<satellite>/2026/261010/<file>`. Anyone can fetch the four files and compare. The backup combination `ilrsb` v80 is not published for this week; it was not needed, because `ilrsa` holds 5,040 epochs from 0 h every 120 s for both satellites.

## One departure from the protocol

The protocol's §7 has three steps that record the forecast's life in a ledger: step 2 (`forecast.py register`), step 3 (`open`) and step 5 (`score`). Each writes and commits a registration to a Git repository of a local build copy of the engine. That copy no longer existed when the data arrived, and **those three steps were not run**. In their place, every file was fingerprinted before it was opened: the fetcher's in-stream SHA-256 log and `FINGERPRINTS.txt`. Those records carry this machine's clock, not GitHub's. What does not rest on this machine's clock: the target and the forecast's protocol hash were public, signed and dated by GitHub on 17 October, and the orbits were published at the EDC on 20 and 21 October.

Unchanged from the protocol: the scoring program, the targets, the reference rule and the engine. Each program's SHA-256 was recomputed at scoring and equals the protocol's: `31_score.py` `4461faad…66fe`, `lageos_ledger.py` `476b1078…50ab`, the fetcher `05ee39bc…35c6`, the forecast manifest `d2ccadba…03a5`, Bulletin A `3a901133…6d89`. The engine is the served 0.12.0 binary the protocol names, SHA-256 `fec124af6940a02d2eb617423f4cb00f8c503ce432be0864a02cc6dd7453d241`. The protocol document's SHA-256, recomputed at scoring, is `92cfb3802f77a398ae9b37c89e64a338aa55d14a368c58dc8ecd5ed1ee34659b`, the hash in the target. The week was fetched and scored into folders other than the ones the protocol names; no program was changed for that.

## In this folder

| File | What it is | SHA-256 |
|---|---|---|
| `RESULT.md` | This page | |
| `score.json` | The scoring program's full output: every distance, every run seal, every input's hash | `5a327dc28e625c3900df40e7f716e7b15d15ad0f8b4e89eab13be0ccda734b06` |
| `score_run.log` | What the scoring program printed, start to exit 0 | `f3bf8b6df7da80b6786b63305aaf7ea54e0d65c152e37b6284b9caa40ed2119e` |
| `FINGERPRINTS.txt` | SHA-256, bytes, fetch time and URL of each data file, written before opening | `5ec2b303ebe14951b280e51bc655c093187e990f18f838a370874a823c6d99f7` |
| `ftp_listing_lageos1_2026-10-22T030334Z.txt`, `ftp_listing_lageos2_2026-10-22T030345Z.txt` | The EDC's listing of the week's folder at fetch, with each file's publication time | `42ec1d95…acf3`, `108495b1…68d9` (in `FINGERPRINTS.txt`) |

Super Intelligence on behalf of Protocol Company, 22 October 2026.
