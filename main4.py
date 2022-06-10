# if we create class with inheriting Thread class then we canno create construnctor in its constructor in it 

from threading import Thread


""" Below code will not work """
class Mythread(Thread):
    def __init__(self):
        self.name = "abc"

    def run(self):
        print("runing started")

t = Mythread()

t.start()


""" Below code will work """
class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.name = "abc"

    def run(self):
        print("runing started")

t = Mythread()

t.start()