def printTable(user_input):
    list = [i*user_input for i in range(1, 11)]
    print(list)
    with open(f"/home/candy/Documents/python/second/hw_05_store_output_from_hw_03_to_a_file/table_of_{user_input}.txt", 'wt') as f:
        for index,element in enumerate(list):
            f.write(f"{user_input} * {index+1} = {element}\n")


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
    except ValueError as ve:
        print("Enter a valid integer as a number")
    except:
        print("Something else went wrong")
