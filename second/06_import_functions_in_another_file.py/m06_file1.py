def greet(name):
    print(f"Good morning {name}")


#if __name__=__main__ is not there then while importing this module to amother file this will also run there 

if __name__ == "__main__":
    n=input("Enter a string")
    greet(n)
