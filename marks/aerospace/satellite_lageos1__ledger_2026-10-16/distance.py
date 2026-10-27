#!/usr/bin/env python3
"""The forecast's distance from the published orbit, from two files alone.

    python3 distance.py forecast/lageos1_forecast_positions.csv ilrsa.orb.lageos1.261010.v80.sp3.gz

The first file is the forecast: every 120 s epoch of the sealed run, turned
into the Earth-fixed frame (columns itrf_x_m, itrf_y_m, itrf_z_m). The second
is the ILRS combined orbit of week 261010 (SP3, positions in km in the same
frame). For each horizon it prints the largest 3-D distance over every epoch
up to it, and how many epochs were scored. Python 3, nothing else.
"""
import csv
import gzip
import math
import sys

HORIZONS_S = [("one revolution", 13560.0, "1 m"), ("one day", 86400.0, "10 m"),
              ("three days", 259200.0, "reported only"), ("seven days", 604680.0, "100 m")]


def read_sp3(path):
    """{'YYYY-MM-DDTHH:MM:SSZ': (x, y, z) in metres}"""
    opener = gzip.open if path.endswith(".gz") else open
    positions, epoch = {}, None
    with opener(path, "rt") as f:
        for line in f:
            if line.startswith("*"):
                y, mo, d, h, mi, s = line[1:].split()[:6]
                epoch = "%s-%02d-%02dT%02d:%02d:%02dZ" % (y, int(mo), int(d), int(h), int(mi), int(float(s)))
            elif line.startswith("P") and epoch:
                positions[epoch] = tuple(float(v) * 1000.0 for v in line[4:].split()[:3])
    return positions


def main(forecast_csv, sp3_path):
    reference = read_sp3(sp3_path)
    rows = list(csv.DictReader(open(forecast_csv)))
    for name, horizon, target in HORIZONS_S:
        largest, scored = 0.0, 0
        for r in rows:
            if float(r["t_s"]) > horizon:
                break
            if r["utc"] in reference:
                ours = (float(r["itrf_x_m"]), float(r["itrf_y_m"]), float(r["itrf_z_m"]))
                largest = max(largest, math.dist(ours, reference[r["utc"]]))
                scored += 1
        print("%-15s %8.3f m over %4d epochs (target %s)" % (name, largest, scored, target))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
