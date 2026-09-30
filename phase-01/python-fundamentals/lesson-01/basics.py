print("=" * 50)
print("AI STUDY PROGRESS CHECKER")
print("=" * 50)

name = input("What is your name? ")

hours_per_day = int(input("How many hours do you study per day? "))
days_per_week = int(input("How many days per week do you study? "))

weekly_hours = hours_per_day * days_per_week

print()
print(f"{name}, you study {weekly_hours} hours per week.")

if weekly_hours >= 20:
    print("Status: On target")
elif weekly_hours >= 15:
    print("Status: Close to target")
elif weekly_hours >= 10:
    print("Status: Below target")
else:
    print("Status: Needs improvement")

print("=" * 50)