file = open("deleteFile.txt", "x")
file.write("Hello delete!")
file.close()

file = open("deleteFile.txt", "r")
print(file.read())