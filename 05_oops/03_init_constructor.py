class ChaiOrder:
    # create a constructor no need to define variable on top like in c# we do python will understand a create a variable with same name as constructor param.
    # add extra '_' if its python key
    def __init__(self, type_, order):
        self.type = type_
        self.order = order

    def summary(self):
        print(f"selected chai type {self.type} with nuumner {self.order}")

chai_order1 = ChaiOrder("Ginger", 200)
chai_order2 = ChaiOrder("Lemon", 220)

chai_order1.summary()
chai_order2.summary()


