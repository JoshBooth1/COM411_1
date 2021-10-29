# Ask user for input on how many live cables to avoid
print("How many live cables should I avoid")
cables_to_avoid = int(input())

# Control variable
cables_avoided = 0

# Display avoiding the cables
while cables_avoided < cables_to_avoid:
    print("Avoiding cables...", end="")
    print("on the same line")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} cables avoided.")
print("All live cables have been avoided")
