info = [("Allice", "Math"), ("Bob", "Science"), ("Charlie", "History"), ("David", "Math"), ("Eve", "Science")]
print(type(info)) #it will print <class 'list'> because we have created a list of tuples
unique_subjects = set() #creating an empty set to store unique subjects
for tup in info:
    print(tup[1]) #it will print each subject in the list of tuples
    unique_subjects.add(tup[1]) #adding subjects to the set

print(unique_subjects) #it will print the set of unique subjects

for name, subject in info:
    print(f"{name} is studying {subject}") #it will print the name and subject of 

    # list the students who are studying Math
    if subject == "Math":
        print(f"{name} is studying Math") #it will print the name of the student who is studying Math