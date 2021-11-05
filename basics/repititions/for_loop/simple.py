# Ask user for a number of mountains
print("How many mountains should I display?")
mountains = int(input())

# Display the mountains based on the number entered by the user
print("Displaying...")

for mountain in range(mountains):
    print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\

  """)
