import os
import shutil

fromDir = "C:/Users/Lenovo/Desktop/New folder/files"

toDir = "D:/"

list_of_files= os.listdir(fromDir)
#print(list_of_files)

for file_name in list_of_files:
   # print(file_name)

   name,extension = os.path.splitext(file_name)
#    print(name)
#    print(extension)
   if (extension == ""):
        continue
   if extension in ['.jpg','.png','.jpeg','.gif']:

        path1=fromDir+'/'+file_name

        path2 = toDir+'/'+"newImageFolder"

        path3= toDir+'/'+"newImageFolder"+"/"+file_name

        if os.path.exists(path2):
            print("moving files....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("moving files....")
            shutil.move(path1,path3)



