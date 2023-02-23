class Body:
    def __init__(self, m, pos, vel, acc):
        self.m = m
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.epot = 0
        self.ekin = 0
