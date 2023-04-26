#WAP to find greatest of 3 numbers

def maximum(num1,num2,num3):
    temp_max=0
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
    

print(maximum(23,354,545))
