list1 = [1,2,2,3,3,4,5,5,5,6,6]
templist = list()
for num in list1:
    if list1.count(num) == 1:
        templist.append(num)

print(templist)
