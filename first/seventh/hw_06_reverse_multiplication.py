a=int(5)

print("using the logic to reverse the loop iterations")
for i in range(10,0,-1):
    print(str(a) +" times " +str(i) + " is: ", a*i )


print("\nUsing the reversing of a list")
l1=[]
for i in range(11):
    l1.append(i*a)

l2=l1
z=int(len(l2))
for j in range(z):
    print(a,"times",10-j,"is:",l2.pop())