class BaseClass1:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello {} from {}'.format(self.name, __name__))
