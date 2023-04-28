
a="WARNING"

with open("/home/candy/Documents/python/first/nineth/IBM_log_file.txt",'rt') as f:
    content=f.read()

if a in content.upper():
    print("yes warnings are present")
else:
    print("no warnings are found, system in safe state")