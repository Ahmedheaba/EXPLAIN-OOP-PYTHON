'''
IN OOP CLASS GIVE YOU ALOT OF METHOD TO HELP YOU 
1: getattr
2: hasattr
3: setattr
4: delattr
'''

class CarFactor:
    TITLE: 'BMW'  #CLASS VARIABLE
    def __init__(self, engine, color):
        self.engine = engine #INSTANCE VARIABLR
        self.color = color #INSTANCE VARIABLR

    def hasAllData(self): #CLASS METHOD
        return f'THIS CAR HAS ENGINE: {self.engine} AND IT COLOR IS: {self.color}'

#OBJECT OR INSTANCE FROM CLASS CARFACTOR
carOne = CarFactor('2x359', 'black')
print(carOne.hasAllData()) #THIS CAR HAS ENGINE: 2x359 AND IT COLOR IS: black
#hasattr
'''
hasattr(object, value you need to cheack if exist or not)
'''
bool1 = hasattr(carOne, 'age')
bool2 = hasattr(carOne, 'engine')
print(bool1)# False
print(bool2)#True

'''
serattr(obj: object, name: str, value: Any Value)
'''
setattr(carOne, 'year', 2024)
bool3 = hasattr(carOne, 'year')
print(bool3)
print(carOne.year)

'''
getattr(o: object, name: str)
'''
print(getattr(carOne, 'year'))

'''
delattr(obj: object, name: str)
'''
delattr(carOne, 'year')
print(carOne.year)#AttributeError: 'CarFactor' object has no attribute 'year'



'''
THERE ARE MANY MAGIC METHODS ALSO HELP YOU SUCH AS
__doc__ : GET CLASS DOCUMENTATION STRINR
__name__: GET CLASS NAME
__dict__: GET DITIONARY CONTAINIG THE CLASS (namespace in the class)
''' 