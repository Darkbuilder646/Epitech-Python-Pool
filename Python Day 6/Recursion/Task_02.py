import os as os 

for root, dirs, files in os.walk(".", topdown=True):
    print(root)
    print(files)
    print("-------------------")
