class Programer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product
        print("Programer details class for", self.name)

    def programer_Details(self):
        print(
            f"The name of the programer is {self.name} and this employee works on product {self.product}")


harry = Programer("harry", "Skype")
harry.programer_Details()
print("")
Alka = Programer("Alka", "GitHub")
Alka.programer_Details()
