# SIR_vaccination.py
# Extends the basic SIR model to include a vaccinated group (V).
# Runs the simulation for different vaccination rates and plots
# the infected count over time for each rate on one figure,
# so we can see where herd immunity kicks in.

import os
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# shared parameters
N = 10000
initial_infected = 1
beta = 0.3
gamma = 0.05
time_steps = 1000

# try vaccination from 0% to 100% in steps of 10%
vaccination_rates = [i / 10 for i in range(11)]

plt.figure(figsize=(6, 4), dpi=150)

for idx, vac_rate in enumerate(vaccination_rates):

    # set up initial counts for this vaccination level
    V = int(N * vac_rate)                # people who are vaccinated (immune)
    S = N - V - initial_infected         # remaining susceptible
    I = initial_infected
    R = 0

    I_list = []                          # only need to track I for this plot

    # same time loop as the basic SIR model
    for t in range(time_steps):
        I_list.append(I)

        if S > 0 and I > 0:
            infection_prob = beta * (I / N)
            new_infections = np.sum(
                np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
            )
        else:
            new_infections = 0

        if I > 0:
            new_recoveries = np.sum(
                np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
            )
        else:
            new_recoveries = 0

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        S = max(S, 0)
        I = max(I, 0)

    # plot infected curve for this vaccination rate
    plt.plot(I_list, label=f'{int(vac_rate * 100)}% vaccinated',
             color=cm.viridis(idx / len(vaccination_rates)))

plt.xlabel('Time step')
plt.ylabel('Number of infected people')
plt.title('SIR Model: Effect of Vaccination')
plt.legend(fontsize=8)
plt.savefig(os.path.join(SCRIPT_DIR, 'SIR_vaccination_result.png'))
print("Saved SIR_vaccination_result.png")
