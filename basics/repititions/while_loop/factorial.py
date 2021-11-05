# Ask for users input for the number
print("Please enter a number")
number = int(input())
# Define the variables
count = 0
total = 1

# Calculate the factorial
while count < number:
    count = count + 1
    total = total * count
print("")
print(f"The factorial equals {total}")
