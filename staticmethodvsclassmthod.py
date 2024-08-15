class Pet:
    _classInfo = 'Pet Animals'
    def about(self):
        print(f'THIS CLASS IS ABOUT {self._classInfo} ')

class Dog(Pet):
    _classInfo = 'MAN BEST FRIND'

class Cat(Pet):
    _classInfo = 'ALL KIND OF CATS'

x = Pet()
x.about()#THIS CLASS IS ABOUT Pet Animals 

y = Dog()
y.about()#THIS CLASS IS ABOUT Pet Animals 

z = Cat()
z.about()#THIS CLASS IS ABOUT ALL KIND OF CATS.


'''
THIS WAY WILL BE RUN AND THE RESULT WILL CORRECT
BUT THE CODE NOT WILL PREFECT 
CODE IS BAD
'''

#WITH STATIC METHOD

'''
STATIC METHOD CANT ACCESS ON BASE CLASS
IF YOU HAVE CLASS VARIBLE AND IT IS CALLED CLASS INFO
AND YOU INHIRT FROM THIS CLSAA TO ANOTHER CLASSES
IN ANOTHER CLASSES YOU HAVE THE SAME CLASS VARIBLE BUT YOU MADE OVERRIDE ON IT
WHEN YOU NEED TO PRINT THE SAME METHOD ON THREE CLASSES THE SAME RESULT WILL PRINT
'''
class Pet:
    _classInfo = 'Pet Animals'
    @staticmethod
    def about():
        print(f'THIS CLASS IS ABOUT {Pet._classInfo} ')

class Dog(Pet):
    _classInfo = 'MAN BEST FRIND'

class Cat(Pet):
    _classInfo = 'ALL KIND OF CATS'

Pet.about() #THIS CLASS IS ABOUT Pet Animals 
Cat.about() #THIS CLASS IS ABOUT Pet Animals 
Dog.about() #THIS CLASS IS ABOUT Pet Animals 

'''
TO SLOVE THIS PROBLEM YOU CAN USE CLASSMETHOD
IN CLASS METHOD YOU HAVE (CLS)
THIS CLS REFERE TO CLASS NOT OBJECT
AND IN CLASSMETHOD YOU CAN ACCESS ON STATE OF CLASS
'''
class Pet:
    _classInfo = 'Pet Animals'
    @classmethod
    def about(cls):
        print(f'THIS CLASS IS ABOUT {cls._classInfo} ')

class Dog(Pet):
    _classInfo = 'MAN BEST FRIND'

class Cat(Pet):
    _classInfo = 'ALL KIND OF CATS'

Pet.about() #THIS CLASS IS ABOUT Pet Animals 
Cat.about() #THIS CLASS IS ABOUT ALL KIND OF CATS
Dog.about() #THIS CLASS IS ABOUT MAN BEST FRIND


#ANOTHER EXAMPLE

from datetime import date

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def fromBirthYear(cls, name, year):
        #return Person(date.today().year - year)
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18
perOne = Person('FARIDA', 18)
perTwo = Person.fromBirthYear('OMAR', 1998)

print(perOne.age)
print(perTwo.age)

print(Person.isAdult(22))
print(Person.isAdult(perOne.age))
print(Person.isAdult(perTwo.age))

