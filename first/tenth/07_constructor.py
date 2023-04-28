class Employee:
    company="Google"

    def __init__(self, name, salary, subunit):
        self.name=name
        self.salary=int(salary)
        self.subunit=subunit
        print("Employee is created!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The name of the salary is {self.salary}")
        print(f"The name of the subunit is {self.subunit}")


    def getSalary(self, signature):
        print(f"The salary of this employee working for {self.company} is {self.salary}. \nSIGN:\"{signature}\"")
    
    @staticmethod #use this  if not using self in class functions
    #the above is a decorator to mark that below this are static methods
    def greet():
        print("good morning! Salute Salamat Namaste")

    @staticmethod
    def time():
        print(f"The time is something idk")


object_variable=Employee("Harry",100,"YouTube")

object_variable.getDetails()