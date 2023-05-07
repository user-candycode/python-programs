'''
    use of filter
    Filter Syntax: filter(function,           list or iterable object)
                                ^                           ^
                    (can be lambda function)        (list or string)
'''

def greater_than_5(num):
    if num>5:
        return True
    else:
        return False
    
l=[2,52,4,8,6,7,12,0,0,11,21,2,5]

g10 = lambda num:num>10

print(list(filter(greater_than_5,l)))
print(list(filter(g10,l)))