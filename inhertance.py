#INHERTANCE

class Parent:
    parentAttr = 0 #CLASS VARIABLE
    def __init__(self, id, name, age): 
        self.id = id  #INSTANCE VARIABLR
        self.name = name #INSTANCE VARIABLR
        self.age = age #INSTANCE VARIABLR
        print('HELLO FROM PARENT CLASS') #HELLO FROM PARENT CLASS -- WILL BE PRINT FIRST
    
    def parentMethod(self):
        print('CALLING PARENT METHOD')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
        # print(f'parentAttr: {attr}')
    
    def getAttr(self):
        print(f'{Parent.parentAttr}')

'''
SCOEND CLASS INHERT FROM PARENR CLASS.
CLASS CHILD CAN INHERT EVERYTHING IN PERANRT CLASS.
'''
class child(Parent):
    def __init__(self, id, name, age, email):
        #super() => used to give access to methods and properties of a parent or sibling class
        super().__init__(id, name, age)
        self.email = email

    def childMethod(self):
        print('CALLING CHILD METHOD')


x = Parent(1, 'AHMED HEABA', 26)
print(x.parentAttr) #0
x.parentMethod() #HELLO FROM PARENT CLASS
x.setAttr(215)  #215 BUT NOT PRINT IN THE CONSOLE
x.getAttr() #215

y = child(1, 'AHMED HEABA', 26, 'ahmedheaba1911@gmail.com')
y.childMethod() #CALLING CHILD METHOD
y.parentMethod() #CALLING PARENT METHOD
y.setAttr(15)
y.getAttr()