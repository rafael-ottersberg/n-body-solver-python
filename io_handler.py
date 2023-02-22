import pandas as pd
import numpy as np


def read_data(filename="solar_jfc.dat"):
    df = pd.read_csv(filename, sep=',')

    number_of_bodies = len(df.index)

    pos = np.zeros((number_of_bodies, 3))
    vel = np.zeros((number_of_bodies, 3))

    names = np.asarray(df['name'].values)
    masses = np.asarray(df['m'].values)
    pos[:,0] = np.asarray(df['x'].values)
    pos[:,1] = np.asarray(df['y'].values)
    pos[:,2] = np.asarray(df['z'].values)
    vel[:,0] = np.asarray(df['vx'].values)
    vel[:,1] = np.asarray(df['vy'].values)
    vel[:,2] = np.asarray(df['vz'].values)

    return names, masses, pos, vel

