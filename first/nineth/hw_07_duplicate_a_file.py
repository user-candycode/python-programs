
with open('/home/candy/Documents/python/first/nineth/to_be_copied.txt', 'rt') as f:
    content=f.read()

with open('/home/candy/Documents/python/first/nineth/duplicated_new_file.txt', 'wt') as m:
    m.write(content)