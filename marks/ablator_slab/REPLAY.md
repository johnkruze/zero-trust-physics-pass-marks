# Replay the heat-shield solver against NASA's codes and the Stardust flight

The solver `ablator_slab` in three calls an agent can run at `https://mcp.zerotrustphysics.com/mcp` (open, no key): once against NASA's code FIAT on the Ablation Workshop's standard case, and twice against the heat shield of the Stardust capsule, recovered after its entry of 15 January 2006. Every number below was reproduced at the open address, engine 0.15.2 (`genesis_solvers_v0.13.0`), on 26 October 2026; each answer is signed ML-DSA-87 and each seal holds at `verify_solution` with `{"request": <the request>, "solution_seal": <the seal>}`.

## 1. Against FIAT: Ablation Workshop Test Case 1

TACOT 3.0, a 5 cm slab from 298 K, the face held at 1,644 K for 60 s. `solve` with:

```json
{"solver": "ablator_slab", "parameters": {"material": "TACOT 3.0", "thickness_m": 0.05, "start_temperature_k": 298.0, "thermocouple_depths_m": [0.001, 0.002, 0.004, 0.008, 0.016, 0.05], "face": "held_temperature", "held_temperature_k": 1644.0, "hold_duration_s": 60.0, "continue_after_s": 0.0, "return_face_history": false, "return_thermocouple_histories": true, "return_final_profile": false}}
```

Solution seal `1dbae1559562ad3fc1076b8ffa4928d7c0f82c1d9c5fde20b983f4204f1d9118cd6fd3823ced143aac0e3b5e8cc4bd00`. It is the solver's worked example (`describe_solver` → `example_solve`) with the thermocouple histories turned on.

NASA's FIAT temperatures for the same case are the table `FIAT_TEMPERATURE` in the engine's public source, [`genesis_solvers/src/ablator_slab.rs` at tag v0.15.2, line 6231](https://github.com/johnkruze/zero-trust-physics-engine/blob/v0.15.2/genesis_solvers/src/ablator_slab.rs#L6231), transcribed from PATO 3.1, `tutorials/1D/AblationTestCase_1.0/data/ref/FIAT/T`. `python3 fiat_compare.py` makes the call, reads that table and prints:

```
1 to 16 mm, every second to 60 s (300 values): root mean square 0.633 %, worst +1.77 % at 1 s, 1 mm
at 60 s:   depth      FIAT      this solver   difference
            1 mm   1528.22 K   1528.21 K    -0.00 %
            2 mm   1420.87 K   1421.35 K    +0.03 %
            4 mm   1227.80 K   1230.30 K    +0.20 %
            8 mm    914.97 K    920.42 K    +0.60 %
           16 mm    551.89 K    556.13 K    +0.77 %
           50 mm    298.39 K    298.32 K    -0.03 %
```

The same comparison is the source's own test, `test_case_1_against_fiat` ([line 6957](https://github.com/johnkruze/zero-trust-physics-engine/blob/v0.15.2/genesis_solvers/src/ablator_slab.rs#L6957)); `test_case_1_from_300_k_against_pato` and `case_2_2_against_pato` hold it against NASA's PATO.

## 2. The Stardust flight

The PICA model of the open record, version 5, at the two places cores were cut from the recovered shield, with NASA's computed heating of the entry. Measured wear: 5.7 mm near the nose (6.1 mm by X-ray scan) and 3.2 mm on the flank.

| | Call | `wear_m` | Solution seal |
|---|---|---|---|
| Near the nose | `solve` with `{"solver": "ablator_slab", "example": "example_solve_stardust_near_nose"}`, the solver's second worked example; the same request in full is `stardust_nose_request.json` | 0.007575342631352342 (7.58 mm) | `83ef5890b76ee046a4be8e7a75d6e79ecb4b62ef8f307746db696e690ac9349caa6ad06a2bcf8c0e9480937f4d764974` |
| Flank | `solve` with `stardust_flank_request.json` | 0.0033219429478248256 (3.32 mm) | `444706bdd7a8311d837d9eaeb8d5b7f3ffd7ccb7ba7d8ed85b5f649b2539fc4edda21f419aa498e4889ca2102231ec06` |

Beside NASA's own computations of the same two cores:

| Wear | Near the nose | Flank |
|---|---|---|
| Measured on the recovered shield | 5.7 mm (6.1 by X-ray) | 3.2 mm |
| This solver | 7.58 mm, a third high | 3.32 mm, 0.12 mm over |
| NASA's uncoupled predictions (Kontinos and Stackpoole, AIAA 2008-1197, as reprinted in Beerman 2011, Table 4.2) | 9.2 mm | 4.0 mm |
| NASA's coupled flow and material computations (Chen and Gokcen 2013, NTRS 20140005552; Johnston 2014, NTRS 20140004052) | 7.0 and 4.9 mm | 2.6 mm |

**What was fixed before the flight was run.** No target was posted for the flight (the target beside this folder says so). The model was fitted on one number, a char conductivity scale, from the thermocouples of four arc-jet blocks; its surface rules were set on 36 arc-jet tests; each version was frozen before it was run on the flight, and nothing in version 5 is set on the flight. That record is the engine's own description (`describe_solver ablator_slab`), not a date kept by GitHub.

**Where it misses.** At the nose it runs a third high. The depth at which the shield is back within 2 percent of untouched material is 12.0 and 14.4 mm against 8.65 and 10.74 mm measured. On the 31 held-back arc-jet tests the hottest face runs 4.1 percent hot on average, against 3.5 allowed. `describe_solver ablator_slab` states each.

**The heating.** The wall pressure, heat-transfer coefficient and flow enthalpy, every second to 133 s, are NASA's computation of the entry with a bare wall: Omidy, Panerai, Martin, Lachaud, Cozmuta and Mansour (2015), *Code-to-Code Comparison, and Material Response Modeling of Stardust and MSL using PATO and FIAT*, NASA/CR-2015-218960, NTRS 20160006963, Appendix D, Table D3 (near the nose) and Table D4 (flank); NTRS: "Public Use Permitted." The radiative heating is read from Johnston (2014), *Study of Aerothermodynamic Modeling Issues Relevant to High-Speed Sample Return Vehicles*, NTRS 20140004052; NTRS: "Work of the US Gov. Public Use Permitted." The stream is off from 134 s and the shield cools to 600 s.

**With the engine's own entry in place of NASA's heating.** The coupling `stardust_entry_to_pica_slab` hands the engine's own computed entry (`capsule_stardust`, nothing fitted) into the same slab under one chain proof: 4.65 mm near the nose, 18 percent low. Those runs and their proofs are the dataset [Atmospheric entry and heat-shield wear](https://huggingface.co/datasets/zero-trust-physics/zero-trust-physics-entry-heatshield).

Super Intelligence on behalf of Protocol Company, 26 October 2026.
