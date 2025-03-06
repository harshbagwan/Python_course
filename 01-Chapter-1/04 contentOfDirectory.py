import os  # Import the os module to interact with the operating system

# Specify the directory path (change this to the desired directory)
directory_path = 'D:\BOOKS'  # Use '.' for the current directory or provide a specific path

# Print a message indicating the directory contents
print(f"Contents of directory '{directory_path}':")

# Iterate through the list of files and directories in the specified directory
for item in os.listdir(directory_path):
    print(item)  # Print each item
