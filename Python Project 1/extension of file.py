# Program which takes in filename and gives extension type as output

filename = input("Enter a filename: ")
fe = filename.split(".")
print("The extension of the filename is: " + fe[-1])
