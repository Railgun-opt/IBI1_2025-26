"""
Practical 10 — Working with Global Health Data
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


#   set working directory so Python can find the csv
os.chdir("/Volumes/MOVESPEED/IBI/Week 10 Public health informatics")

#   load the data  
df = pd.read_csv("dalys-rate-from-all-causes.csv")
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

#   quick look at what we've got  
print("--- preview ---")
print(df.head(10))
print(f"\ncountries/entities : {df['Entity'].nunique()}")
print(f"year range        : {df['Year'].min()} – {df['Year'].max()}")
print(f"DALYs range      : {df['DALYs'].min():.0f} – {df['DALYs'].max():.0f}")
print(f"missing values   : {df.isnull().sum().sum()}")


#   pick one country and plot its trend over time  
country = "China"
cdata = df[df["Entity"] == country].sort_values("Year")

plt.figure(figsize=(10, 6))
plt.plot(cdata["Year"], cdata["DALYs"], marker="o", ms=4, lw=1.5,
         color="#2196F3", label=country)
plt.title(f"DALYs Rate: {country} (1990–2019)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs per 100,000 people", fontsize=12)
plt.grid(ls="--", alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig("china_dalys_trend.png", dpi=150, bbox_inches="tight")
print("\nsaved: china_dalys_trend.png")
plt.show()
plt.close()


#   compare several countries on one plot  
countries = ["China", "United States", "Japan", "Brazil", "Nigeria"]
colors   = ["#E53935", "#1E88E5", "#43A047", "#FB8C00", "#8E24AA"]

plt.figure(figsize=(12, 7))
for i, nation in enumerate(countries):
    sub = df[df["Entity"] == nation].sort_values("Year")
    plt.plot(sub["Year"], sub["DALYs"], marker="o", ms=3, lw=2,
             color=colors[i], label=nation)

plt.title("DALYs Rate Comparison (1990–2019)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("DALYs per 100,000 people", fontsize=12)
plt.grid(ls="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig("multi_country_dalys_comparison.png", dpi=150, bbox_inches="tight")
print("saved: multi_country_dalys_comparison.png")
plt.show()
plt.close()


#   rankings for the most recent year  
latest_year = df["Year"].max()
recent = df[df["Year"] == latest_year]

print(f"\n--- top 10 highest DALYs ({latest_year}) ---")
print(recent.nlargest(10, "DALYs")[["Entity", "DALYs"]].to_string(index=False))

print(f"\n--- top 10 lowest DALYs ({latest_year}) ---")
print(recent.nsmallest(10, "DALYs")[["Entity", "DALYs"]].to_string(index=False))


#   per-country stats: average, first year, last year, % change  
rows = []
for entity in df["Entity"].unique():
    ed = df[df["Entity"] == entity].sort_values("Year")
    first_val = ed["DALYs"].iloc[0]
    last_val  = ed["DALYs"].iloc[-1]
    if first_val > 0:                       # avoid division by zero
        pct_change = (last_val - first_val) / first_val * 100
    else:
        pct_change = 0
    rows.append({
        "Entity":   entity,
        "Avg":      round(ed["DALYs"].mean(), 2),
        "First":    round(first_val, 2),
        "Last":     round(last_val, 2),
        "Change%":  round(pct_change, 2)
    })

stats = pd.DataFrame(rows)

print("\n--- most improved (biggest drop) ---")
print(stats.nsmallest(15, "Change%").to_string(index=False))

print("\n--- most worsened (biggest rise) ---")
print(stats.nlargest(15, "Change%").to_string(index=False))


#   global mean trend over time  
yearly_mean = df.groupby("Year")["DALYs"].mean()

plt.figure(figsize=(10, 6))
plt.plot(yearly_mean.index, yearly_mean.values, marker="o", lw=2,
         color="#E91E63", label="Global mean")
plt.title("Global Mean DALYs (1990–2019)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Mean DALYs per 100,000", fontsize=12)
plt.grid(ls="--", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig("global_mean_dalys_trend.png", dpi=150, bbox_inches="tight")
print("\nsaved: global_mean_dalys_trend.png")
plt.show()
plt.close()


#   scatter: 1990 vs 2019, each point = one country  
plt.figure(figsize=(10, 8))
sc = plt.scatter(stats["First"], stats["Last"],
                 c=stats["Change%"], cmap="RdYlGn_r", alpha=0.6, s=35)
mx = max(stats["First"].max(), stats["Last"].max())
plt.plot([0, mx], [0, mx], "k--", alpha=0.4, label="no change")
plt.title("DALYs: 1990 vs 2019 per Country", fontsize=14, fontweight="bold")
plt.xlabel("DALYs in 1990", fontsize=12)
plt.ylabel("DALYs in 2019", fontsize=12)
plt.colorbar(sc, label="Change %")
plt.legend()
plt.grid(ls=":", alpha=0.4)
plt.tight_layout()
plt.savefig("dalys_scatter_1990_vs_2019.png", dpi=150, bbox_inches="tight")
print("saved: dalys_scatter_1990_vs_2019.png")
plt.show()
plt.close()

#   write stats table to csv  
stats.to_csv("country_dalys_statistics.csv", index=False)
print("saved: country_dalys_statistics.csv")
print("\ndone — 4 plots + 1 csv generated.")