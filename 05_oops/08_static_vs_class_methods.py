#class has only one constructor and we want to have multiple ways to create object we can use class methods or static methods.
# static methods don't take self or cls as first parameter and they can't access class or object level properties directly.
# they are utility functions that are related to class but don't need class or object context.

class chaiUtils:
    def __init__(self, ingredients):
        self.ingredients = ingredients
# cls refers to class itself and we can access class level properties via cls it usually used to create alternative constructors.
    @classmethod
    def from_string(cls, ingredients_str):
        ingredients = [ingredient.strip().lower() for ingredient in ingredients_str.split(',')]
        return cls(ingredients)
    @classmethod
    def from_list(cls, ingredients_list):
        ingredients = [ingredient.strip().lower() for ingredient in ingredients_list]
        return cls(ingredients)
# static method example will not have self or cls as first parameter
    @staticmethod
    def clean_ingredients(ingredients):
        return [ingredient.strip().lower() for ingredient in ingredients]
    
# using class methods as alternative constructors call classname and method.
chai1 = chaiUtils.from_string(" Sugar , Tea , Milk ")
chai2 = chaiUtils.from_list([" Honey ", " Lemon ", " Ginger "])
print(chai1.ingredients)  # ['sugar', 'tea', 'milk']
print(chai2.ingredients)  # ['honey', 'lemon', 'ginger']
# using static method as utility function
clean_ingredient = chaiUtils.clean_ingredients([" Sugar ", " Tea ", " Milk "])  # ['sugar', 'tea', 'milk']
print(clean_ingredient)