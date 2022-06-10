# 1. start method => which will start thread Pool 
# 2. after start method there is inbuilt run method called 
# 3. join => join method will tells that wait for complete thread task



from threading import Thread

class MythreadClass(Thread):
    def run(self):
        print("run method")


t=MythreadClass()
t.start()

t.join()