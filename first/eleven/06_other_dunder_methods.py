class Number:
    def __init__(self, num):  # dunder method
        self.num = num

    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return 22

n=Number(9)
print(n)

print(len(n))

