import os

def rename_subsidy_applications(directory):
    # Get a list of all files in the directory
    files_list = os.listdir(directory)
    
    # Sort files based on modification time
    files_list.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    
    for i, file in enumerate(files_list):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            # Check if the file name contains "subsidy application"
            if "subsidy application" in file.lower():
                # Check the next 7 files
                for j in range(i+1, min(i+8, len(files_list))):
                    invoice_file = files_list[j]
                    # Check if the file name contains "invoice" and "gs"
                    if "invoice" in invoice_file.lower() and "gs" in invoice_file.lower():
                        # Rename the "subsidy application" file with "gs" prefix
                        base_name, extension = os.path.splitext(file)
                        new_name = f"gs_{base_name}{extension}"
                        os.rename(file_path, os.path.join(directory, new_name))
                        print(f"Renamed: {file} -> {new_name}")
                        break

# Define the directory to search
directory_to_search = r"C:/rejected"

# Call the function to rename subsidy applications
rename_subsidy_applications(directory_to_search)
