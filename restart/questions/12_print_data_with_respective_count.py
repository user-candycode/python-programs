mystr = "a,a,a,b,b,c,c,c"

templist = []
templist = mystr.split(",")
print(templist)

countlist = list()
set1 = set()
for data in templist:
    if data not in set1:
        countlist.append(f"{data}:{templist.count(data)}")
        set1.add(data)

print(",".join(countlist))
