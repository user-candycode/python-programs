myDict1={
    "Pankha": "fan",
    "Kursi" : "chair",
    "Mejh" : "table"
}

print("Options are: ", myDict1.keys())
a=input("\nEnter the hinglish word:\n")
# print("the meaning of", a,"is",myDict1[a] + ".")  ---------Here myDict1[a] if a is not in sdictionary then it will throw an error
print("the meaning of", a,"is",myDict1.get(a) + ".")