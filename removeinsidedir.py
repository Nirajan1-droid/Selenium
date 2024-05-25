import os

def remove_files_except_2(root_dir):
    """Remove files whose names are not '2' from child directories."""
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name != '2.jpg':
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Removed file: {file_path}")

# Example usage
root_directory = "C:/pdffilter/split_output"
remove_files_except_2(root_directory)
