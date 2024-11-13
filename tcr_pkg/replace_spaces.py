import os

def replace_spaces(directory: str):
    """Replace spaces with underscores in filenames for html validation"""
    for filename in os.listdir(directory):
        if ' ' in filename:
            new_filename = filename.replace(' ', '_')
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Example usage:

if __name__ == '__main__':  # This will run if the file is run directly  
    dir ='../TCR/thumbs/'
    replace_spaces(dir)