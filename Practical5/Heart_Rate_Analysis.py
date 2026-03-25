import matplotlib.pyplot as plt

# the dataset
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
average_heart_rate = sum(heart_rates) / len(heart_rates)

print("Heart Rates:", heart_rates)
print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")

# classify into groups
high_group = []
low_group = []
medium_group = []

for i in range(len(heart_rates)):
    if heart_rates[i] > 120:
        high_group.append(heart_rates[i])
        print(f"Heart rate {heart_rates[i]} is high.")

    elif heart_rates[i] < 60:
        low_group.append(heart_rates[i])
        print(f"Heart rate {heart_rates[i]} is low.")

    else:
        medium_group.append(heart_rates[i])  # normal range 60-120
        print(f"Heart rate {heart_rates[i]} is within the normal range.")

high_number = len(high_group)
low_number = len(low_group)
medium_number = len(medium_group)

# find the category with most patients
category = {"High": high_number, "Low": low_number, "Normal": medium_number}
max_group = max(category, key=category.get)
max_group_number = category[max_group]

print(f"\nThe average heart rate is: {average_heart_rate:.2f} bpm.")
print(f"The category with the most heart rates is: {max_group} with {max_group_number} heart rates.")

# pie chart
plt.figure(figsize=(8, 8))
plt.pie(category.values(), labels=category.keys(), autopct='%1.1f%%', explode=(0.05, 0.05, 0.05))
plt.title("Distribution of Heart Rate Categories")
plt.show()
