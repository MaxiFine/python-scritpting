"""
7. Using os.path.getsize() Function
os.path.getsize() function gives us the size of the file in bytes. To use this method we need to pass the name of the file as a parameter.

"""

import os 

size = os.path.getsize("os_change_cwd.py") #getting size of file
print(f"Size of the file is {size} bytes.")
