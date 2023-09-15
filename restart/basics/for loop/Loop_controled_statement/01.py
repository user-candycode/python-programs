#continue
#break
#pass

print("Entering name and breaking")
while True:
	name = input("Enter your name: ")
	if name != "":
		break

print("Phone Number")
phone_number = "123-456-7890"

for i in phone_number:
	if i == "-":
		continue
	print(i,end="")

print("")
print("Printing a sequence except 13")
for i in range(1,21):
	if i == 13:
		pass
	else:
		print(i)
