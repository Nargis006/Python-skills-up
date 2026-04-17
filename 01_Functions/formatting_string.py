a = 10
b = 20
# Using f-string for formatting
result = f"The sum of {a} and {b} is {a + b}"
print(result)

# Using format() method for formatting
result = "The sum of {} and {} is {}".format(a, b, a + b)
print(result)
# Using % operator for formatting
result = "The sum of %d and %d is %d" % (a, b, a + b)
print(result)
#using concatenation for formatting
result = "The sum of " + str(a) + " and " + str(b) + " is " + str(a + b)
print(result)
# Using f-string for formatting with expressions
result = f"The sum of {a} and {b} is {a + b}"
print(result)

# use indexing for formatting
print("The sum of {0} and {1} is {2}".format(a, b, a + b))
