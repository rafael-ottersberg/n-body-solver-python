import timeit
import numpy as np

from io_handler import read_data


class Simulation:

    def __init__(self, bodies, t=1000, dt=1.0, g=6.67408e-11):
        self.bodies = bodies

        self.t = t
        self.dt = dt
        self.g = g

    @staticmethod
    def calc_direct_forces(pos, masses, g):
        r_vec = pos[:, np.newaxis, :] - pos[np.newaxis, :, :]
        r = np.sum(r_vec**2, axis=2)**0.5

        a = g * masses[:, np.newaxis, np.newaxis] * r_vec / (r**3)[:, :, np.newaxis]

        a_tot = np.sum(a, axis=0)

        return a_tot

    def run(self):
        names, masses, pos, vel = self.bodies
        for ti in range(self.t):
            # LEAPFROG
            pos = pos + vel * 0.5 * self.dt

            a = self.calc_direct_forces(pos, masses, self.g)
            
            vel = vel + a * self.dt
            pos = pos + vel * 0.5 * self.dt


if __name__ == '__main__':
    bodies = read_data()
    Sim = Simulation(bodies)
    result = np.array(timeit.repeat(Sim.run, number=1, repeat=10))
    print(f"This took {result.mean():.2f} +/- {result.std():.2f} seconds")
