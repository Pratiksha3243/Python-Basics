# myFile = open("demo.txt","r")
# data = myFile.readline()
# data2 = myFile.read(6)
# myFile.close()

# print(data)
# print("-------------------")
# print(data2)

# # # Writing a file Overwritten
myFile = open("demo.txt","w")
myFile.write("\My Name is Pratiksha")
myFile.close()

# # # Writing a file Appending
import os
myFile = open("demo.txt","a")
myFile.write("\My Name is Pratiksha")
myFile.close()
os.remove("demo.txt")

# 1
FileName= open("practice.txt","w")
FileName.write("Hi everyone \n We are learning File handling I/O \n using Python \n I like programming in Python")
FileName.close()