import numpy as np          
import matplotlib.pyplot as plt

N = 10000 
initial_infected = 1   # 增加初始感染者，避免随机灭绝
S = N - initial_infected 
I = initial_infected 
R = 0 

beta = 0.3 
gamma = 0.05 

S_list = [S] 
I_list = [I] 
R_list = [R] 

for t in range(1000): 
    
    infection_prob = beta * (I / N)
    
    new_infections = np.sum(
        np.random.choice([0, 1], size=S, p=[1-infection_prob, infection_prob])
    )
    
    new_recoveries = np.sum(
        np.random.choice(
            [0, 1],
            size=I,              
            p=[1-gamma, gamma]  
        )
    )
    
    S = S - new_infections       
    I = I + new_infections - new_recoveries 
    R = R + new_recoveries  

    # 记录移到更新之后
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6, 4))

plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='orange') 
plt.plot(R_list, label='Recovered', color='green') 

plt.xlabel('Time')           # x-axis label
plt.ylabel('Number of people')  # y-axis label
plt.title('SIR Model Simulation')  # Figure title
plt.legend()                # Display legend

plt.savefig('SIR_result.png', format='png')  # Save figure
plt.show()