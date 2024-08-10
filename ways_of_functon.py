#WAY NUM 1 
def sumOne(num):
    return num + 1

addOne = sumOne
print(addOne(5))#6

#WAAY NUM 2 FUNCTION INSIDE FUNCTION
def plusOne(num):
    def addOne(num):
        return num + 1
    result = addOne(num)
    return result

print(plusOne(8))

#WAY NUM 3 PASS FUNCTION AS ARGUMENT
def sumTwo(num):
    return num + 2

def functionCall(f):
    addNum = 5
    return f(addNum)

print(functionCall(sumTwo))

#INSIDE FUNCTION CAN ACSESS ON OUTSIDE UFNCTION
def printMessage(message):
    def insideFunc():
        print(message)
    insideFunc()

printMessage('HELLO ITI ')