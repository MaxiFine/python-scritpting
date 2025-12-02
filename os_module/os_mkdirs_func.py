import os
directory = "Nikhil"
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created \n" % directory)
directory = "c"
parent_dir = os.getcwd()
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)