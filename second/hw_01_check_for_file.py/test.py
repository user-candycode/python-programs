import os

# Get the current working directory
dir_path = os.getcwd()
dir_path = os.path.dirname(os.path.abspath(__file__))

print(dir_path)

# Get a list of all the files in the directory
file_list = os.listdir(dir_path)
print(file_list)
print()
# print(type(file_list))



def readfile(file_name):
    try:
        stich="/home/candy/Documents/python/second/hw_01_check_for_file.py/"+file_name
        with open(stich, "r") as f:
            print(f"{stich}:")
            print(f.read())

    except :
        print(f"{file_name} not found on the system.")


file_list.sort()
for file_name in file_list:
    if file_name.endswith('.txt'):
        readfile(file_name)
        # print(file_name)

