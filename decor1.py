
# Without Decorator
""" 
def decor(fun):
    def inner():
        print("Before decorating function")
        fun()
        print("After decorating function")
    return inner

def number():
    print("Number")

res = decor(number)
res()

"""

# With Decorator

# """

# exp1.
# def decor(fun):
#     def inner():
#         print("Before decorating function")
#         fun()
#         print("After decorating function")
#     return inner

# @decor
# def number():
#     print("Number")


# def add_10(num):
#     def add_fun():
#         n = num()
#         n = n+10
#         return n
#     return add_fun

# @add_10
# def num():
#     return 10

# print(num()) # out 20




# """


""" """

# def authenticate(fun):
#     print("authentcating")
#     def inner():
#         print("inner")
#         x = fun()
#         print("modifying output..")
#         x = x + 20
#         print("compled")
#         return x
#     return inner

# @authenticate
# def add():
#     n = 5
#     return n 

# ans = add()
# print(ans)         