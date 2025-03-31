#Step1 - Get user input for name and monthly income
name = input("Enter your name: ")
monthly_income = float(input("Enter your monthly income: "))

#Step2 - Get user input for monthly expenses
rent = float(input("Enter your monthly rent: "))
utilities = float(input("Enter your monthly utilities: "))
groceries = float(input("Enter your monthly groceries: "))
other_expenses = float(input("Enter other expenses: "))

#Step3 - Calculate monthly savings
total_expenses = rent + utilities + groceries + other_expenses
savings = monthly_income - total_expenses

# print(f"Monthly savings: ${round(savings, 2)}")

#Step 4 - Age Input
age = int(input("Enter your age: "))

#Step 5 - Approx Year Born
year_born_estimate = 2024 - age

#Step 6 - Distance Walked/Ran and Time
distance = float(input("Enter the distance you walk/run in km: "))
time = float(input("Enter how long this takes in min: "))

#Step 7 - Average Speed km/h
time = time / 60
speedkmPh = round(distance/time, 2)

#Step8 - Average Speed m/s
speedmPs = round((speedkmPh * (5/18)), 2)

print(f"Hello, ${name}! You were born in {year_born_estimate}.")
print(f"Your monthly savings are: ${round(savings, 2)}.")
print(f"Your average speed is: {speedkmPh} km/h ({speedmPs} m/s).")