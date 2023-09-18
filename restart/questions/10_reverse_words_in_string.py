str1 = "sky is blue"

temp_list = str1.split()
print("reversed in list: ",end="")
print(temp_list:=temp_list[::-1])

str2 = " ".join(temp_list)
print(str2)

# OR
# print(" ".join(str1.split()[::-1]))
