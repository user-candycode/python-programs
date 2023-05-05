try:
    i=int(input("enter an element"))
    c=1/i
except Exception as e:
    print(e)
    exit()
#finally runs even if the entire program was exited
finally:
    print("No matter what this will run always whenever a try is there, whether the try is sucessfull or not")

