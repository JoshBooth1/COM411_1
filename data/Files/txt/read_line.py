# Define the search function
def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("Done!")


# Define the run function
def run():
    search("library.txt")


# Call the run function
if __name__ == "__main__":
    run()
