# spatial_SIR.py
# 2D spatial SIR model on a 100x100 grid.
# Each cell is a person: 0 = susceptible, 1 = infected, 2 = recovered.
# Infection spreads to the 8 neighbouring cells with probability beta.
# Infected individuals recover (become 2) with probability gamma.

import os
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# (no fixed seed — each run will be different, which is the point of a stochastic model)

# set up a 100x100 grid, everyone starts susceptible (0)
population = np.zeros((100, 100))

# pick one random cell as patient zero
outbreak = np.random.choice(range(100), size=2)
population[outbreak[0], outbreak[1]] = 1

beta = 0.3     # infection probability per neighbour contact
gamma = 0.05   # recovery probability per time step

# pseudocode for the time loop:
# for each of 100 time steps:
#   1. find all cells currently in state 1 (infected)
#   2. if no infected cells remain, stop early
#   3. for each infected cell:
#        for each of its 8 neighbours (within grid bounds):
#          if the neighbour is susceptible (state 0):
#            infect it with probability beta -> write to new_population
#   4. for each infected cell:
#        recover it (set state to 2) with probability gamma -> write to new_population
#   5. replace population with new_population
#   6. save a heatmap image every 10 steps

print(f"Outbreak starts at grid position ({outbreak[0]}, {outbreak[1]})")
print("Running spatial SIR simulation...")

frames_saved = 0

# run for 100 time steps
for t in range(100):

    # find every cell where someone is currently infected
    infectedIndex = np.where(population == 1)

    # if nobody is infected anymore, stop early
    if len(infectedIndex[0]) == 0:
        print(f"  Disease died out at step {t}")
        break

    # work on a copy so we don't infect-and-spread in the same step
    new_population = population.copy()

    # each infected person tries to infect their 8 neighbours
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]

        # loop over the 3x3 neighbourhood centred on (x, y)
        for xNeighbour in range(x - 1, x + 2):
            for yNeighbour in range(y - 1, y + 2):
                # skip the cell itself
                if (xNeighbour, yNeighbour) != (x, y):
                    # stay inside the grid boundaries
                    if 0 <= xNeighbour < 100 and 0 <= yNeighbour < 100:
                        # only infect people who are still susceptible
                        if population[xNeighbour, yNeighbour] == 0:
                            new_population[xNeighbour, yNeighbour] = np.random.choice(
                                range(2), p=[1 - beta, beta]
                            )

    # now handle recovery: each infected person recovers with prob gamma
    infectedIndex = np.where(population == 1)   # re-find after infections
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.random() < gamma:
            new_population[x, y] = 2           # mark as recovered

    population = new_population

    # save a frame every 10 steps (and always the last one)
    if t % 10 == 0 or t == 99:
        fname = os.path.join(SCRIPT_DIR, f'spatial_SIR_t{t:03d}.png')
        plt.figure(figsize=(6, 4), dpi=100)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR — Time step {t}')
        plt.colorbar(label='0=Susceptible  1=Infected  2=Recovered')
        plt.savefig(fname)
        plt.close()
        frames_saved += 1

print(f"Done. Saved {frames_saved} frames to {SCRIPT_DIR}")
