# Retrieve what is seen and heard from the user
print("What did I hear?")
sound = input()
print("What did I see?")
sight = input()

# Identify and display what beep should do
if (sound == "hoot") and (sight == "2 red eyes"):
    print("There is a scary creature. I should get out of here!")
else:
    print("I am a little scared but I will continue.")
