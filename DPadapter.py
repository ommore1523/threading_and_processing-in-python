
class string:
    def get(self, s):
        return s

class integer:
    def get(self, n):
        return n

class adapteStringConverter(integer):
    def get(self,n):
        return str(super(adapteStringConverter,self).get(n))

if __name__ == '__main__':
    obj = adapteStringConverter()
    x = obj.get(12)
    print(x)