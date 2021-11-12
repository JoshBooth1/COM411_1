# Ask the user for a number
print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())

# Use the chr function to convert any numbers in the range to an ascii character
if 33 <= code <= 126:
    print(f"The character represented by the ASCII value {code} is: {chr(code)}")

# Display errors for if the number is enter out of range or as an non visual character
elif 0 <= code <= 32:
    print("This number represents an ascii character that cannot be displayed visually")
elif code >= 127 >= code:
    print("This number represents an ascii character that cannot be displayed visually")
else:
    print("This number does not relate to an ascii character")
print("Program Ended!")
