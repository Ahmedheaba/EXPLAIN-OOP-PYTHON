class Robot:
    __count = 0
    def __init__(self) -> None:
        Robot.__count += 1

    def robotInstance(self):
        return Robot.__count
    
# Robot.robotInstance()#TypeError: Robot.robotInstance() missing 1 required positional argument: 'self'
x = Robot()
print(x.robotInstance())#1
y = Robot()
print(y.robotInstance())#2