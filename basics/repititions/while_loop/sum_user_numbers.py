print("How many numbers should I add up?")
numbers_to_sum = int(input())
summed_numbers = 1
total = 0
while summed_numbers <= numbers_to_sum:
    print(f"Please enter number {summed_numbers} of {numbers_to_sum}:")
    number = int(input(""))
    total = total + number
    summed_numbers = summed_numbers + 1

print(f"The total is {total}")
