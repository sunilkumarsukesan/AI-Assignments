class Employee:

    def __init__(self, name, experience_years):
        self.name = name
        self.experience_years = experience_years

class Experience(Employee):

    def __init__(self,name, experience_years):
        super().__init__(name,experience_years)

    def show_details(self):
        print(f"{self.name} {self.experience_years}")


class Profession(Experience):

    def __init__(self,name, experience_years, profession_years):
        super().__init__(name,experience_years)
        self.profession_years = profession_years

    def show_details(self):
        print(f"{self.name} {self.experience_years} {self.profession_years}")

E1 = Profession("Sunil", "Test" , "10")
E1.show_details()