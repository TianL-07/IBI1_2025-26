heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 1. Sentence with number of patients and mean heart rate
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients
print(f"Number of patients: {num_patients}, mean heart rate: {mean_hr:.2f} bpm")

# Categorise heart rates
low = 0
normal = 0
high = 0

for rate in heart_rates:
    if rate < 60:
        low += 1
    elif rate > 120:
        high += 1
    else:
        normal += 1

# 2. Print number of patients in each category
print(f"Low (<60 bpm): {low} patients")
print(f"Normal (60–120 bpm): {normal} patients")
print(f"High (>120 bpm): {high} patients")

# Identify largest category
categories = {"Low": low, "Normal": normal, "High": high}
largest = max(categories, key=categories.get)
print(f"The largest category is '{largest}' with {categories[largest]} patients")

# 3. Pie chart
import matplotlib.pyplot as plt

labels = list(categories.keys())
sizes = list(categories.values())
plt.pie(sizes, labels=labels, autopct='%.1f%%')
plt.title("Heart Rate Categories Distribution")
plt.show()