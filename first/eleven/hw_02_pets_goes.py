class Animal:
    animal_type="Mammal"
    pass

class Pets(Animal):
    color="white"

class Dog(Pets):
    @staticmethod
    def __str__():
        return f"Dog ran "
    @staticmethod
    def bark():
        print("woff")


d=Dog()
d.bark()
print(d)