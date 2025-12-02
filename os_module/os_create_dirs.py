# Creating directories using os.makedirs() and listing files in the created directory
import os

directory = "new_dir_by_mkdir"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)  # joining parent directory with the new directory name
os.mkdir(path)  # creating the directory
print("Directory '% s' created at: \n" % directory)
print(path)
print()
new_dirs = "GeekBymkdir"
parent_dir = os.getcwd()
mode = 0o666
path = os.path.join(parent_dir, new_dirs)
os.mkdir(path, mode)  # creating the directory with specific mode
print("Directory '% s' created..." % new_dirs)



# os.makedirs(path, exist_ok=True)  # creating the directory
# print(f"Directory '{directory}' created at: {path}")

# # Listing files in the created directory
# files = os.listdir(path)
# print(f"Files in '{directory}': {files}")