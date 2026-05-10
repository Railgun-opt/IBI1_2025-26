# SIR.py
# Basic stochastic SIR (Susceptible-Infected-Recovered) model.
# Simulates disease spread through a well-mixed population of 10000 people.

import os
import matplotlib
matplotlib.use('Agg')   # non-interactive backend (no display needed)
import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# model parameters
N = 10000              # total population
initial_infected = 1   # start with one sick person
S = N - initial_infected   # everyone else is susceptible
I = initial_infected
R = 0                   # nobody has recovered yet

beta = 0.3              # infection probability upon contact
gamma = 0.05            # recovery probability per time step

# arrays to record how S, I, R change over time
S_list = []
I_list = []
R_list = []

# run the simulation for 1000 time steps
for t in range(1000):

    # record current state
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

    # new infections: each susceptible person gets infected with
    # probability = beta * (fraction of population that is infected)
    if S > 0 and I > 0:
        infection_prob = beta * (I / N)
        new_infections = np.sum(
            np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
        )
    else:
        new_infections = 0

    # new recoveries: each infected person recovers with probability gamma
    if I > 0:
        new_recoveries = np.sum(
            np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
        )
    else:
        new_recoveries = 0

    # update the counts
    S = S - new_infections
    I = I + new_infections - new_recoveries
    R = R + new_recoveries

    # safety: don't let counts go negative
    S = max(S, 0)
    I = max(I, 0)

# plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='orange')
plt.plot(R_list, label='Recovered', color='green')
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
plt.savefig(os.path.join(SCRIPT_DIR, 'SIR_result.png'))
print("Saved SIR_result.png")
