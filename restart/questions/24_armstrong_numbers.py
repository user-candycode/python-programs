import os
import platform
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

# WAP to print armstrong numbers between 1 to 1000

# input1 = int(input("enter a number between 1 to 1000: "))
# input_str = str(input1)

# digits = list()
# for i in input_str:
#     digits.append(i)

# out = 0
# for i in digits:
#     out += int(i)**(len(input_str))

# if input1 == out:
#     print("Its an armstrong number")
# else:
#     print("Its not an armstrong number")

print("Armstrong Number between 1 to 1000: ")
for i in range(1,10001):
    n = len(str(i))
    digits = str(i)
    out = 0
    for j in digits:
      out += int(j)**n
    if int(digits) == int(out):
        print(f"{digits} an armstrong number")


# Using while loop
print("\nUsing while loop: ")
for x in range(1,1001):
    num = x
    sum1=0
    n=len(str(num))
    while (num != 0):
        digit = int(num%10)
        sum1 = (sum1 + int(digit**n))
        num=int(num//10)
    if int(sum1)==int(x):
        print(f"{x} is an Armstrong number")