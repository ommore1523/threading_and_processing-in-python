""" Thread Communication 
   EVENT() method used use flag which is default false 
   it will true when set() method is called
   it will false when clear() method is called 


   exp. when green light then drive else stop


   two threads communication with signal flag
"""

## USING EVENT

# import threading
# from time import sleep

# e = threading.Event()
# def light_switch():
#     sleep(3)
#     e.set()
#     print("Switch On")
#     sleep(5)
#     print("Switch OFF")
#     e.clear()

# def vehical():
#     e.wait()
#     while e.is_set():
#         print("Driving")
#         sleep(0.5)
#     print("Done")

# t1 = threading.Thread(target=light_switch)
# t2 = threading.Thread(target=vehical)

# t1.start()
# t2.start()


#------ USING CONDITION ------------------------------------

""" 
    condition class helps to increase speed of communication between two threads
    coondition variable is always ascociated with some kind of lock; this can be passed in or created by default
    passing one is useful when several condition variable must share the same lock  the lock is part of condition object ; 
    YOu dont have to track it separately

"""


# import threading
# from time import sleep

# cond = threading.Condition()
# items = []
# def produceproduct():
#     cond.acquire()
#     for i in range(6):
#         items.append(i)
#         sleep(5)

#     cond.notify()
#     cond.release()

# def getproducts():
#     cond.acquire()
#     cond.wait(timeout=0)
#     cond.release()
#     print("consumed")


# threads1 = threading.Thread(target=produceproduct)
# threads2 = threading.Thread(target=getproducts)

# threads1.start()
# threads2.start()




#------ USING QUEUE ------------------------------------

""" Here producer will produce data which will held by queue
    The data can be taken from queue and utilized by consumer
    We need not to lock any thread  
"""


import threading
from queue import Queue
from time import sleep


class Producer:
    def __init__(self):
        self.q = Queue()

    def produce(self):
        for i in range(6):
            print("Item Produced",i)
            self.q.put(i)
            sleep(3)
            
class Consumer:
    def __init__(self,producerObj):
        self.producerObj = producerObj
    
    def consumer(self):
        for i in range(6):
            print("item consumed",self.producerObj.q.get(i))

p = Producer()
c = Consumer(p)

t1 = threading.Thread(target=p.produce)
t2 = threading.Thread(target=c.consumer)

t1.start()
t2.start()
