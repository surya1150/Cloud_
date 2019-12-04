class Test:
    x = 30
    def __init__(self):
        self.y = 20
        self.z = 50

t1 = Test()
t2 = Test()
print("Before Updating Values:", t1.x,t1.y,t1.z)
t1.y= 100
Test.x = 40
print("After Update t1:", t1.x,t1.y,t1.z)
print("After Update t2:", t2.x,t2.y,t2.z)
