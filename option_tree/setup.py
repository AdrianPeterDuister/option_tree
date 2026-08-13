import os

os.makedirs("src")

files ={"README.TXT" : "",
        "main.py": "# code runs here",
        "src/forward_tree.py": "# creates forward propogated price tree function",
        "src/backward_tree.py": "# creates backward propogated value tree functions"}


for file, description in files.items():
    with open(file, "w") as new_file:
        new_file.write(description)
    
    print(f"made file {file}")