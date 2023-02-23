import timeit
import numpy as np
import matplotlib.pyplot as plt
from io_handler import read_data


class Simulation:

    def __init__(self, bodies, t=1000, dt=1.0, g=6.67408e-11):
        self.bodies = bodies
        self.t = t
        self.dt = dt
        self.g = g
        self.E = []

    def calc_direct_forces(self):
        for b_i in self.bodies:
            b_i.acc = np.zeros(3)
            b_i.epot = 0
            for b_j in self.bodies:
                if b_j != b_i:
                    r_vec = b_j.pos - b_i.pos
                    r = np.linalg.norm(r_vec)
                    b_i.acc += self.g * b_j.m * r_vec / (r ** 3.0)
                    b_i.epot += np.linalg.norm(b_i.acc) * b_i.m * r

    def run(self, benchmark=True):
        for ti in range(self.t):
            # LEAPFROG
            E = 0
            for b in self.bodies:
                b.pos = b.pos + b.vel * 0.5 * self.dt
            self.calc_direct_forces()
            for b in self.bodies:
                b.vel = b.vel + b.acc * self.dt
                b.pos = b.pos + b.vel * 0.5 * self.dt
                b.ekin = 0.5 * b.m * np.linalg.norm(b.vel) ** 2
                E += b.ekin + b.epot
            if not benchmark:
                self.E.append(E)


if __name__ == '__main__':
    bodies = read_data()
    Sim = Simulation(bodies, t=100, dt=24 * 60 * 60)
    Sim.run(benchmark=False)
    result = np.array(timeit.repeat(Sim.run, number=1, repeat=10))
    print(f"This took {result.mean():.2f} +/- {result.std():.2f} seconds")
    E = np.array(Sim.E)
    dE = np.diff(E)
    plt.plot(range(Sim.t)[1:], dE/E[1:])
    plt.xlabel("timestep [-]")
    plt.ylabel(r"d$E/E$")
    plt.show()