# dalys.py
# Practical 10 — Working with Global Health Data
# Analyse the DALYs dataset from Our World in Data.

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# set working directory to wherever this script lives so we can find the csv
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

print("current directory:", os.getcwd())
print("files here:", os.listdir())

# ---- import the dataset ----
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ---- have a quick look at the dataframe ----
print("\n--- first 5 rows ---")
print(dalys_data.head(5))

print("\n--- info ---")
dalys_data.info()

print("\n--- describe ---")
print(dalys_data.describe())


# ---- task 1: show the third and fourth columns (Year, DALYs) for the first 10 rows ----
# The first 10 rows of data are all Afghanistan entries (one per year from 1990–1999).
# Across these first 10 years, 1998 reported the maximum DALYs value for Afghanistan.
print("\n--- Year and DALYs for first 10 rows ---")
print(dalys_data.iloc[0:10, [2, 3]])


# ---- task 2: use a Boolean to show all years for which DALYs were recorded in Zimbabwe ----
zimbabwe_mask = dalys_data["Entity"] == "Zimbabwe"
zimbabwe_years = dalys_data.loc[zimbabwe_mask, "Year"]
# Zimbabwe data spans from 1990 to 2019.
print("\n--- Zimbabwe years ---")
print(zimbabwe_years.values)
print(f"first year: {zimbabwe_years.iloc[0]}, last year: {zimbabwe_years.iloc[-1]}")


# ---- task 3: countries with the maximum and minimum DALYs in 2019 ----
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_idx = recent_data["DALYs"].idxmax()
min_idx = recent_data["DALYs"].idxmin()
country_max = recent_data.loc[max_idx, "Entity"]
country_min = recent_data.loc[min_idx, "Entity"]

# In 2019, Lesotho had the highest DALYs and Singapore had the lowest.
print(f"\nmax DALYs in 2019: {country_max} ({recent_data.loc[max_idx, 'DALYs']:.2f})")
print(f"min DALYs in 2019: {country_min} ({recent_data.loc[min_idx, 'DALYs']:.2f})")


# ---- task 4: plot DALYs over time for one of the two countries above (Lesotho) ----
lesotho = dalys_data.loc[dalys_data.Entity == country_max]

plt.figure(figsize=(10, 6))
plt.plot(lesotho["Year"], lesotho["DALYs"], "b+")
plt.xticks(lesotho["Year"], rotation=-90)
plt.title(f"DALYs over Time — {country_max}", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs per 100,000 people", fontsize=12)
plt.grid(ls="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "dalys_plot.png"), dpi=150,
            bbox_inches="tight")
print("\nsaved: dalys_plot.png")
plt.close()


# ---- task 5: answer our own question ----
# Question: How has the relationship between DALYs in China and the UK changed over time?
# Are they becoming more similar or less similar?
#
# We extract both countries' data, plot them together on the same figure,
# and compute the absolute gap between their DALYs values each year.

china = dalys_data.loc[dalys_data.Entity == "China"].sort_values("Year").reset_index(drop=True)
uk    = dalys_data.loc[dalys_data.Entity == "United Kingdom"].sort_values("Year").reset_index(drop=True)

plt.figure(figsize=(11, 6))
plt.plot(china["Year"], china["DALYs"], "r-o", ms=4, lw=1.5, label="China")
plt.plot(uk["Year"],    uk["DALYs"],    "g-s", ms=4, lw=1.5, label="United Kingdom")
plt.title("China vs UK: DALYs Over Time (1990–2019)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs per 100,000 people", fontsize=12)
plt.legend(fontsize=11)
plt.grid(ls="--", alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "china_uk_comparison.png"), dpi=150,
            bbox_inches="tight")
print("saved: china_uk_comparison.png")
plt.close()

# compute the absolute gap each year
gap = abs(china["DALYs"] - uk["DALYs"])
print(f"\nChina-UK DALYs gap in 1990: {gap.iloc[0]:.2f}")
print(f"China-UK DALYs gap in 2019: {gap.iloc[-1]:.2f}")

print("\ndone.")
