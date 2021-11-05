# Ask user for a word
print("What strange markings do you see?")
markings = input()

# Identify each letter
print("\nIdentifying...\n")
for count in range(0, len(markings), 1):
    print(f"index {count}:", markings[count])
print("")
print("Done!")
