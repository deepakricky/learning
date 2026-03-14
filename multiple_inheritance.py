class Cricketer:
    name="Dhoni"
    role="WicketKeeper"
    def showinfo(self):
        print(f"Name is {self.name} and role is {self.role}")

class Team:
    team="Chennai"

class Stats(Cricketer,Team):
    runs= 57000
    def showstats(self):
        print(f"The cricketer {self.name} is a {self.role} and scored {self.runs} and he plays for {self.team}")

a=Stats()
a.showstats()
