from random import random


class Foo:
    def __init__(self):
        self.num = random()

    def bar(self):
        return self.num * 10000

    def print(self):
        print(100 * self.num)
