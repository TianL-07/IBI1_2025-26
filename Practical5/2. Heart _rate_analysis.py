heart_rates=[72, 60, 126, 85, 90,	59,	76,	131, 88, 121, 64]
print("Patients number=",len(heart_rates))
mean= sum(heart_rates)/len(heart_rates)
print("mean=",mean)

Low=0
Normal=0
High=0
for i in range(len(heart_rates)):
    if heart_rates[i] < 60:
        Low+=1
    elif heart_rates[i] > 120:
        High+=1
    else:
        Normal+=1
print("Patients=", Low+High)
Category={"Low":Low, "Normal":Normal, "High":High}
max_category=max(Category, key=Category.get)
print(max_category,Category[max_category])

import numpy as np
import matplotlib.pyplot as plt
labels=list(Category.keys())
sizes=list(Category.values())
plt.pie(sizes, labels=labels,autopct='%.1f%%')
plt.title("Patients' heart rates category")
plt.show()