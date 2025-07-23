myFile = open("demo.txt","r")
data = myFile.readline()
data2 = myFile.read(6)
myFile.close()

print(data)
print("-------------------")
print(data2)
