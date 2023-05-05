list1=[3,54,67,False,True,'a',"Hello",'''MrK''',3.14]

# index=0
# for item in list1:
#     print(index,item)
#     index += 1

for index,item in enumerate(list1):
    print(index,":",item,":\t",type(item))