import os 
directory="Python" #folder1
#directory2="Python2" #folder2
parent_dir="C:/Users/ernur/Desktop/" #main directory
path=os.path.join(parent_dir, directory) #path of 1 folder
#path2=os.path.join(parent_dir, directory2) #path of 2 name 
os.mkdir(path) #create directory
#os.rmdir(path) #delete directory
#os.rename(path, path2) #give another name
print(os.getcwd())#read directory
