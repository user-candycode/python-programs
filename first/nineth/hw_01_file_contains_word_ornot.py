
with open('/home/candy/Documents/python/first/nineth/file_containing_the_word.txt','rt') as f:
    t=f.read()
    print(t)
    if "COVID" in t:
        print("Covid found")
    else:
        print("no covid found")
