import os

f = open("myfile.txt", "r")

print(f.read())
f.close()
os.remove("myfile.txt")
