class TeaLeaf:
    def __init__(self, age):
        self._age = age  # private attribute with underscore like getter setter in c#

    @property
    def age(self):
        return self._age + 2  # we can add some logic here its also possible to make read only property by not defining setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
        
tea_leaf = TeaLeaf(5)
print(tea_leaf.age)  # prints 7
try:
    tea_leaf.age = -10
except ValueError as e:
    print(e)  # prints Age cannot be negative