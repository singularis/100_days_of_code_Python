def add(*args):
    a = 0
    for n in args:
        a +=n
    return a

print(add(5,4,3))

def calucalte(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key*value)


calucalte(add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw["model"]