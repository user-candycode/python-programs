data = {'jay':['male',23,2000],'raj':25,'vicky':['male',22],'ram':['male',23]}
count = 0

for item in data:
    if isinstance(data[item],list):
        count+=1
print(count)