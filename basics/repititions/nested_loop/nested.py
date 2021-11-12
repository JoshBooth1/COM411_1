# Ask how many rows and columns there should be
print("How many rows should I have?")
rows = int(input())
print("How many columns should I have?")
columns = int(input())
print("Here I go:")
# Display the table of ascii emojis
for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(":-)", end="")
print()


