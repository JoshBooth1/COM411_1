# Define the cwd function
def cwd():
    import os
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    print(f"The current working directory contains the following:")
    for file in os.listdir(path):
        print(file)


# Define the run function
def run():
    print("Processing...")
    cwd()


# Run the functions
run()
