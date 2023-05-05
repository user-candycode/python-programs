a = [2,5,45,65,21,47,89,62,1,4,21,35,45,2,54,3,4,5,6,7,8,9]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

b = {i for i in a if i%2==0}
print(b)

c = [i for i in a if i>8]
print(c)