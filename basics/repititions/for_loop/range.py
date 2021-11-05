# Ask the user to provide a brightness level
print("What level of brightness is required?")
brightness_required = int(input())

# Loop to display a an asterix for each even level of brightness
print("\nadjusting brightness...\n")
for brightness in range(2, brightness_required + 1, 2):
    print(f"Beeps brightness: {'*' * brightness}")
    print(f"Bops brightness: {'*' * brightness}")

print("Adjustments complete!")
