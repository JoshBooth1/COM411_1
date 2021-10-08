# Find out more information about the user
print("What is your name human?")
name = input()
print("How old are you in years?")
user_age = int(input())
print("How tall are you in metres?")
user_height = float(input())
print("How much do you weigh in kilograms")
user_weight = int(input())
# confirm the information back to the user and calculate the bmi
print(f"{name} you are {user_age} and your bmi is {user_weight/user_height**2}")







