'''
Python uses a mechanism known as Method Resolution Order (MRO) 
to manage multiple inheritance,
which establishes the order in which classes are searched for a method or attribute.
The “mro()” method and the “.__mro__” attribute both return the MRO,
which is determined using the C3 linearization algorithm.


url:https://www.upgrad.com/tutorials/software-engineering/python-tutorial/multiple-inheritance-in-python/
'''

'''
WHEN YOU NEED TO INHERT FROM MORE CLASS YOU 
EX:
“Animal” is the base class, representing generic animal behavior.
“Dog” and “Cat” are subclasses of “Animal”, representing specific animal types.
“Pet” inherits from both “Dog” and “Cat”, showcasing multiple inheritances. It effectively combines the behaviors of both “Dog” and “Cat”.

'''
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def showNameAndType(self):
        return f'THE NAME IS : {self.name} AND THE TYPE IS: {self.type}'
    
class Cat(Animal):
    def __init__(self, name, type, age):
        super().__init__(name, type)
        self.age = age
    
    def calcAgePerDays(self):
        return f'THE AGE IS: {self.age * 365} DAYS!'

class Dog(Animal):
    def showMessage(self):
        return f'THE DOG IS THE PERSON FRIND'

#THIS CLASS INHERT FROM TWO CLASS AS THE SAME TIME (CAT AND DOG)
class Pet(Cat, Dog):
    def __init__(self, name, type, age, owner):
        super().__init__(name, type, age)
        self.owner = owner

    def getAllData(self):
        return f'THIS {self.name} FROM TYPE {self.type} AND IT IS AGE IS: {self.calcAgePerDays()} AND IS IS OWNER IS: {self.owner}'
    
animalOne = Animal('MICHO', 'GARD')
print(animalOne.showNameAndType())

#THIS IS OBJECT FROM PET CLASS AND AS YOU KNOW THIS CLASS ANHERT FROM CAT AND DOG
animalTwo = Pet('KOKO', 'DOLPHIN', 12, 'AHMED HEABA')
print(animalTwo.getAllData())
print(animalTwo.calcAgePerDays())
print(animalTwo.showMessage())

