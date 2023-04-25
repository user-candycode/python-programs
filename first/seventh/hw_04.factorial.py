#WAR to find a factorial of a number
a=int(input("Enter a number:\n"))
fact=int(1)
for i in range(1,a+1):
    fact=fact*i
    print(fact)

print("\nFinally the factorial value of",a,"is",fact)