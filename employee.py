from functions import employee


class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position)

employee1 = Employee("Mark","CEO",250000)
print(employee1.name,employee1.position,employee1.salary)

employee2 = Employee("Marlon","HR",120000)
print(employee2.name,employee2.position,employee2.salary)

employee3 = Employee("Rebbecca","Manager",300000)
print(employee3.name,employee3.position,employee3.salary)

employee4 = Employee("Ian","Secretary",50000)
print(employee4.name,employee4.position,employee4.salary)

