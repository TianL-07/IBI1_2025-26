# Create 2 dictionary to store the population of each country in the same year
pop2020={'UK':66.7, 'China':1426, 'Italy':59.6, 'Brazil':208.6, 'USA':331.6}
pop2024={'UK':69.2, 'China':1410, 'Italy':58.9, 'Brazil':212.0, 'USA':340.1}
# Calculate percentage changes
# Match the keys in two dictionary
# then calculate the percentage changes separately
percentage_changes=[]
# Country stores the key we're currently working with, like a box
for country in pop2020.keys():
    if country in pop2024.keys():
        pop0=pop2020[country]
        pop4=pop2024[country]
        percent_change = ((pop4 - pop0) / pop0) * 100
        # adding the results to the empty list we created before
        percentage_changes.append((country, percent_change))
        print(country,"population percentage change", percent_change)
# Ordering the values
descending=sorted(percentage_changes, key=lambda x: x[1], reverse=True)
print(descending)
# Identify the country has largest increase and decrease in population by the order the list
print("The country had largest increase in population is", descending[0])
print("The country had largest decrease in population is", descending[4])
import numpy as np
import matplotlib.pyplot as plt
# Create the bar plot
plt.figure(figsize=(10,6))
bars=plt.bar(country, percent_change, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population change (millions)')
plt.title('Population change by cuntry (2020-2024)')
plt.grid(axis='y', alpha=0.3)
plt.show()