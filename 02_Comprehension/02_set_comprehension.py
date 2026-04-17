chai_ingridents = {
    "Masala_Chai": ["Ginger","Cardamom","Clove","Sugar"],
    "Ginger_Tea": ["Ginger","Sugar","Tea"],
    "Normal tea": ["Sugar","Tea","Milk"],
}

chai_ingridents_in_Set = {"Ginger","Cardamom","Clove","Sugar","Ginger","Sugar","Tea","sugar","Tea","Milk"}

# set is use to get us unique values
unique_ingrdients = {ingredients for ingredients in chai_ingridents_in_Set}

# return unique vales
print(f"unique ingrdient from set", unique_ingrdients)

# we have a set of dicionary in chai_ingridents we have to find unique ingedients.
# {expression(alway final return value) for expression in List if condition in expression}
unique_ingredients_dictionary = {ingredient for unique_ingrdients in chai_ingridents.values() for ingredient in unique_ingrdients}

print(f"unique ingredient from dictionary",unique_ingredients_dictionary)