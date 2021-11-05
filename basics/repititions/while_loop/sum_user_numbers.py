print("How many numbers should I add up?")
numbers_to_sum = int(input())
# Define variables
summed_numbers = 1
total = 0
# Gather inputs from user based on the numbers_to_sum
while summed_numbers <= numbers_to_sum:
    print(f"Please enter number {summed_numbers} of {numbers_to_sum}:")
    number = int(input(""))
    total = total + number
    summed_numbers = summed_numbers + 1
# Display the output
print(f"The total is {total}")
