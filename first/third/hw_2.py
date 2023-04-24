letter='''Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''

name=input("Enter your name\n")
date=input("Enter date\n")
print()
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)