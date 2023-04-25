#WAP to print multiplication table for given input

a=input("=====Enter a number to print its multiplication table=====\n")
x=int(1)

if a.isdigit():
    x=int(a)
    print("Input number belongs to ",type(x))
    print("\nSo,its a valid number")
else:
    print("\n\trun the program again")

#using x print its table
for i in range(1,11,1):
    #output=x * i
    #print(str(x)+" * "+str(i)+" = ",output)
                #OR
    print(f"{x}X{i} is equals to {x*i}")
    