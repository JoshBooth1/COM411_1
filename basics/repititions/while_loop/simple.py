# Ask for a number of cables to remove
print("How many cables should I remove?")
cables_to_remove = int(input())

# Declare a control variable
cables_removed = 0

# Display the removal of cables
print()

while cables_removed < cables_to_remove:
    print("Removed cable.")
    cables_removed = cables_removed + 1
