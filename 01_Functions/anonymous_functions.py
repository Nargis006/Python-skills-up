chat_types = ["Kadak", "Ginger","Leamon","Kadak"]


#use lambda function when logic is one liner
strong_chai = list(filter(lambda chai: chai == "Kadak", chat_types))
print(strong_chai)

user_detail = [("Nargis", 4, "Hyderabad"),
               ("Ajaz", 5, "Riyadh"),
               ("Tabassum", 1, "Nuamundi"),
               ("Tarannum", 2, "Tata"),
               ("Anjum", 3, "JSR")]

sorted_user = sorted(user_detail, key= lambda x:x[1])
print(sorted_user)

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)