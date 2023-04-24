#Creating an empty set
b= set()
print(type(b))

#Adding values to empty sets
b.add(4)
b.add(5)

#Printing the resultant set
print("\nsimply printing the set be after inserting two values",b)

'''
    sets cant have lists and dictionary inside it because they both are not hashable as their contents can be changed
    so, tuples can be allowed but not sets
    hence,
        b.add([1,2,3])  #throws an error
'''

#inserting tuples to a set
b.add((4,5,6 ))
print("\nprinting the values after inserting a tuples to the set",b)


#printing a length of a set
print("\nLength of set b is:",len(b))

#removing elements from set 
b.remove(4)
#b.remove(999) #throws an error because 999 is not an set element
print("\nremoved 4:",b)


# ---------pop function will remove randomly any one value of a set
print(b.pop())  #useful for picking up any random arbitary element
