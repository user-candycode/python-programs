#lists are mutable objects

l1=[1,8,7,2,21,15]
print("Orignal:",l1)
#Sorting the list
l1.sort()
print("Sorted: ",l1)

#reversing the sorted list 
l1.reverse()
print("Reversed Sorted:",l1)

#append to a list note: append appends at he end of the list
l1.append(45)
print("45 appended:",l1)

#insert at location and shifts the rest ahead at indexes
print("Length of l1 now:",len(l1))
l1.insert(3,69)
print("Inserted 69 at index 3:",l1)


#pop i.e. removes the last entry from the list
print("Orignal NOW1:",l1)
l1.pop()
print("poped:",l1)

print("Orignal NOW2:",l1)
l1.pop(0)
print("poped at index 0:",l1)

#removes (takes argument) the first match
l1.append(69)
l1.append(69)
l1.append(69)
l1.append(69)

print("Orignal NOW3:",l1)
l1.remove(69)
print("Removed 69:",l1)

#counting in list
print(l1.count(69))
