# Exercise 1 - Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

# Exercise 2 - Temperature Converter
# Convert a temperature from C to F or F to C
t = float(input("Input the temperature: "))
unit = input("Enter the unit to convert to: ").upper()

if unit == "C":
    convertedTemp = (t-32)/1.8
    print(f"The temperature in Celcius is {convertedTemp:.2f}°C")
elif unit == "F":
    convertedTemp = (t*1.8)+32
    print(f"The temperature in Fahrenheit is {convertedTemp:.2f}°F")
else:
    print("Invalid unit!")

# Exercise 3
n = int(input("Enter an integer: "))

if (n >= 1) and (n <= 100):
    if n % 2 == 1:
        print("Weird")
    else:
        if (n >= 2) and (n <= 5):
            print("Not Weird")
        elif (n >= 6) and (n <= 20):
            print("Weird")
        elif (n > 20):
            print("Not Weird")
