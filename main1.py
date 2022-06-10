import threading
import time

t = threading.current_thread().getName()

print("abc")
time.sleep(5)
print(t) # utput MainThread




