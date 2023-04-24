
#concatinating strings two strings
greeeting= "Good Morning, "
name="harry"

c=greeeting + name
print(c)


'''
string splicing
          ___________
    name= |H|a|r|r|y| ==> length = 5
           0 1 2 3 4
          -5-4-3-2-1
'''

#extracting first element of a string
print("first element of name is ",name[0])

'''
    also strings in python are immutable
'''

print(name[0:3])
#first on is inclusive and th next after : is not inclusive
print(name[1:3])
#if start parameter is not given then it defaults to 0 && if last parameter is not given it defaults to length of string here 5
print(name[:])

'''
    name[inital_index:last_index:skip_inital_value_by]
    i.e. name[1:5:1]
'''
print(name[1:5:2])

name="harry is good"
print(name[0::2])