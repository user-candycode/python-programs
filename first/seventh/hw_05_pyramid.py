#WAP to print pyramid
'''
        *
       ***
      *****
    this is actually a matrix of 3 rows by 5columns i.e. if rows=rows then columns=(rows*2)-1
'''
rows=5

for i in range(rows):
    print(" " * (rows-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (rows-i-1))


'''
    * * *
    *   *  3+1-1 = n + (n-2) -1
    * * *

    * * * * *
    *       *
    *       *  5+3-1 = n + (n-2) -1
    *       *
    * * * * *

    * * * * * * * *
    *             *
    *             *
    *             *  8+6-1 = n + (n-2) -1 =
    *             *
    *             *
    *             *
    * * * * * * * *

'''
print("\n============2==========\n")
row=int(5)
for i in range(1, row+1, 1):
        mid=int(row + (row-2) -1)
        if i == 1 or i == row:
            print("*",end="")
            for j in range(1,mid+1):
                print("*", end="")
            print("*")
        else:
            print("*",end="")
            for j in range(1,mid+1):
                print(" ", end="")
            print("*")  
 