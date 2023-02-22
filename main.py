import timeit
import numpy as np

from io_handler import read_data


class Simulation:

    def __init__(self, bodies, t=1000, dt=1.0, g=6.67408e-11):
        self.bodies = bodies
        self.t = t
        self.dt = dt
        self.g = g

    def calc_direct_forces(self):
        for b_i in self.bodies:
            b_i.acc = np.zeros(3)
            for b_j in self.bodies:
                if b_j != b_i:
                    r_vec = b_j.pos - b_i.pos
                    r = np.linalg.norm(r_vec)
                    b_i.acc += self.g * b_j.m * r_vec / (r ** 3.0)

    def run(self):
        for ti in range(self.t):
            # LEAPFROG
            for b in self.bodies:
                b.pos = b.pos + b.vel * 0.5 * self.dt
            self.calc_direct_forces()
            for b in self.bodies:
                b.vel = b.vel + b.acc * self.dt
                b.pos = b.pos + b.vel * 0.5 * self.dt


if __name__ == '__main__':
    bodies = read_data()
    Sim = Simulation(bodies, t=100, dt=24 * 60 * 60)
    result = np.array(timeit.repeat(Sim.run, number=1, repeat=10))
    print(f"This took {result.mean():.2f} +/- {result.std():.2f} seconds")
