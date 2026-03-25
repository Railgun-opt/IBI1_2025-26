# 1. set total population to 91
# 2. starting infected students e.g. 5
# 3. daily growth rate e.g. 0.4
# 4. day counter starts at 1
# 5. print day 1 infected count
# 6. loop while infected < total population
# 7. infected = infected * (1 + growth_rate)
# 8. day += 1
# 9. print day and infected count
# 10. when loop ends, print total days

total_population = 91
infected = 5
growth_rate = 0.40  # 40% per day
day = 1

# print starting number
print(f"Day {day}: {infected} students infected.")

# keep going until everyone is infected
while infected < total_population:
    infected = round(infected * (1 + growth_rate))  # new infected = old * (1 + rate)
    day += 1
    print(f"Day {day}: {infected} students infected.")

# done
print(f"\nAll {total_population} students were infected in {day} days.")
