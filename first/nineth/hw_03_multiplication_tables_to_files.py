for i in range(2,21):
    with open(f"/home/candy/Documents/python/first/nineth/tables/table_of_{i}.txt",'wt') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
        #break to check first 2d loop