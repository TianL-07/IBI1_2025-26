import matplotlib.pyplot as plt

# Population data (millions)
pop2020 = {'UK': 66.7, 'China': 1426, 'Italy': 59.4, 'Brazil': 208.6, 'USA': 331.6}
pop2024 = {'UK': 69.2, 'China': 1410, 'Italy': 58.9, 'Brazil': 212.0, 'USA': 340.1}

# Calculate percentage change for each country
changes = []  # list of (country, percent_change)

for country in pop2020.keys():
    if country in pop2024.keys():
        old = pop2020[country]
        new = pop2024[country]
        pct = ((new - old) / old) * 100
        changes.append((country, pct))
        print(f"{country} population percentage change: {pct:.2f}%")

# Sort descending (largest increase to largest decrease)
sorted_changes = sorted(changes, key=lambda x: x[1], reverse=True)

print("\nSorted in descending order:")
for country, pct in sorted_changes:
    print(f"{country}: {pct:.2f}%")

# Identify largest increase and largest decrease
largest_increase = sorted_changes[0]
largest_decrease = sorted_changes[-1]
print(f"\nCountry with largest increase: {largest_increase[0]} ({largest_increase[1]:.2f}%)")
print(f"Country with largest decrease: {largest_decrease[0]} ({largest_decrease[1]:.2f}%)")

# Bar chart
countries = [item[0] for item in sorted_changes]
percentages = [item[1] for item in sorted_changes]

plt.figure(figsize=(10, 6))
plt.bar(countries, percentages, color='skyblue', edgecolor='navy')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population change (%)', fontsize=12)
plt.title('Population Percentage Change by Country (2020-2024)', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(percentages):
    plt.text(i, v + 0.2, f"{v:.2f}%", ha='center', fontsize=10)

plt.tight_layout()
plt.show()