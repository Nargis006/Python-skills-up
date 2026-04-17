# set can have only immutable elements and they are unordered collections of unique elements
my_set = {1, 2, 3, 4, 5, "Hello", (1, 2, 3)}
print(my_set)
# set cant create duplicates and they are mutable no ordered collection of unique elements
duplicate_set = {1, 2, 2, 3, 4, 5}
print(duplicate_set) #it will print {1, 2, 3, 4, 5} because set will remove duplicates
my_set.add(6) #adding element to set
print(my_set)

# to create an empty set we have to use set() function because {} creates an empty dictionary
empty_set = set()
print(type(empty_set)) #it will print <class 'set'> because we have created an empty set using set() function
#clear method is used to remove all elements from the set
my_set.clear()
#pop method is used to remove a random element from the set
my_set.pop()
# union method is used to combine two sets and it returns a new set with all unique elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) #it will print {1, 2, 3, 4, 5} because it will combine both sets and remove duplicates
# intersection method is used to find common elements between two sets and it returns a new set with common elements
intersection_set = set1.intersection(set2)
print(intersection_set) #it will print {3} because it is the only common element between both sets
# difference method is used to find elements that are present in one set but not in another set and it returns a new set with those elements
difference_set = set1.difference(set2)
print(difference_set) #it will print {1, 2} because these elements are present in set1 but not in set2