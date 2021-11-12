# Ask the user to select a sequence
print("Please enter a sequence")
sequence = input()
# Ask the user to add a marker
print("Please enter a marker")
marker = input()

marker1_position = -1
marker2_position = -1

for position in range(0, len(sequence), 1):
    letter = sequence[position]
    if letter == marker:
        if marker1_position == -1:
            marker1_position = position
        else:
            marker2_position = position

# Display the distance between the 2 markers
print(f"The distance is {marker2_position - marker1_position - 1}.")
