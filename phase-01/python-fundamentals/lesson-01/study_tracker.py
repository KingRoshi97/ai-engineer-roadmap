name = input("What is your name? ")
days_studied = int(input("How many days did you study this week? "))

total_hours = 0

for day in range(1, days_studied + 1):
    hours = float(input(f"Hours studied on day {day}: "))
    total_hours += hours

average_hours = total_hours / days_studied

print()
print(f"{name}, you studied {total_hours} hours this week.")
print(f"Average per study day: {average_hours:.1f} hours")

if total_hours >= 20:
    print("Status: On target")
elif total_hours >= 15:
    print("Status: Close to target")
elif total_hours >= 10:
    print("Status: Below target")
else:
    print("Status: Needs improvement")