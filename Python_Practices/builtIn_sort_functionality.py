# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
# students.sort(key=age)                                       # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)

# To betetr understand the lambda function
mylist = [(3, 5, 8), (6, 2, 8), ( 2, 9, 4), (6, 8, 5)]
print(sorted(mylist, key=lambda x: x[1]))