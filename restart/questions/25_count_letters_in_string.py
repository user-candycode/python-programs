# WAP to count no of occurences in a string of its characters

input1 = "aaaabbbccd"
output = ""

set1 = set()
for i in input1:
    set1.add(i)

sorted_list = sorted(set1)
for x in sorted_list:
    z = input1.count(x)
    output = output + f"{x}:{z} "

print(output)