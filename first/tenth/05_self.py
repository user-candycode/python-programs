class Employee:
    company="Google"
    def getSalary(self):
        print(f"sallary for this employee working in {self.company} is {self.sallary}")

harry=Employee()
harry.sallary=15343
harry.getSalary() # Employee.getSalary(harry) # or the above harry converts to an argument to a class

