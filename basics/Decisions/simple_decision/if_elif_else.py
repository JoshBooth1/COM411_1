# Ask the user to choose a direction to paint in
print("Which direction should I paint in? (Up, Down, Left or Right)")
direction = input()
# Give a response based on the input of the user
if direction == "left":
    print("I'm painting left")
elif direction == "right":
    print("I'm painting right")
elif direction == "up":
    print("I'm painting up")
elif direction == "down":
    print("I'm painting down")
else:
    print("I can't go in that direction!")

print("Painting complete.")