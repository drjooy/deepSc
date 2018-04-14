
class Man:
    def __init__(self,name):
        self.name = name
        print("initialized!")

    def hello(self):
        print("Hello"+self.name+"!")

    def goodbye(self):
        print("Good-bye"+self.name+"!")
m = Man("David")
m.hello()
m.goodbye()



#broadcast
import numpy as np
x = np.array([1.0,2.0,3.0])
print(x)

A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A*B)