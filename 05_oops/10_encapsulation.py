#there is a concept of private, protected and public in python but it is not like other programming languages
#in python we can access private members of a class but it is not recommended
#encapsulation is the process of hiding the internal details of an object and only exposing the necessary details to the outside world
class Employee:
    def __init__(self, name, age, salary):
        self.name = name #public member
        self._age = age #protected member
        self.__salary = salary #private member

    def display(self):
        print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

    # use getter and setter to access private member
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

emplyee = Employee("John", 30, 50000);
emplyee.display() # Name: John, Age: 30, Salary: 50000
print(emplyee.name) # John
print(emplyee._age) # 30 (not recommended to access protected member)
print(emplyee.get_salary()) # 50000
emplyee.set_salary(60000)
print(emplyee.get_salary()) # 60000