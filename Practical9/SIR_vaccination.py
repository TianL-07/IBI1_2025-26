# import necessary library
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.figure(figsize=(6,4),dpi=150)

# Define infection probability and recovery probability
beta=0.3
gamma=0.05

# The total number of people
N=10000
# Define vaccination rates
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
peak_infections=[]

# Simulate with different vaccination rate
# Use enumerate to facilitate the color painting later
for idx, v_rate in enumerate(vaccination_rates):
    Imm=int(N*v_rate)
    I=1
    S=N-I-Imm
    R=0
    
    # S cannot be negative
    if S < 0:
        S=0
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
    # record the peak infected people under this vaccination rate
    peak_infections.append(max(I_history))
    # drawing the curve
    color = cm.viridis(idx / len(vaccination_rates))
    plt.plot(time_history, I_history, color=color, label=f'{int(v_rate*100)}%')

# Adding labels
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR Model with different vaccination rates')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("SIR Model with different vaccination rates.pdf")
plt.show()
