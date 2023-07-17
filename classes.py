class MyClass:
    i: int = 19

    def __init__(self, _i: int):
        self.i = _i


x = MyClass(10)
y = MyClass(123)

print(x.i)
print(y.i)

x.new_attr = 1234
x.i = 12345

print(x.new_attr)
print(x.i)


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
print(w1.purpose, w1.region)


def f1(self, _x, _y):
    return min(_x, _x + _y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c_obj = C()

print(c_obj.h())
print(c_obj.f(12, -22))
print(c_obj.g())


def template_method():
    print()


class UnsupportedOpException(BaseException):
    pass


class AbstractClass:
    def override_it(self):
        raise UnsupportedOpException('This is abstract method and it should be overwritten on child')


class Implementation(AbstractClass):
    def override_it(self):
        print("I can do this not my parent")


impl = Implementation()

impl.override_it()
AbstractClass.override_it(impl)


class MyException(RuntimeError):
    pass


raise MyException('test error')
