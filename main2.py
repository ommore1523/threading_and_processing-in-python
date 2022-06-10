# creating thread using function

# import threading
# import time
# print(threading.active_count())
# def hello(abc):
#     time.sleep(10)
#     print("Hello",abc)
# for i in range(5):
#     thread = threading.Thread(target=hello,args=(2,))
#     thread.start()
#     print(threading.active_count())
import threading
import time
# print(threading.active_count())
def hello(abc):

    time.sleep(3)
    print("Hello",abc)

proce = []
for i in range(10):
    process = threading.Thread(target=hello,args=(2,))
    proce.append(process)

for pro in proce:
    pro.start()

for pro in proce:
    pro.join()

print("hello world")
    # process.start()
    # process.join()
    # print(threading.active_count())