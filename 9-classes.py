from BaseClass1 import BaseClass1
from BaseClass2 import BaseClass2


class MyClass(BaseClass1, BaseClass2):
    """This is a very simple class"""

    count = 0

    def __init__(self, name):
        super().__init__(name)
        MyClass.count = MyClass.count + 1
        self.name = name

    @staticmethod
    def square(x):
        return x ** 2


c = MyClass('Tom')
print(c.__doc__)
print('Counter: ', c.count)
print(c.square(2))

# todo: switch the inheritance position in line 5 to see the difference
c.say_hello()

c2 = MyClass('Jerry')
print('Counter: ', c2.count)
c2.say_hello()
