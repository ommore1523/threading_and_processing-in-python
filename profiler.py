from profilehooks import profile
import time
@profile
def my_function():
    for i in range(10):
        print(i)
        time.sleep(5)
    x = 10 + 10

if __name__ == '__main__':
    my_function()