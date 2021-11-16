# Define the function and the steps
def cross_bridge(steps):
    for step in range(steps):
        print("Crossed step")

# Display the message based on how many steps are taken
    if steps > 5:
        print("The bridge is collapsing")
    else:
        print("We must keep going")


print("How many steps should we take?")
cross_bridge(int(input()))
