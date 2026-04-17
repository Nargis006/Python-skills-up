class chaiUtils:
    @staticmethod
    def clean_ingredients(ingredients):
        return [ingredient.strip().lower() for ingredient in ingredients]
    
clean_ingredient = chaiUtils.clean_ingredients([" Sugar ", " Tea ", " Milk "])  # ['sugar', 'tea', 'milk']

print(clean_ingredient)