class Employee:
    company="Google"

    def getSalary(self, signature):
        print(f"The salary of this employee working for {self.company} is {self.salary}. \nSIGN:\"{signature}\"")
    
    @staticmethod #use this  if not using self in class functions
    #the above is a decorator to mark that below this are static methods
    def greet():
        print("good morning! Salute Salamat Namaste")

    @staticmethod
    def time():
        print(f"The time is something idk")

harryObject=Employee()
harryObject.salary="100K"

harryObject.getSalary("MrHarry")
harryObject.greet()
harryObject.time()


