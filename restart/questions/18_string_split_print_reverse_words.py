input1 = "python is easy"

words = input1.split()
print(words)

list1 = []
for i in words:
    list1.append(i[::-1])
print(list1)

output = " ".join(list1)
print(output)