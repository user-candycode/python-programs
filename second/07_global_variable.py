a =54 #Global variable

def funct1():
    global a 
    print("Global:\t",a)
    #global Will overite a of global in next step

    a= 8 # local variable
    print("Local:\t",a)

funct1()
print("Global:\t",a)