class IndentContext:
    def __init__(self):
        self._count = -1

    def __enter__(self):
        self._count += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._count -= 1

    def print(self, content):
        print("\t" * self._count, content)

with IndentContext() as ic:
    ic.print("une ligne")
    ic.print("une autre ligne")
    with ic:
        ic.print('Une ligne indentée')
    ic.print('Et hop, retour.')