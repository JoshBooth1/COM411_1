print("Calculating the sum of the first 100 numbers")
# Define the starting points
number = 1
total = 0
# Add the previous number to the current number whilst the number is less than or equal to 100
while number <= 100:
    total = total + number
    number = number + 1
# Display the result
print(f"... Done the answer is {total}")