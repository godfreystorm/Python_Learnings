# This operator := allows for assignment during print statements.
food = True
print(food)

# Can also be written as
print(food := True)

# Better example
foods = list()
while True:
    food = input('What is your favourite meal? ')
    if food == "done":
        break


# Can also be written as
foods = list()
while foods := input('What is your favourite meal? ') != "done":
    foods.append(food)