# Ask the user for a location to search
print("Beep is looking for his spare battery")
print("Where should he look")
# Nests for each of the possible locations to search
place = input()

# Check the bedroom
if place == "bedroom":
    print("Where in the bedroom should I look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

# Check the bathroom
elif place == "bathroom":
    print("Where in the bathroom should I look?")
    bathroom_place = input()

    if bathroom_place == "in the bath":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

# Check the lab
elif place == "lab":
    print("Where in the lab should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

# If the place is unknown
else:
    print("I do not know where that is but I will keep looking.")