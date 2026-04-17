# Inheritance models an IS-A relationship and reuses behavior via subclassing. Composition models a HAS-A relationship by delegating work to contained objects. Inheritance is rigid and tightly coupled, while composition is flexible, safer, and easier to extend. That’s why modern Python design prefers composition over inheritance.
class baseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"preparing chai of type: {self.type}")

# inheritence adding base class inside () 
class MasalaChai(baseChai):
    def add_spices(self):
        print(f"adding cardamom ginger and clove in {self.type}")

class chaiShop:
    chai_cls = baseChai # keep references not call it. call composition.

    def __init__(self):
        self.chai = self.chai_cls("RegularChai")

    def serve(self):
        print(f"serving {self.chai.type} chai in shop")

# inheritence and composition together
class fancyChaiShop(chaiShop):
    chai_cls = baseChai


# inheritence
user1_order = MasalaChai("masalaChai")
user1_order.prepare()
user1_order.add_spices()

# composition
user2_order = chaiShop()
user2_order.chai.type = "LemonTea"
user2_order.chai.prepare()
user2_order.serve()

# inheritence and composition together
user3_order = fancyChaiShop()
user3_order.chai.type = "GingerTea" # we used user3_order.chai_cls = baseChai so it will create baseChai object as fancyChaiShop doesnot have its own constructor it will call parent constructor which will create baseChai object.
user3_order.chai.prepare()



