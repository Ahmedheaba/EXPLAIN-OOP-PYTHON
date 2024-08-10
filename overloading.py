'''
IN PYTHON, WE CAN COMBINE TWO PAIRS OF THE SAME TYPE, NUMBERS WITH NUMBERS OR LETTERS WITH LETTERS,
BUT IF YOU TRY TO COMBINE OBJECT + OBJECT WILL BE ERROR

HERE COMES A OVERLOADING WHEN YOU NEED TO CHANGE THE BEHAVIOR 
WHEN YOU NEED TO CHANGE THE LANGUAGE ITSELF
'''

class Vector:  
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #THIS MAGIC METHOD TO CHANGE THE STRING IT WILL RETURN FROM CLASS
    def __str__(self):
        return f'VECTOR({self.a} {self.b})'
    
    def __add__(self, others):
        return Vector(self.a + others.a, self.b + others.b)

#FIRST OBJECT 
objOne = Vector(20, 15)
#SECOND OBJECT 
objTwo = Vector(10, 12)
#THIRD OBJECT 
objThree = Vector(10, 5)
print(objOne)
print(objTwo)
#HERE WE NEED TO ADD THEREE OBJECT 
print(objOne+objTwo+objThree)



