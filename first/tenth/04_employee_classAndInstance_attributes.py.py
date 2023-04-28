class Employee:
    #the instance attribute values will overide these class attributes or chosen as default
    #this below class attribute only works if there is no explicite instance attribute initilization
    works_at="Google"
    salary=100

gajani= Employee()
rajani=Employee()

gajani.salary=300
rajani.salary=400

print(gajani.works_at)
print(rajani.works_at)

Employee.works_at="Youtube"
print(gajani.works_at)
print(rajani.works_at)

print(gajani.salary)
print(rajani.salary)


'''
gajani.salary =45
print(gajani.salary)
print(rajani.salary)

#here the output will be 
45 #The new instance value will overwrite the class attribute
100#The class attribute will be used as default
'''

'''
#below line throws an error
print(rajani.address)
'''