# Ask user for a number
print("Please enter a whole number.")
number = int(input())
# Display message
if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")
# This is because if the number goes in to the 2 with no remainder it is even if not and it has a remainder it must be odd