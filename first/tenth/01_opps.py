'''
    OLD way of doing it procedurally without class
        a=12
        b=43
    print("sum of a and b is", a+b)
'''

#new way of writing same logic using class
class Number:
    def sum(self):
        return self.a + self.b

num=Number()
num.a=12
num.b=12

s=num.sum()
print(s)

