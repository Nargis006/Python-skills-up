list_tea = ["Normal tea","Black tea","Leamon TEa","Masala Cahi"]


# [expression for expression in List if condition in expression]
masala_chai = [masala_tea for masala_tea in list_tea if "Masala" in masala_tea]

print(masala_chai)