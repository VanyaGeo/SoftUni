import os

# Set the directory where your .py files are located
directory = 'your_file_path'

# Define the current and new file extensions
current_extension = '.py'
new_extension = '.sql'

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(current_extension):
        # Generate the new file name with the new extension
        new_filename = os.path.splitext(filename)[0] + new_extension
        # Create the full file paths
        current_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(current_path, new_path)

print(f"Changed extensions from {current_extension} to {new_extension} for files in {directory}")


# import os
#
# # Get the current working directory
# current_directory = os.getcwd()
#
# print("Current directory:", current_directory)