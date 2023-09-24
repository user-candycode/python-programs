string = input("Enter a string: ")
count = 0

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count+=1

print(count)