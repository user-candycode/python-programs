
with open('/home/candy/Documents/python/first/nineth/Identical_file1.txt', 'rt') as f1:
    file1_content=f1.read()

with open('/home/candy/Documents/python/first/nineth/Identical_file2.txt', 'rt') as f2:
    file2_content=f2.read()

if file1_content == file2_content:
    print("both files are identical")
else:
    print("Files are NOT identical")
