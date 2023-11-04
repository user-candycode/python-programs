inp = int(16)
first = 0
second = 1

if inp<=0:
    print("Please enter positive integer")
elif inp==1:
    print(first)
else:
    x=0
    z=1
    for i in range(inp):
        print(first,end=" ")
        temp = first + second
        first =second
        second =temp
    print("")