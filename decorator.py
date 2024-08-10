'''
HERE WILL BE EXPLAIN DECORATORS IN PYTHON
'''
#SIMPLE DECORATORS
#DECORATORS CAN ADD YOUR FUNCTION ONTIME WITOUT CHANGE IT STRUCTURE
#EX : IF YOU NEED TO MAKE FUNCTION TAKE FUNCTION AS ARGUMENT

def uppercaseDecorators(function):
    def wrapper():
        func = function()
        createUpeer = func.upper()
        return createUpeer
    return wrapper

#this is function just return simple string
def sayHi():
    return 'hello there'

#DOWN WE WILL NOT DO THIS STEP WITH DECORATOR
decOne = uppercaseDecorators(sayHi)
print(decOne())#HELLO THERE
print(sayHi())#hello there

#TILL NOW WE NOT DO ANY THING NEW ..
'''
HERE DECORATOR WILL COME 
'''
def uppercaseDecorators(function):
    def wrapper():
        func = function()
        createUpeer = func.upper()
        return createUpeer
    return wrapper

@uppercaseDecorators
def sayHi():
    return 'hello there'

print(sayHi())
