import sys
sys.path.append('../app')

class Bar:
    def __init__(self, name):
        self.name = name

    def foo(self):
        return f"{self.name}_fooss"

    def bar(self):
        return f"{self.name}_bar"


if __name__ == "__main__":
    app = Bar('quux')
