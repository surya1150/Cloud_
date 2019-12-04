from threading import *
class Mythread(Thread):
    def run(self):
        for i in range(1,11):
            print("Child- Thread")
t = Mythread()
t.start()
for i in range(10):
    print("Main Thread")