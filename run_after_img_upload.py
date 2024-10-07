import os

def rename_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-files (e.g., directories) and process only files
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Sort the files to ensure consistent renaming order
    files.sort()

    # Loop through the files and rename them
    for index, filename in enumerate(files):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Create the new filename (img1.jpg, img2.jpg, etc.)
        new_filename = f"img{index + 1}{file_extension}"

        # Create full file paths
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Specify the folder path
folder_path = 'C:/Users/19tay/Documents/GitHub/nora/images'  # Replace with the actual folder path

# Call the function
rename_files_in_folder(folder_path)
