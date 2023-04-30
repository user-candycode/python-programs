class Employee:
    company = "Google"

    def showDetails(self):
        print("this is an employee")


class Programer(Employee):
    language= "Python"
    def getLanguage(self):
        print(f"the language is {self.Language}")

    def showDetails(self):
        print("This is a programer")

e = Employee()
e.showDetails()
p = Programer()
p.showDetails()

print(p.company)