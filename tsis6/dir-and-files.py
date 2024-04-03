#1
import os

path = "/path/to/directory"
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all_directories = []
all_files = []
for root, dirs, files in os.walk(path):
    for d in dirs:
        all_directories.append(os.path.relpath(os.path.join(root, d), path))
    for f in files:
        all_files.append(os.path.relpath(os.path.join(root, f), path))
print(directories)
print(files)
print(all_directories)
print(all_files)

#2
import os

path = "/path/to/file_or_directory"
exists = os.path.exists(path)
readable = os.access(path, os.R_OK)
writable = os.access(path, os.W_OK)
executable = os.access(path, os.X_OK)
print(exists)
print(readable)
print(writable)
print(executable)

#3
import os

path = "/path/to/file_or_directory"
if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(filename)
    print(directory)
else:
    print("do not exist")
    
#4
file_path = "example.txt"
with open(file_path, 'r') as file:
    line_count = sum(1 for line in file)
print(line_count)

#5
file_path = "example.txt"
input_list = [1, 2, 3, 4, 5]
with open(file_path, 'w') as file:
    for item in input_list:
        file.write(str(item) + '\n')
        
#6
import string

for letter in string.ascii_uppercase:
    file_path = f"{letter}.txt"
    with open(file_path, 'w'):
        pass 
    
#7
source_path = "example.txt"
destination_path = "destination.txt"
with open(source_path, 'r') as example_file:
    with open(destination_path, 'w') as destination_file:
        for line in example_file:
            destination_file.write(line)
            
#8
import os

file_path = "example.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File is deleted")
else:
    print("do not exist")