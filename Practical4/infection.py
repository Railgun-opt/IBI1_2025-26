# 1. Set the total population to 91.
# 2. Initialize the starting number of infected students (e.g., 5).
# 3. Set the daily growth rate (e.g., 0.40 for 40%).
# 4. Initialize a day counter starting at 1.
# 5. Display the initial infected count for day 1.
# 6. Loop WHILE the number of infected students is strictly less than the total population:
# 7. Calculate the new number of infected students (current + current * growth_rate).
# 8. Add 1 to the day counter.
# 9. Display the day number and the current number of infected students.
# 10. Once the loop finishes, print the total number of days it took.

total_population = 91
infected = 5
growth_rate = 0.40
day = 1

print(f"Day {day}: {infected} students infected.")

while infected < total_population:
    infected = round (infected * (1 + growth_rate))
    day += 1
    print(f"Day {day}: {infected} students infected.")

print(f"\nAll {total_population} students were infected in {day} days.")