import os

def print_directory_tree(root_dir, file, prefix=""):
    entries = sorted(os.listdir(root_dir))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        is_last = index == (entries_count - 1)
        connector = "└── " if is_last else "├── "
        
        if os.path.isdir(path):
            line = f"{prefix}{connector}{entry}/"
            file.write(line + "\n")
            
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_tree(path, file, new_prefix)
        else:
            line = f"{prefix}{connector}{entry}"
            file.write(line + "\n")

if __name__ == "__main__":
    project_dir = os.getcwd()  # Current folder
    output_file = "Project Folder Structure.txt"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(project_dir + "\n")
        print_directory_tree(project_dir, f)
    
    print(f"Folder structure of current directory has been saved to '{output_file}'.")
