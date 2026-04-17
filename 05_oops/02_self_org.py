#self will hold reference of all the properties of class

class Chai:
    chai_type = "ginger"
    # call it method not function if its inside class 
    def prepare_tea(self):
        print(self.chai_type)

chai_obj1 = Chai()
chai_obj2 = Chai()
chai_obj2.chai_type = "Lemon"

# python by default if nothing is return returns None. like 
# def f():
#   pass
#print(chai_obj1.prepare_tea()) # return None

chai_obj1.prepare_tea() # prints ginger
# when calling via class we need to mention which object to point so pass object is self
Chai.prepare_tea(chai_obj1) # prints ginger
Chai.prepare_tea(chai_obj2) # prints lemon
        