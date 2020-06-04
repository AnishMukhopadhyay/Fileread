fileName = input ("Enter the file name : ")
file = open(fileName, "a")
data = input ("Enter the data for append in the file "+ fileName + " : \n")
file.write("\n")
file.write(data)
file.close()
print("File Information")
file = open(fileName,"r")
print (file.read())



