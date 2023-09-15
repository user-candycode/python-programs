name = "Brooo"

print("Printing length of string: "+ str(len(name)) + " (prints actual length not index count)")
print("find 'o' in string: " + str(name.find("o")) + " (prints the index of first occurance)")
print("Capatalize the first character of the sting: " + name.capitalize())
print("Capatalize the whole string: "+name.upper())
print("Capatalize the whole string: "+name.upper())
print("IS only alphabets: "+ str(name.isalpha()))
print("Counting a character occurance: "+str(name.count('o')))
print("Replacing all matched character in a string: "+name.replace("o","O"))
print(name*3)
x="123a"
print("Checks a sting is a digit or not?: "+ str(x.isdigit())) #returns bool value
