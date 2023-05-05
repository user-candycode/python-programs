def printTable(user_input):
    list = [i*user_input for i in range(1, 11)]
    print(list)


print("==============Press q to quit the program anytime==================")
flag = True
while (flag):
    user_input = input("Enter a number to print its table:\n")
    if user_input == 'q':
        break
    try:
        print(f"Printing table of {user_input}......")
        user_input = int(user_input)
        printTable(user_input)
        # OR
        # list = [i*user_input for i in range(1, 11)]
        # print(list)
    except ValueError as ve:
        print("Enter a valid integer as a number")
    except:
        print("Something else went wrong")
