list1 = ["hello",10,20,40,20,60,40,30]

d=list()

for i in list1:
    if list1.count(i) > 1 and i not in d:
        d.append(i)

print(d)


# MEthod 2
temp_list = list()
l = len(list1)
for i in range(l):
    for j in range(i+1,l):
        if list1[i] == list1[j] and list1[i] not in temp_list:
            temp_list.append(list1[i])
            break

print("Method 2 ",temp_list)