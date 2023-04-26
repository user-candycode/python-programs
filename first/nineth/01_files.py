import os
#by default in open the mode is r  i.e. open('location')
f = open('/home/candy/Documents/python/first/nineth/sample.txt', 'r')
data=f.read()
print(type(data))
print(data)

f.close()





f = open('/home/candy/Documents/python/first/nineth/sample.txt', 'r')
read_first_5_characters=f.read(55)
print("\nFirst 5 characters: ",read_first_5_characters)
f.close()
