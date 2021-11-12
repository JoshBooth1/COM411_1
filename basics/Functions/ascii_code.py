# Ask the user for a standard character
print("Program Started!")
print("Please enter a standard character:")
character = input()
# Use the len + ord functions to output the ascii value of the user input
if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
# If the user enters more than 1 character display an error message
else:
    print("Please enter a single character")
print("Program Ended!")
