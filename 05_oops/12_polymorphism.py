class Animal:
    def speak(self) -> str:
        return "Animal speaks"

class Dog(Animal):
    def speak(self) -> str:
        return "Dog barks"

class Cat(Animal):
    def speak(self) -> str:
        return "Cat meows"
    
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())
print(dog.speak())
print(cat.speak())

