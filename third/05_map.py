square = lambda num : num*num
l=[5,7,1]

#method one 
l2 = []
for item in l:
    l2.append(square(item))

print(l2)


#method two
print(list(map(square,l)))
#       ^ for type casting map from <map object at 0x7f3db780b820> to [25, 49, 1]
