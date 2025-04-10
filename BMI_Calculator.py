# If running in a sandbox, replace the input() function to simulate input.
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
except OSError:
    # Fallback to predefined values if input() is not supported
    weight = 70.0  # Example weight in kg
    height = 1.75  # Example height in meters

BMI = weight / (height ** 2)

print("Your BMI is:", BMI)

if BMI < 16:
    print("You are severely underweight")
elif 16 <= BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI < 24:
    print("You are healthy")
elif 25 <= BMI < 30:
    print("You are overweight")
else:
    print("You are obese")