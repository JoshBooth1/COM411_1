# Ask the user for a location to search
print("Beep is looking for a way out of the forest")
print("Where should he look")
# Nests for each of the possible locations to search
place = input()

# Check the fog
if place == "fog":
    print("What did he hear?")
    fog_sound = input()
    print("What did he see?")
    fog_sight = input()

    # Identify and display what beep should do
    if (fog_sound == "nothing") and (fog_sight == "nothing"):
        print("It looks clear I can escape here!")
    elif (fog_sound == "growl") or (fog_sight == "yellow eyes"):
        print("Seems theres a bear! I need to find another place")
    else:
        print("That doesn't seem right I better try another place")

# Check the tunnel
if place == "tunnel":
    print("What did he hear?")
    tunnel_sound = input()
    print("What did he see?")
    tunnel_sight = input()

    # Identify and display what beep should do
    if (tunnel_sound == "nothing") and (tunnel_sight == "nothing"):
        print("It looks clear I can escape here!")
    else:
        print("That doesn't seem right I better try another place")
