'''
IN PYTHON YOU HAVE PRIVITE VARIABLE AND YOU CAN NOT USE THIS VARIABLE OUT OF CLASS
WHEN YOU NEED TO READ THIS VARIABLE YOU CAN USE GETTER AND SETTER
'''

#THIS IS OLD WAY BY PYTHONIC WAY
class ITI:
    def __init__(self, age=0) -> None:
        #AS YOU KNOW AGE HERE IS PRIVATE VAR
        self.__age = age

    def getAge(self):
        print('getAge called')
        return self.__age
    
    def setAge(self, x):
        print('setAge called')
        self.__age = x

    def delAge(self):
        del self.__age
    #THIS IS PYHONIC WAY TO MAKE PRIVITE VARIABLE IS BUBLIC    
    age = property(getAge, setAge, delAge)
p = ITI()
print(p.age)
p.delAge()
print(p.age)
# print(p.__age)#AttributeError: 'ITI' object has no attribute '__age'

#THIS IS NEW WAY BY PYTHONIC WAY
class ITI:
    def __init__(self, age=0) -> None:
        #AS YOU KNOW AGE HERE IS PRIVATE VAR
        self.__age = age
    @property
    def age(self):
        print('getAge called')
        return self.__age
    @age.setter
    def age(self, x):
        print('setAge called')
        self.__age = x
    @age.deleter
    def age(self):
        del self.__age
p = ITI()
print(p.age)
