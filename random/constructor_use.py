#!/bin/python3
class PartyAnimal:
    x=0
    name = ''
    def __init__(self, name):
        self.name = name
        print(self.name,'constructor\n')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

    def __del__(self):
        print("i am destructor",self.x)

obj1 = PartyAnimal('Quincy')
obj2 = PartyAnimal('Miya')

obj1.party()
obj2.party()
obj1.party()

obj3 = PartyAnimal('MrK')
