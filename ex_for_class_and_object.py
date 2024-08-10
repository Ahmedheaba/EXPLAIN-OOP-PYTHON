'''
THIS IS CALLED (DOCument STRING) => IF YOU NEEED TO EXPLAIN WHAT IS THIS CLASS DO 
'''
class Empolyee:
    '''
    COMMON BASE CLASS FOR ALL EMPLOYEE
    '''
    #CLASS VARIABLE RELATEED BY CLASS
    '''
    ANY OBJECT WILL CREATED FROM EMPLOYEE CLASS WILL SHARED WITH IT (empCount).
    '''
    empCount = 0 #CLASS VARIABLE

    #CONSTRACTOR init=> initiate
    def __init__(self, fName, lName, age, salary):
        self.fName = fName   #INSTANCE VARIABLR
        self.lName = lName   #INSTANCE VARIABLR
        self.age = age      #INSTANCE VARIABLR
        self.salary = salary #INSTANCE VARIABLR
#THIS IS EXPLAIN WHAT HAPPEN UNDER THE HOD IN MEMORY
    #+-------|--------+|--------+|--------+
    #|  fNAME | lNAME  |   AGE   |  SALARY +
    #   2X27  | 2X28   |   2X29  |  2X30   +
    #+-------|--------+|--------+|--------+

    #init will be excute Atomaticlly when you make object
    def displayFullNme(self):
        return f'{self.fName} {self.lName}'
    #ANY METHOD SHOULD FIRST PARAMETER IS (self) 
    def sayHello(self):
        return f'HELLO {self.displayFullNme()}'
    
#first object
#FIRST ARGUMENT IN THE OBJECT ALWAYS IS SELF BY DEFULT
#empOne = Empolyee(self, 'AHMED', 'HEABA', 26, 15000)
empOne = Empolyee('AHMED', 'HEABA', 26, 15000)
#YOU CAN ADD ANY PROBARTY TO THE OBJECT AFTER CREATE IT
empOne.hasCar = True
#THIS IS EXPLAIN WHAT HAPPEN UNDER THE HOD IN MEMORY
    #+-------|--------+|--------+|--------+-----------+
    #|  fNAME | lNAME  |   AGE   |  SALARY +  HASCAR  +   INSTANCE VARIABLE
    #   2X27  | 2X28   |   2X29  |  2X30   +  2X31    +   ADRESS OF MEMORY
    #+-------|--------+|--------+|--------+-----------+
print(empOne.hasCar)
print(empOne.displayFullNme())
print(empOne.sayHello())

#FINALLY YOU CAN DELETE ANT ANSTANCE VARIABLE

del empOne.hasCar
#THIS IS EXPLAIN WHAT HAPPEN UNDER THE HOD IN MEMORY
    #+-------|--------+|--------+|--------+-+
    #|  fNAME | lNAME  |   AGE   |  SALARY +   INSTANCE VARIABLE
    #   2X27  | 2X28   |   2X29  |  2X30   +   ADRESS OF MEMORY
    #+-------|--------+|--------+|--------+

#print(empOne.hasCar)    #AttributeError: 'Empolyee' object has no attribute 'hasCar'