import pandas as pd
import numpy as np
import csv

def read_data(filename="solar_jfc.dat"):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        bodies = []
        au = 1.5e11
        m_sol = 2e30
        day = 24.0 * 60.0 * 60.0
        masses = []
        pos_x = []
        pos_y = []
        pos_z = []
        vel_x = []
        vel_y = []
        vel_z = []
        for i, row in enumerate(reader):
            if i > 0:
                pos_x.append(np.float64(row[2]) * au)
                pos_y.append(np.float64(row[3]) * au)
                pos_z.append(np.float64(row[4]) * au)
                vel_x.append(np.float64(row[5]) * au / day)
                vel_y.append(np.float64(row[6]) * au / day)
                vel_z.append(np.float64(row[7]) * au / day)
                masses.append(np.float64(row[1]) * m_sol)
    return masses, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z