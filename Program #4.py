class Employee:
    def __init__(self, name, id, department, job):
        self.name = name
        self.id = id
        self.department = department
        self.job = job
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job}")
        print()
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
employee1.display_info()
employee2.display_info()
employee3.display_info()
