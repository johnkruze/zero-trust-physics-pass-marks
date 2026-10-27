#!/usr/bin/env python3
"""Ablation Workshop Test Case 1: the solver at the open address against FIAT.

    python3 fiat_compare.py

Asks the open address for the solver's worked example (`example_solve`: TACOT
3.0, 5 cm, the face held at 1,644 K for 60 s) with the thermocouple histories
on, reads NASA's FIAT temperatures for the same case from the engine's public
source at tag v0.15.2 (the table FIAT_TEMPERATURE, transcribed from PATO 3.1,
tutorials/1D/AblationTestCase_1.0/data/ref/FIAT/T), and prints the difference
at every depth and second. Python 3, nothing else.
"""
import json
import re
import urllib.request

ADDRESS = "https://mcp.zerotrustphysics.com/mcp"
SOURCE = ("https://raw.githubusercontent.com/johnkruze/zero-trust-physics-engine/"
          "v0.15.2/genesis_solvers/src/ablator_slab.rs")
DEPTHS_MM = [1, 2, 4, 8, 16, 50]


def call(name, arguments):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": name, "arguments": arguments}}).encode()
    request = urllib.request.Request(ADDRESS, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
        "User-Agent": "zero-trust-physics-replay/1.0"})
    result = json.load(urllib.request.urlopen(request, timeout=120))["result"]
    text = result["content"][0]["text"]
    if result.get("isError"):
        raise SystemExit(text)
    return json.loads(text)


def fiat_table():
    """61 rows: time (s), face, then 1, 2, 4, 8, 16 and 50 mm (K)."""
    source = urllib.request.urlopen(SOURCE, timeout=120).read().decode()
    head = "const FIAT_TEMPERATURE: [[f64; 8]; 61] = ["
    start = source.index(head) + len(head)
    block = source[start:source.index("\n    ];", start)]
    numbers = [float(x) for x in re.findall(r"-?\d+(?:\.\d+)?", block)]
    return [numbers[i:i + 8] for i in range(0, len(numbers), 8)]


def main():
    example = call("describe_solver", {"solver": "ablator_slab"})["example_solve"]
    example["parameters"]["return_thermocouple_histories"] = True
    answer = call("solve", example)
    times = answer["result"]["thermocouple_time_s"]
    temperatures = answer["result"]["thermocouple_temperature_k"]
    fiat = fiat_table()

    squares, worst = [], (0.0, 0.0, 0)
    for row in fiat[1:]:
        for slot in range(5):  # 1 to 16 mm; 50 mm barely moves and is left out, as in the test
            ours = temperatures[slot][times[slot].index(row[0])]
            pct = 100.0 * (ours - row[2 + slot]) / row[2 + slot]
            squares.append(pct * pct)
            if abs(pct) > abs(worst[0]):
                worst = (pct, row[0], DEPTHS_MM[slot])
    rms = (sum(squares) / len(squares)) ** 0.5
    print("engine %s, outcome %s, solution_seal %s..., signed %s" % (
        answer["engine_version"], answer["outcome"], answer["solution_seal"][:16], "signature" in answer))
    print("1 to 16 mm, every second to 60 s (%d values): root mean square %.3f %%, worst %+.2f %% at %.0f s, %d mm"
          % (len(squares), rms, worst[0], worst[1], worst[2]))
    print("at 60 s:   depth      FIAT      this solver   difference")
    for slot, depth in enumerate(DEPTHS_MM):
        ours = temperatures[slot][times[slot].index(60.0)]
        theirs = fiat[60][2 + slot]
        print("          %3d mm  %8.2f K  %8.2f K   %+6.2f %%" % (depth, theirs, ours, 100.0 * (ours - theirs) / theirs))


if __name__ == "__main__":
    main()
