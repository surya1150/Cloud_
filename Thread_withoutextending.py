from threading import *
class Thread_Test:
    def display(self):
        for i in range(1,11):
            print("Child Thread")
obj = Thread_Test()
t = Thread(target=obj.display)
t.start()

for i in range(1,5):
    print("Main - Thread")