""" Avoid Race conditions 
1. Thread synchronisation :  Thread syncronisation is used when multiple threads are acting on same object / function 
"""

# import threading

# class Myclass:
#     def __init__(self,available_seats):
#         self.available_seats =  available_seats
#     def reserve(self,need_seats):
#         print('Available_seats',self.available_seats)
#         if self.available_seats >= need_seats:
#             name = threading.currentThread().name
#             print(f'{need_seats} seats is allocatied for {name}')
#             self.available_seats -= need_seats

#         else:
#             print('Sorry! All seats has allocatied')

# obj = Myclass(1)
# t1 = threading.Thread(target=obj.reserve,args=(1,),name="t1")
# t2 = threading.Thread(target=obj.reserve,args=(1,),name="t2")

# t1.start()
# t2.start()


""" 
omkar@IdeaPad-Y510P:~/Documents/Threading$ python3 main7.py 
Available_seats 1
1 seats is allocatied for t1
Available_seats 0
Sorry! All seats has allocatied

omkar@IdeaPad-Y510P:~/Documents/Threading$ python3 main7.py 
Available_seats 1
1 seats is allocatied for t1
Available_seats 1
Sorry! All seats has allocatied
"""

# import threading

# class Myclass:
#     def __init__(self,available_seats):
#         self.available_seats =  available_seats
#         self.lock = threading.Lock()

#     def reserve(self,need_seats):
#         # self.lock.acquire()
#         print('Available_seats',self.available_seats)
#         if self.available_seats >= need_seats:
#             name = threading.currentThread().name
#             print(f'{need_seats} seats is allocatied for {name}')
#             self.available_seats -= need_seats
#         else:
#             print('Sorry! All seats has allocatied')
#         # self.lock.release()

# obj = Myclass(1)
# t1 = threading.Thread(target=obj.reserve,args=(1,),name="t1")
# t2 = threading.Thread(target=obj.reserve,args=(1,),name="t2")


# """ You can use either join or lock-release"""
# t1.start()
# # t1.join()
# t2.start()
# # t1.join()


""" diff :  lock can used to object and code block level , join : entire process level """





# -------RLOCK-----------------------------------------------------

import threading

# class Myclass:
#     def __init__(self,available_seats):
#         self.available_seats =  available_seats
#         self.lock = threading.RLock()

#     def reserve(self,need_seats):
#         self.lock.acquire()
#         self.lock.acquire()
#         print('Available_seats',self.available_seats)
#         if self.available_seats >= need_seats:
#             name = threading.currentThread().name
#             print(f'{need_seats} seats is allocatied for {name}')
#             self.available_seats -= need_seats
#         else:
#             print('Sorry! All seats has allocatied')
#         self.lock.release()
#         self.lock.release()

# obj = Myclass(1)
# t1 = threading.Thread(target=obj.reserve,args=(1,),name="t1")
# t2 = threading.Thread(target=obj.reserve,args=(1,),name="t2")

# t1.start()
# t2.start()


# -------SEMAPHOE-----------------------------------------------------


import threading

class Myclass:
    def __init__(self,available_seats):
        self.available_seats =  available_seats
        self.lock = threading.Semaphore(2)

    def reserve(self,need_seats):
        self.lock.acquire()
        print('Available_seats',self.available_seats)
        if self.available_seats >= need_seats:
            name = threading.currentThread().name
            print(f'{need_seats} seats is allocatied for {name}')
            self.available_seats -= need_seats
        else:
            print('Sorry! All seats has allocatied')
        self.lock.release()

obj = Myclass(1)
t1 = threading.Thread(target=obj.reserve,args=(1,),name="t1")
t2 = threading.Thread(target=obj.reserve,args=(1,),name="t2")

t1.start()
t2.start()


""" Here we can set how many threads can act on single object simultanoulsy 
in above example only two threads can work simultanoulsy """