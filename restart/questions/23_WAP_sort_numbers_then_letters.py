# WAP to sort characters and numbers so that numbers_then_letters

input1 = "A7B1R3"

alpha = list()
num = list()

for ch in input1:
    if ch.isalpha():
        alpha.append(ch)
    else:
        num.append(ch)

alpha.sort()
num.sort()

print(alpha)
print(num)
output = alpha+num

print("".join(output))
