import os

if os.path.exists("newFolder"):
    os.rmdir("newFolder")
    print("directory removed successfully!")
else:
    print("the directory does not exist")