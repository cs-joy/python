import os

if os.path.exists("deleteFile.txt"):
    os.remove("deleteFile.txt")
    print("file deleted successfully!")
else:
    print("The file does not exist")