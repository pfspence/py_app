from random import random


class Foo:
    def __init__(self):
        self.num = random()

    def print(self):
        print(100 * self.num)
