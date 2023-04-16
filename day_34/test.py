class A:

    def __init__(self):
        pass

    def func1(self):
        return 1

    def func2():
        return self.func1()


x = A()
print(x.func2())
