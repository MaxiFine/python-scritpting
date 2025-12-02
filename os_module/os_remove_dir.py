import os 
directory = os.getcwd() + "/c/"
parent = os.getcwd()
path = os.path.join(parent, directory) 
print("Removing Directory '% s' : \n" % directory)
os.rmdir(path)
print("Directory '% s' removed successfully" % directory)
print(os.listdir(parent))
