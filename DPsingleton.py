# class SingleTon:
#     def __new__(cls, *args, **kwargs):
#         print(dir(cls))
#         if not hasattr(cls,'_instance'):
#             cls._instance = super().__new__(cls, *args,**kwargs)
#         return cls._instance

#     def hello(self):
#         print("hello world")

# """ 
#     here after printing objects you can notice that that 
#     every object creation object will be same 
#     <__main__.SingleTon object at 0x7f86c0cc0610> <__main__.SingleTon object at 0x7f86c0cc0610>
# """
# obj1 =  SingleTon()
# obj2 = SingleTon()
# print(obj1,obj2)

# obj1.data=10

# print(obj1.data,obj2.data)
# obj1.hello()

# obj2.data=5
# print(obj2.data,obj1.data)

" *******************************************************************************************************************  "
# class SingleTon:
#     pass

# obj1 = SingleTon()
# obj2 = SingleTon()
# print(obj1,obj2)

"""

In normal case objects creates more than one time 
<__main__.SingleTon object at 0x7f82e63ba4c0> <__main__.SingleTon object at 0x7f82e623dfd0>

"""