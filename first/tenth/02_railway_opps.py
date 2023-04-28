class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")



mrk_application= RailwayForm()
mrk_application.name="K"
mrk_application.train="Rajhdhani Express"
mrk_application.printData()