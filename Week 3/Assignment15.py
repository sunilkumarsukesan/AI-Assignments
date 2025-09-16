class Employee:

    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        print(f"Employee details : \nName : {self.name}\nEmployee ID : {self.emp_id}\nDeparment : {self.department}\n")


class Manager(Employee):

    def __init__(self, name, emp_id, department , team_size : int):
        super().__init__(name, emp_id, department)
        if isinstance(team_size, int):
            self.team_size = team_size
        else:
            raise ValueError("team_size must be an integer")

    def display_info(self):
        print(f"***** Employee details ***** \nName : {self.name}\nEmployee ID : {self.emp_id}\nDeparment : {self.department}\nTeam_size : {self.team_size}\n")


class Developer(Employee):

    def __init__(self, name, emp_id, department , programming_language  : str):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        print(f"***** Employee details ***** \nName : {self.name}\nEmployee ID : {self.emp_id}\nDeparment : {self.department}\nProgramming_language : {self.programming_language}\n")


if __name__ == "__main__":
    manager = Manager("Sunil", "1", "QA", 8)
    manager.display_info()
    dev = Developer("Sunil", "1", "QA", "Java")
    dev.display_info()