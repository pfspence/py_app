from random import random


class Foo:
    def __init__(self):
        self.num = random()

    def bar(self):
        return self.num * 1000

    def baz(self):
        return chr(int(self.num*26) + 97)

    def print(self):
        print(100 * self.num)
