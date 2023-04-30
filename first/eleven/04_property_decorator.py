class Employee:
    company="Bharat Gas"
    salary= 5600
    salary_bonus=500
    # total_salary=6100

    @property #getter
    def totalSalary(self):
        return self.salary+self.salary_bonus 
    
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val - self.salary

e=Employee()
print(e.totalSalary) #totalSalary is not a function now so no need to call it as totalSalary() here () are not needed for @property
