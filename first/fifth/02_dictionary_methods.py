myDict = {
    "fast": "I am a fast coder",
    "MrK": "A fast coder",
    "marks": [1,2,3,4,7,5,3,12],
    "anotherDict": {'harry': 'player1', 'MrK': 'player2' },
    1:2
}
'''
    ================Dictionary methods==================
'''

#print keys of a dictionary
print("\nprints the keys of a dictionary:\t",myDict.keys())
#print type of dictionary keys i.e its always dict_keys
print("\nprint type of dictionary keys of dictionary:\t",type(myDict.keys()))
#convert to dictionary to a list 
print("\nconvert dictionary keys to a list:\t",list(myDict.keys()))
#print the values of dictionary
print("\nprint only the values of dictionary:\t",myDict.values())
#convert to tuples i.e prints (key, value),(key2, value2) for all items of dictionary
print("\nconvert's to tuples:\t",myDict.items())

# ================= Learn to update Dictionary==================
#done by adding key value pairs from another dictionary
print("\n",myDict)
updateDictionary = {
    "Lovish": "friend"
}
myDict.update(updateDictionary) #new dict will be appended at the end to orignal dictionary note it will change the existing value of key if already existing in  the orignal dictionary
print("\n",myDict)


#===============Get method for Dictionary======================
#get is better than printing the value as print(myDict["Key_name"]) because get function will simply tells none if the key to be matched in the dictionary is not present, whereas the printing the value to the key will throw an error and stop the program execution

print(myDict.get("MrK"))    #if the key here is mrk2 then this will throw none on to the screen
print(myDict["MrK"])        #if the key here is mrk2 then this will throw an error