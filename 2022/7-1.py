# There is a file system consists of a tree of files and directories.
# You are given a list of commands you executed.
# Find all the directories with a total size of at most 100000 and sum up their sizes.

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name: str, parent: 'Directory'):
        self.name = name
        self.parent = parent
        self.files = []
        self.subdirectories = []
        self.size = 0

def grow(pwd: Directory):
    log = open('7-input.txt', 'r').readlines()

    # Parse the log file to build a file tree.
    for i, line in enumerate(log):
        if line.startswith('$ ls'):
            while i + 1 < len(log) and not log[i + 1].startswith('$'):
                i += 1
                if log[i].startswith('dir'):
                    pwd.subdirectories.append(Directory(log[i].split(' ')[1].strip(), pwd))
                else:
                    file_size, file_name = log[i].split(' ')
                    pwd.files.append(File(file_name.strip(), int(file_size)))
                    pwd.size += int(file_size)
        elif line.startswith('$ cd'):
            arg = line.split(' ')[2].strip() # Remove trailing newline.
            if arg == '/':
                pwd = root
            elif arg == '..':
                pwd.parent.size += pwd.size
                pwd = pwd.parent
            else:
                pwd = [d for d in pwd.subdirectories if d.name == arg][0]

def show(dir: Directory, indent: int = 0):
    res = 0
    if dir.size > 100000:
        print(f"\033[1;31m{indent * '\t'}DIR-{dir.size}\033[0m") # Red for large dirs
    else:
        res += dir.size # Add to sum if <= 100000
        print(f"\033[1;32m{indent * '\t'}DIR-{dir.size}\033[0m") # Green for small dirs
        
    for f in dir.files:
        print(f"{(indent+1) * '\t'}FILE-{f.size}")
        
    for d in dir.subdirectories:
        res += show(d, indent + 1)
        
    if indent == 0:
        print(f"\nSum of directories <= 100000: {res}")
    
    return res

root = Directory('/', None)
grow(root) # Build a file tree.
show(root) # Print the file tree.