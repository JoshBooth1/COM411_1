# Retrieve story type from user
print("Kind of adventure should I have?")
adventure = input()

# Identify the adventure types
if (adventure == "Short") or (adventure == "Scary"):
    print("Entering the dark forest")
elif (adventure == "Long") or (adventure == "Safe"):
    print("Taking the safe route")
else:
    print("Not sure which route to take")
