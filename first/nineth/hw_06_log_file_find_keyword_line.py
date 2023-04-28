
i=1
content=True
with open("/home/candy/Documents/python/first/nineth/IBM_log_file.txt",'rt') as f:
    while content:
        content=f.readline()
        
        if 'warning' in content.lower():
            print(content)
            print("Warning is present")
            print("AT line: ",i)
        i=i+1