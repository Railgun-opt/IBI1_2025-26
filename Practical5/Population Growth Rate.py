import matplotlib.pyplot as plt

# population data
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]

# calculate percentage change for each country
percent_changes = []
for i in range(len(countries)):
    change = (pop_2024[i] - pop_2020[i]) / pop_2020[i] * 100  # (new - old) / old * 100
    percent_changes.append(change)
    print(f"{countries[i]}: {change:.2f}%")

# sort from largest increase to largest decrease
paired = list(zip(countries, percent_changes))
paired.sort(key=lambda x: x[1], reverse=True)

print("\n population changes in descending order:")
for country, change in paired:
    print(f"{country}: {change:.2f}%")

# pick out the extremes
largest_increase = paired[0]
largest_decrease = paired[-1]
print(f"\n largest increase: {largest_increase[0]} ({largest_increase[1]:.2f}%)")
print(f"largest decrease: {largest_decrease[0]} ({largest_decrease[1]:.2f}%)")

# bar chart - green for increase, red for decrease
sorted_countries = [p[0] for p in paired]
sorted_changes = [p[1] for p in paired]
colors = ['green' if c > 0 else 'red' for c in sorted_changes]

plt.figure(figsize=(8, 5))
plt.bar(sorted_countries, sorted_changes, color=colors)
plt.xlabel('Country')
plt.ylabel('Population Change (%)')
plt.title('Population Change (2020-2024)')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.tight_layout()
plt.savefig('population_change.png')
plt.show()
