# Ask the user for a phrase
print("Wat phrase do you see?")
phrase = input()
# Reverse the phrase and output
print("\nReversing... ")
print("")
print("The phrase is: ", end="")
reversed_mo = ""
for letter in phrase:
    reversed_mo = letter + reversed_mo
print(reversed_mo)
