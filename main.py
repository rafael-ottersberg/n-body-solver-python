import timeit
import numpy as np

from io_handler import read_data
from numba import jit

@jit(nopython=True)
def calc_direct_forces(pos_x, pos_y, pos_z, masses, g):
    a_x = []
    a_y = []
    a_z = []
    for i in range(len(masses)):
        a_x_i = 0
        a_y_i = 0
        a_z_i = 0
        for j in range(len(masses)):
            r_x = pos_x[j] - pos_x[i]
            r_y = pos_y[j] - pos_y[i]
            r_z = pos_z[j] - pos_z[i]
            r = np.sqrt(r_x ** 2 + r_y ** 2 + r_z ** 2)
            if r != 0:
                a_x_i += g * masses[j] * r_x / (r ** 3.0)
                a_y_i += g * masses[j] * r_y / (r ** 3.0)
                a_z_i += g * masses[j] * r_z / (r ** 3.0)
        a_x.append(a_x_i)
        a_y.append(a_y_i)
        a_z.append(a_z_i)

    return a_x, a_y, a_z

    
@jit(nopython=True)
def run(masses, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, t, dt, g):
    for _ in range(t):
        # LEAPFROG
        for i in range(len(masses)):
            pos_x[i] = pos_x[i] + vel_x[i] * 0.5 * dt
            pos_y[i] = pos_y[i] + vel_y[i] * 0.5 * dt
            pos_z[i] = pos_z[i] + vel_z[i] * 0.5 * dt

        a_x, a_y, a_z = calc_direct_forces(pos_x, pos_y, pos_z, masses, g)
        
        for i in range(len(masses)):
            vel_x[i] = vel_x[i] + a_x[i] * 0.5 * dt
            vel_y[i] = vel_y[i] + a_y[i] * 0.5 * dt
            vel_z[i] = vel_z[i] + a_z[i] * 0.5 * dt

            pos_x[i] = pos_x[i] + vel_x[i] * 0.5 * dt
            pos_y[i] = pos_y[i] + vel_y[i] * 0.5 * dt
            pos_z[i] = pos_z[i] + vel_z[i] * 0.5 * dt




if __name__ == '__main__':
    masses, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z = read_data()
    t=100
    dt=24 * 60 * 60
    g=6.67408e-11
    test = lambda: run(masses, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z, t, dt, g)
    test()
    result = np.array(timeit.repeat(test, number=1, repeat=10))
    print(f"This took {result.mean():.3f} +/- {result.std():.3f} seconds")
