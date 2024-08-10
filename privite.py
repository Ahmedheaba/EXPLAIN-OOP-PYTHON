#DATA HIDING
class JustCounter:
    __secretCount = 0 #THIS IS PRIVATE CLASS VARIABLE
    
    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

count = JustCounter()
count.count() #1
#print(JustCounter.secretCount)#AttributeError: type object 'JustCounter' has no attribute '__secretCount'
#print(JustCounter.__secretCount)#AttributeError: type object 'JustCounter' has no attribute '__secretCount'
#print(count.__secretCount)#AttributeError: 'JustCounter' object has no attribute '__secretCount'

'''
ALL THREE WAYS HAS ERROR BECAUSE (__secretCount) IS PRIVATE CLASS VARIABLE
PRIVATE CLASS VARIABLE CAN ACSESS FROM INSIDE CLASS 
PRIVATE CLASS VARIABLE CAN NOT ACSESS FROM OUTSIDE CLASS
'''
#IF YOU NEED TO ACSESS PRIVATE CLASS VARIABLE FROM OUTSIDE CLASS
#YES YOU CAN ACSESS PRIVATE CLASS VARIABLE FROM OUTSIDE CLASS
#THIS IS SPECHIAL WAY TO ACSESS PRIVATE CLASS VARIABLE FROM OUTSIDE CLASS
'''
OBJECT._CLASSNAME__VARIABLE NAMR
'''
print(count._JustCounter__secretCount)








class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printData(self):
        print(f'HELLO {self.fname} {self.lname}')

class Child(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    
    def printData(self):
        print(f'HELLO {self.fname} {self.lname} AND YOUUR YEAR IS{self.year}')

    
p1 = Child('AHMED', 'HEABA', 2025)
p2 = Person('FARIDA', 'AHMED')       
p1.printData()
p2.printData()