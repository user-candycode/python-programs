'''
n!= 1*2*3*4*5*6*7.......*n
n!= 1*2*3*4*5..........*n-1*n
n!= [1*2*3*4*5..........*n-1]*n
n!= [n-1]!*n
'''

def factorial_recursive(fact):
    if fact==1 or fact==0:
        return 1
    return factorial_recursive(fact-1)*fact


resultant=factorial_recursive(5)
print(resultant)


