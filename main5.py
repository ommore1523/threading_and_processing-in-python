# use class method as thread


from threading import Thread


class Myclass:
    def abc(self,a):
        print("Thread")

obj= Myclass()


t = Thread(target=obj.abc,args=(2,))