from abc import ABC, abstractmethod

class FileSystemElement(ABC):
    def __init__(self, name:str):
        self.name = name

    @property
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def display(self, tree_element):
        pass


class File(FileSystemElement):
    def __init__(self, name:str, size:int):
        super().__init__(name)
        self._size = size

    @property
    def size(self):
        return self._size

    def display(self, indent:int=0):
        print('  ' * indent, self)

    def __str__(self):
        return f'{self.name} ({self.size} bytes)'

class Folder(FileSystemElement):
    def __init__(self, name:str):
        super().__init__(name)
        self._elements = []

    def add_element(self, element:FileSystemElement):
        self._elements.append(element)

    @property
    def size(self):
        return sum(element.size for element in self._elements)

    def display(self, indent:int=0):
        print('  ' * indent, self)
        for element in self._elements:
            element.display(indent + 1)

    def __str__(self):
        return f'{self.name} ({len(self._elements)} items) {self.size} bytes'

root = Folder('Documents')
project = Folder('Project')
project.add_element(File('README.md', 342))
project.add_element(File('.gitignore', 256))

root.add_element(project)

root.display()
project.display()
