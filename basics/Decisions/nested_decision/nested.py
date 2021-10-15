# ask user what cover type the book has
print("What type of cover does the book have? (Hard/Soft)?")
cover_type = input()

# decide if beep should play or study
if cover_type == "Soft":

    # ask user if th book is perfect bound
    print("Is the book perfect bound (y/n)?")
    perfect_bound = input()

    # decide if beep should play with toys or friend
    if perfect_bound == "y":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
