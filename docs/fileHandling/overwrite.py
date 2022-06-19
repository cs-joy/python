file = open("overwrite.txt", "w")
file.write(",,it's overwrite now!")
file.close()

file = open("overwrite.txt", "r")
print(file.read())