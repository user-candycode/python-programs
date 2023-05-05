try:
    i=int(input("enter an element"))
    c=1/i
except Exception as e:
    print(e)
#here the except act as a if statement which whenskipped then else will automatically will be executed
else:
    print("Runs only if try was sucessfull")


'''
    here try runs compalsary first
    then if try succesfull else will also be sucessfull
    if try fails then only except will run 
'''


