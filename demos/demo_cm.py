class ContextDemo:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Entering in {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print("Exiting")
        return 1

    def print(self):
        print(f"Printing from {self.name}")

print("Start")
with ContextDemo("Demo context") as cm:
    print("in context")
    int('toto')

print("done")