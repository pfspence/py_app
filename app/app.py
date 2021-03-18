

class App:
    def __init__(self, name):
        self.name = name

    def foo(self):
        return f"{self.name}_foo"

    def bar(self):
        return f"{self.name}_bar"


if __name__ == "__main__":
    app = App('quux')
