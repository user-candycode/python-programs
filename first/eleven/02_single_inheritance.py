
#======================Class 1
class Person:
    country="india"

    def takeBreath(self):
        print("I am breathing...")


#======================Class 2
class Employee(Person):
    company="honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("i am an employee so i am luckily breathing...")


#=====================Class 3
class Programmer(Employee):
    company="Fiver"

    def getSalary(self):
        super().takeBreath()
        print(f"No salary to programers")

p=Person()
p.takeBreath()
e=Employee()
e.takeBreath()
pr=Programmer()
pr.takeBreath()
print(pr.country)

pr.getSalary()