# user input the number of steps from the cave
print("How many steps are we from the cave?")
steps = int(input())

# Display the countdown

for count in range(steps, 0, -1):
    print(f"{count} steps remaining")

print("We have reached the cave!")

