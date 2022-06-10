
from multiprocessing import Process
import time

# def h1():
#     while True:
#         print(1)
# def h2():
#     while True:
#         print(2)

# def h3():
#     while True:
#         print(3)
# def h4():
#     while True:
#         print(4)
# def h5():
#     while True:
#         print(5)
# def h6():
#     while True:
#         print(6)
# def h7():
#     while True:
#         print(7)
# def h8():
#     while True:
#         print(8)

# def h9():
#     while True:
#         print(9)

# p1 = Process(target=h1)
# p1.start()

# # while p1.is_alive():
# #     print("alive")
# #     time.sleep(2)

# p2 = Process(target=h2,args=(p1,))
# p2.start()
# p3 = Process(target=h3)
# p3.start()
# p4 = Process(target=h4)
# p4.start()
# p5 = Process(target=h5)
# p5.start()
# p6 = Process(target=h6)
# p6.start()
# p7 = Process(target=h7)
# p7.start()
# p8 = Process(target=h8)
# p8.start()
# p9 = Process(target=h9)
# p9.start()



# ------------------------------------------------
# def h1():
#     while True:
#         pass
# def h2():
#     while True:
#         pass

# def h3():
#     while True:
#         pass
# def h4():
#     while True:
#         pass
# def h5():
#     while True:
#         pass
# def h6():
#     while True:
#         pass
# def h7():
#     while True:
#         pass
# def h8():
#     while True:
#         pass

# def h9():
#     while True:
#         pass

# p1 = Process(target=h1)
# p1.start()

# # while p1.is_alive():
# #     print("alive")
# #     time.sleep(2)

# p2 = Process(target=h2)
# p2.start()
# p3 = Process(target=h3)
# p3.start()
# p4 = Process(target=h4)
# p4.start()
# p5 = Process(target=h5)
# p5.start()
# p6 = Process(target=h6)
# p6.start()
# p7 = Process(target=h7)
# p7.start()
# p8 = Process(target=h8)
# p8.start()
# p9 = Process(target=h9)
# p9.start()


# ---------------------------------------------------------------
# def h1():
#     while True:
#         pass

# p1 = Process(target=h1)
# p1.start()

# ---------------------------------------------------------------


def h1():
    for i in range(4):
        print(i)
        time.sleep(2)

p1 = Process(target=h1)
p1.start()

while p1.is_alive():
    print("alive")
    time.sleep(1)