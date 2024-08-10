'''
Overriding is when a child class creates a new implementation of an inherited method.
When a child class method is created with the same name and signature
 as one in the parent, the child’s method takes precedence.

'''

'''
WHEN YOU HAVE TWO CLASSES AND INSIDE CLASS ONE WE HAVE METHOD (myMethod)
AND IN CLASS TWO WE HAVE THE SAME METHOD NAME (myMethod) BUT WITH DIFRRRENT SIGNATURE

'''

'''
IN METHOD OVERRIDING, THE CHILD CLASS CAN CHANGE ITS FUNCTIONS THAT 
ARE DEFINED BY ITS ANCESTRAL CLASSES. IN OTHER WORDS,
THE CHILD CLASS HAS ACCESS TO THE PROPERTIES AND FUNCTIONS OF THE PARENT CLASS
METHOD WHILE ALSO EXTENDING ADDITIONAL FUNCTIONS OF ITS OWN TO THE METHOD.
IF A METHOD IN A SUPERCLASS COINCIDES WITH THAT OF A SUBCLASS,
THEN THE SUBCLASS IS SAID TO OVERRIDE THE SUPERCLASS.
'''
class Pernt:
    #FIRST METHOD IN THIS CLASS 
    def printThing(self):
        print('THIS WILL BE PRINT FROM PARENT CLASS')

class Child(Pernt):
    #AS YOU SEE THIS METHOD HAS THE SAME NAME 
    #BUT THIS METHOD DO SOMETHING ELSE
    def printThing(self):
        return True
        # return super().printThing()

#FIRST OBJECT FROM CHILD CLASS     
x = Child()
print(x.printThing())  #True

#FIRST OBJECT FROM PERNT CLASS 
y = Pernt()
y.printThing() #THIS WILL BE PRINT FROM PARENT CLASS

