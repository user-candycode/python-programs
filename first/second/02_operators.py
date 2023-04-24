a = 3
b = 4

#Arithimatic operators
#divide / always gives a float
print("The sum of 3 & 4 is:",3+4)

#Assignment operators
a=34
a += 2
print(a)
'''
    -=
    *=
    /=
'''

#careful with float conversion
b=22
b /= 7
print("print b:",b) #automatic conversion
print("print b+1:", b+1) #b now remains float
print(b-0.142857142857143)#b still remains float


#Comparison operator
c=(4>7)
print(c)

#Logical operators
'''
 and
 or
 not
'''
bool1=True
bool2=False
print("the value of bool1 and bool2 is:", bool1 and bool2)
print("the value of bool1 or bool2 is:", (bool1 or bool2))
print("the value of not bool1 is:", not bool1)

