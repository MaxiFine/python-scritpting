## Getting Current Working Directory and Creating a New Directory, adding 'test_directory' to it.

import os
cwd  = os.getcwd()
print("Current Working Directory:", cwd)

new_dir = os.path.join(cwd, 'test_directory')
os.mkdir(new_dir)
print("New Directory Created:", new_dir)
print("Directory 'test_directory' created successfully.")
