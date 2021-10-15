# Ask the user to input 2 numbers
print("Please enter the first number")
first_number = int(input())
print("Please enter the second number")
second_number = int(input())
# Compare the 2 numbers to decide which is bigger and print the results
if second_number > first_number:
    print("The second number is bigger")
elif first_number > second_number:
    print("The first number is bigger")
else: print("The numbers are equal")

