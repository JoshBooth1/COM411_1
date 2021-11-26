# Define the display first x characters characters function
def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)


# Define the display first line function
def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print(data)


# Define the display complete text function
def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


# Define the run function
def run():
    print("The first 7 characters are:")
    display_chars("library.txt", 7)
    print("")
    print("The first line is:")
    display_line("library.txt")
    print("")
    print("The whole text is:")
    display_text("library.txt")


# Call the run function
if __name__ == "__main__":
    run()
