#tuples are immutable lists
my_tuple = (1, 2, 2, 4, 5, "Hello", [1, 2, 3], (4, 5, 6))
print(my_tuple[0]) #accessing elements
print(my_tuple[1:4]) #slicing
print(my_tuple[5:]) #slicing
#my_tuple[0] = 10 #this will raise an error because tuples are immutable we cant change its elements as we do in lists