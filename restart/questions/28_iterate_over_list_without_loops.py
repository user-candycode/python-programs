def iterate(n):
    if n>=0:
        print(llist[n],end=" ")
        iterate(n-1)
    else:
        return ""

llist = [10,9,8,7,6,5]
print(llist)
n = len(llist)
print(n)
print("="*n*2)
iterate(n-1)
print("")
# can also use start end pointer approach