
def recursive_sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+recursive_sum(n-1)




print(recursive_sum(5))