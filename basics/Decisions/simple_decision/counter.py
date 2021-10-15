# Ask the user to input 3 numbers

print("Please enter the first number")
first_number = int(input())
print("Please enter the second number")
second_number = int(input())
print("Please enter the third number")
third_number = int(input())

# Create variables for the odd and even calculators

odd_numbers = 0
even_numbers = 0

# Add value to the variables based on the inputs

if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
# Print the values of the counters
print(f"There are {even_numbers} even numbers")
print(f"There are {odd_numbers} odd numbers")


