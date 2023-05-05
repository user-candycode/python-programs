def readfile(file_name):
    try:
        stich="/home/candy/Documents/python/second/hw_01_check_for_file.py/"+file_name
        with open(stich, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{file_name} not found on the system.")

readfile('file1.txt')
readfile('file2.txt')
readfile('file3.txt')



