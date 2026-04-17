# we can call base class constructor using super() method or by directly calling base class constructor or by code duplication but code duplication is not a good practice.

class baseChai:
    def __init__(self, type_, strong):
        self.type = type_
        self.strong = strong
    
    def prepare(self):
        print(f"preparing chai of type: {self.type} and strength: {self.strong}")

class MasalaChai(baseChai):
# Method 1: using super()
    # def __init__(self, type_, strong, spices):
    #     self.type = type_
    #     self.strong = strong
    #     self.spices = spices

# Method 2: direct base class constructor
    # def __init__(self, type_, strong, spices):
    #     baseChai.__init__(self, type_, strong)
    #     self.spices = spices

# Method 3: calling super class constructor
    def __init__(self, type_, strong, spices):
        super().__init__(type_, strong)
        self.spices = spices
