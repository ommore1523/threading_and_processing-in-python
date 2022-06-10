"""
send first task
send second task
send third task
Reply to task 3
Reply to task 2
Reply to task 1

"""
import time

# def task1():
#     print("send first task")
#     task2()
#     time.sleep(1) # wait for completion
#     print("Reply to task 1")
    

# def task2():
#     print("send second task")
#     task3()
#     time.sleep(2) # wait for completion
#     print("Reply to task 2")
    


# def task3():
#     print("send third task")
#     time.sleep(3) # wait for completion
#     print("Reply to task 3")

# task1()


import asyncio

async def task1():
    print("send first task")
    asyncio.create_task(task2())
    asyncio.create_task(task3())
    # task3()
    print("Reply to task 1")
    

async def task2():
    async for i in range(3):
        print("t2",i)
        # asyncio.sleep(5) # wait for completion
    
async def task3():
    async for i in range(3):
        print("t3",i)
        # asyncio.sleep(5) # wait for completion
    

asyncio.run(task1())