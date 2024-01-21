# If it walks like a duck and talks like a duck then it must be a duck.
# I can pass chicken even tho the person function only works with duck because they have the same walk and talk methods.
# If I changed the chicken function and removed the walk method then the duck typing would not work.
class Duck:
    def walk(self):
        print('The duck is walking')

    def talk(self):
        print('The duck is quacking')


class Chicken:
    def walk(self):
        print('The chicken is walking')

    def talk(self):
        print('The chicken is clucking')


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('You caught the critter')


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
