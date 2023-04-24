'''
    greatest of 4 numbers
'''

a=int(5)
b=int(45)
c=int(23)
d=int(12)

'''temp=int(0)
if(temp<=a):
    temp=a
if(temp<=b):
    temp=b
if(temp<=c):
    temp=c
if(temp<=d):
    temp=d

print("greatest of 4 number is:",temp)
'''

#another solution than above is
if(a>b):
    f1=a
else:
    f1=b
if(c>d):
    f2=c
else:
    f2=d

if(f1>f2):
    f1=f1
else:
    f1=f2

print("greatest of 4 number is:",f1)
