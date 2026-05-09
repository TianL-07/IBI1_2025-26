# import necessary library
import numpy as np
import matplotlib.pyplot as plt
# The total number of people
N=10000
# Define Infected, Susceptible people
I=1
S=N-I
R=0
# Define infection probability and recovery probability
beta=0.3
gamma=0.05
S_history=[S]
I_history=[I]
R_history=[R]
time=0
time_history=[time]
"""
for each time step (1 to 1000):
    p_infect = beta * I / N
    p_recover = gamma

    new_I = count of random choices (0 or 1) for S individuals with probability p_infect
    new_R = count of random choices (0 or 1) for I individuals with probability gamma

    I = I + new_I - new_R
    S = S - new_I
    R = R + new_R

    append S, I, R to history lists
"""
for i in range(1000):
    time+=1
    p_Infected=beta*I/N
    p_Recovered=gamma

    new_I_list=np.random.choice(range(2), S, p=[1-p_Infected,p_Infected])
    new_I=np.sum(new_I_list)
    new_R_list=np.random.choice(range(2), I, p=[1-gamma,gamma])
    new_R=np.sum(new_R_list)

    I=I+new_I-new_R
    S = S - new_I
    R = R + new_R

    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
    time_history.append(time)

# generate plots and label each axis
plt.figure(figsize=(6,4),dpi=150)
plt.plot(time_history, S_history, label='Susceptible')
plt.plot(time_history, I_history, label='Infected')
plt.plot(time_history, R_history, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
plt.savefig("SIR_model.pdf")
plt.show()
