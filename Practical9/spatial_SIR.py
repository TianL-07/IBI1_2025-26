# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
# Use 0 for susceptible, 1 for infected, 2 for recovered
population = np. zeros( (100, 100) )

# randomly choose one point in the array as the outbreak point
outbreak = np.random.choice(range(100) ,2)
population[outbreak[0], outbreak[1]] = 1

# store snapshot in specific timepoint
snapshots = {}
snapshots[0] = population.copy()

# use heat map to plot out
plt.figure (figsize =(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')

# Define infection probability and recovery probability
beta=0.3
gamma=0.05
time_steps=100

# FOR each time step from 1 to time_steps:
#     FIND all infected individuals (where population == 1)
#     IF no infected individuals:
#         BREAK out of loop (disease has died out)
#     
#     CREATE empty lists for new_infections and recoveries
#     
#     FOR each infected person at position (i, j):
#         
#         # INFECTION PHASE
#         FOR each neighbour in the 8 surrounding cells (di from -1 to 1, dj from -1 to 1):
#             IF (di, dj) is (0, 0):  # Skip the cell itself
#                 CONTINUE
#             
#             CALCULATE neighbour coordinates (ni, nj) = (i+di, j+dj)
#             
#             IF neighbour is within grid boundaries (0 to 99):
#                 IF neighbour is susceptible (population == 0):
#                     WITH probability beta:
#                         ADD neighbour to new_infections list
#         
#         # RECOVERY PHASE
#         WITH probability gamma:
#             ADD current infected person to recoveries list
#     
#     REMOVE duplicate entries from new_infections (a cell may be infected by multiple sources)
#     
#     # UPDATE PHASE (batch update to avoid interfering with current time step)
#     FOR each position in new_infections:
#         SET population to 1 (infected)
#     FOR each position in recoveries:
#         SET population to 2 (recovered)
#     
#     IF current time step is 10, 50, or 99:
#         STORE a copy of population in snapshots dictionary
# END FOR

for t in range (time_steps):
    infected = np.where(population == 1)
    infected_positions =list(zip(infected[0], infected[1]))
    if len(infected_positions)==0:
        break
    new_infections=[]
    recoveries=[]

    for i,j in infected_positions:
        # infection
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                # calculate the spots of neighbours
                ni, nj = i+di, j+dj
                # check if the neighours out of the zone
                if 0<=ni<100 and 0<=nj<100:
                    if population[ni,nj]==0:
                        if np.random.random() < beta:
                            new_infections.append((ni,nj))
        # recovery
        if np.random.random() < gamma:
            recoveries.append((i,j))

    new_infections = list(set(new_infections))
    
    # update in groups
    # set newly infected people as 1, set newly recovered people as 2
    for pos in new_infections:
        population[pos[0],pos[1]] = 1
    for pos in recoveries:
        population[pos[0],pos[1]] = 2

    if t in [10, 50, 99]:
        snapshots[t] = population.copy()

time_points = [0, 10, 50, 99]
fig, axes = plt.subplots(2, 2, figsize=(10, 10), dpi=150)

for idx, t in enumerate(time_points):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]
    
    if t in snapshots:
        im = ax.imshow(snapshots[t], cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        ax.set_title(f'Time step: {t}')
        ax.axis('off')
    else:
        ax.text(0.5, 0.5, f'Time step {t} not available', 
                ha='center', va='center', transform=ax.transAxes)
        ax.axis('off')

plt.tight_layout()   
plt.show() 