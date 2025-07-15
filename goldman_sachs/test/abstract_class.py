from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Engineer(Employee):
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def calculate_salary(self):
        return self.base + self.bonus
    
class Manager(Employee):
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def calculate_salary(self):
        return self.base + self.bonus + 0.1 * self.base