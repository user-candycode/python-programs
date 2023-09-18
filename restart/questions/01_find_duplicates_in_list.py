# WAP to print the duplicates in a list

list = ["hello",10,20,40,20,60,40,30]

# SOLUTION

dlist = []
for element in list:
	if list.count(element) >1 and element not in dlist:
		dlist.append(element)

print(dlist)
