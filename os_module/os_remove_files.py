"""
os.remove() method is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method.

"""
import os

# --------------------------------------------------------------
# Example: Removing a file using os.remove() method

file = 'file1.txt'
location = os.getcwd()  # current working directory
path = os.path.join(location, file)
# removing the file 
os.remove(path)
print(f"File '{file}' removed from location: {location}")
os.listdir(location)  # listing files in the current directory