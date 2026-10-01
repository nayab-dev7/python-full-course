import os

# Specify the path you want to list ('.' means the current directory)
path = '/root'

# List only the directories
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

print("Directories in Current Folder:")
for folder in directories:
    print(f"📁 {folder}")