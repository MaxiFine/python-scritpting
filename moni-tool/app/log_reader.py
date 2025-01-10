import os

def list_files_in_directory(directory):
    """List all files and directories in the given path."""
    try:
        items = os.listdir(directory)
        return items
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return []

def fetch_file_content(file_path):
    """Fetch the content of the selected log file."""
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return content
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Step 1: List available files in `/var/log`
    directory = "//wsl$/Ubuntu/var/log"  # Replace `Ubuntu` with your WSL distro name
    items = list_files_in_directory(directory)
    
    if items:
        print("Files and directories in '/var/log':")
        for i, item in enumerate(items, start=1):
            print(f"{i}: {item}")
        
        # Step 2: Prompt the user to select a file
        choice = int(input("Enter the number of the file or directory to process: ")) - 1
        selected_item = os.path.join(directory, items[choice])
        
        # Step 3: Check if the selected item is a file or directory
        if os.path.isfile(selected_item):
            # Read the file content
            print(f"Reading file: {selected_item}")
            content = fetch_file_content(selected_item)
            print("".join(content[:10]))  # Display the first 10 lines as a preview
        elif os.path.isdir(selected_item):
            # List files in the directory
            print(f"{selected_item} is a directory. Listing contents:")
            sub_items = list_files_in_directory(selected_item)
            for sub_item in sub_items:
                print(f"- {sub_item}")
        else:
            print("Invalid selection.")
    else:
        print("No files or directories found.")
