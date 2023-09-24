#WAP to display the words that are repeated more than or equal to n times in the text
# case sensitive

# I/P
input1 = "cat batman latt matter cat matter cat cat latt latt"
n = 3

# Method 1
output = list()
split = input1.split()
for i in split:
    if split.count(i) >= 3 and i not in output:
        output.append(i)
print(output)

# Method 2
counts =dict()
for i in input1.split():
    if i in counts:
        counts[i] +=1
    else:
        counts[i] = 1
print(counts)