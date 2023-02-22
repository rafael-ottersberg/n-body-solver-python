import csv

import numpy as np

from body import Body


def read_data(filename="solar_jfc.dat"):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        bodies = []
        au = 1.5e11
        m_sol = 2e30
        day = 24.0 * 60.0 * 60.0
        for i, row in enumerate(reader):
            if i > 0:
                pos = np.array(row[2:5], dtype=np.float64) * au
                vel = np.array(row[5:8], dtype=np.float64) * au / day
                acc = np.zeros(3)
                b = Body(float(row[1]) * m_sol, pos, vel, acc)
                bodies.append(b)
    return bodies
