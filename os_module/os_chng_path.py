import os


## Changing Directory with os.chdir()
def current_path():
    print("Current Directory Path: \n", os.getcwd())
    print()
current_path()
print("Changing Directory to Root Path...")
os.chdir('../')
print('Path Changed Successfully.\n')
print("Current Root Directory Path: \n", os.getcwd())
