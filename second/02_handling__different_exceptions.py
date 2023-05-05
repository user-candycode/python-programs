try:
    a=int(input("enter a number:\n"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Enter a valid data")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")
    print(e)
except:
    print("something else went wrong")

print("\nthanks for using this code!")