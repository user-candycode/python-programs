# salary after increment = salary * increment

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        print("orignal")
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary
        print("mod")

e=Employee()
#print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement=2000
print(e.increment)
print(e.salaryAfterIncrement)
