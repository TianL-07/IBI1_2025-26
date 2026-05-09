# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# The dataset already in this directory so no need to change
# Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Quick inspection 
print(dalys_data.head(5))
dalys_data.info()

# Columns: assume order is Entity (0), Code (1), Year (2), DALYs (3)
first10_yeardalys = dalys_data.iloc[0:10, [2, 3]]
print(first10_yeardalys)

# Find the year of maximum DALYs for Afghanistan among the first 10 rows
afg_data = dalys_data.iloc[0:10]
afg_rows = afg_data[afg_data['Entity'] == 'Afghanistan']
max_year_afg = afg_rows.loc[afg_rows['DALYs'].idxmax(), 'Year']
print(f"\nIn Afghanistan, the maximum DALYs within the first 10 rows occurred in {max_year_afg}.")
# The maximum DALYs recorded in Afghanistan within the first 10 rows occurred in 1998.

# Use Boolean to show all years for which DALYs were recorded in Zimbabwe
zimbabwe_bool = dalys_data['Entity'] == 'Zimbabwe'
zimbabwe_years = dalys_data.loc[zimbabwe_bool, 'Year']
print("\nAll years with DALYs recorded for Zimbabwe:")
print(zimbabwe_years.tolist())
print(f"First recorded year: {zimbabwe_years.min()}, Last recorded year: {zimbabwe_years.max()}")
# The first recorded year for Zimbabwe is 1990, and the last recorded year is 2019.

# Compute countries with maximum and minimum DALYs in 2019.
data_2019 = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']].dropna()
max_row_2019 = data_2019.loc[data_2019['DALYs'].idxmax()]
min_row_2019 = data_2019.loc[data_2019['DALYs'].idxmin()]
print(f"\nIn 2019, country with MAXIMUM DALYs: {max_row_2019['Entity']} ({max_row_2019['DALYs']})")
print(f"In 2019, country with MINIMUM DALYs: {min_row_2019['Entity']} ({min_row_2019['DALYs']})")
# The country with the maximum DALYs in 2019 is Lesotho.
# The country with the minimum DALYs in 2019 is Singapore.

# Create a plot showing DALYs over time for Lesotho
extreme_country = max_row_2019['Entity']   
ctry_data = dalys_data.loc[dalys_data['Entity'] == extreme_country, ['Year', 'DALYs']].dropna()
plt.figure(figsize=(10,5))
plt.plot(ctry_data['Year'], ctry_data['DALYs'], 'r-o', markersize=4)
plt.title(f'DALYs over time: {extreme_country}')
plt.xlabel('Year')
plt.ylabel('DALYs (per 100,000 people)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Additional question: Distribution of DALYs across all countries in 2019
dalys_2019 = dalys_data.loc[dalys_data['Year'] == 2019, 'DALYs'].dropna()
plt.figure(figsize=(8,5))
plt.hist(dalys_2019, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
plt.title('Distribution of DALYs across all countries in 2019')
plt.xlabel('DALYs (per 100,000)')
plt.ylabel('Number of countries')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
print(f"Mean DALYs: {dalys_2019.mean():.2f}")
print(f"Median DALYs: {dalys_2019.median():.2f}")
print(f"Std deviation: {dalys_2019.std():.2f}")
print(f"Range: {dalys_2019.min():.2f} – {dalys_2019.max():.2f}")