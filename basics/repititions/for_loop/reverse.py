# Ask user to input a phrase
print("Wat phrase do you see?")
phrase = input()
# Reverse the phrase and output
print("Reversing... ")
print("")
print("The phrase is: ", end="")
for position in range(len(phrase) - 1, -1, -1,):
    print(phrase[position], end="")
