class IndentContext:
    def __init__(self):
        self.indent = -1

    def print(self, sentence):
        print("    " * self.indent, sentence)

    def __enter__(self):
        self.indent += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent -= 1


with IndentContext() as ic:
    ic.print("une ligne")
    ic.print("une autre ligne")
    with ic:
        ic.print("une ligne indentée")
        with ic:
            ic.print("une ligne encore plus indentée")
    ic.print("une autre ligne")