#WAP to print prime number

num = int(input("Enter a number to be validated as prime or not:\n"))
flag=False
for i in range(2,num,1):
    if (num%i==0):
        flag=True
        break

if flag==True:
    print("its not a prime number")
else:
    print("its a prime number")