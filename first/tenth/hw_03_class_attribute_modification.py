class Sample:
    a="MrK"


obj=Sample()
obj.a="Vikky"

print("through object:\t\t",obj.a)
print("directly from class:\t",Sample.a)
#now mod directly in class
Sample.a = "Dikky"
print("Modified 'a' in sample:\t",Sample.a)
