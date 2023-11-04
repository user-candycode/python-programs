n1=0
n2=1
def printFibonacci(n):
    global n1
    global n2
    if n>2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3,end=" ")
        printFibonacci(n-1)

n = 57
print(f"{0} {1}",end=" ")
printFibonacci(n)