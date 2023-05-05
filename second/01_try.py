while (True):
    print("press q to quit")
    a = input("enter a number:\n")
    if a == 'q':
        break
    try:
        #this will run as far as possible then wherever it encounters an error it will switch to except
        print("trying......")
        a = int(a)
        if a > 6:
            print("You enter a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error:\t {e}")


print("thanks for playing this game")
