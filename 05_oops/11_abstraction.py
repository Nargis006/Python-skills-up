from abc import ABC, abstractmethod
from typing import final

class Emploee(ABC):
    @final
    def calculate_salary(self, salary, percentageDeduction) -> int:
        return self.get_basic_salary(salary) - self.get_deduction(salary, percentageDeduction)
    
    @abstractmethod
    def get_basic_salary(self, salary) -> int:
            pass

    @abstractmethod
    def get_deduction(self,salary, percentageDeduction) -> int:
            pass    

    def salary_credit_date(self):
        print("Salary will be credited on 1st of every month")

class FullTimeEmployee(Emploee):
    def get_basic_salary(self, salary) -> int:
        return salary

    def get_deduction(self, salary, percentageDeduction) -> int:
        return int(salary * (percentageDeduction / 100))

    def salary_credit_date(self):
        print("Salary will be credited on 30th of every month for full-time employee")

nargis = FullTimeEmployee()
nargis.salary_credit_date() # Salary will be credited on 30th of every month for full-time employee
print("Salary credited:", nargis.calculate_salary(5000, 10)) # Calculating salary for full-time employee
