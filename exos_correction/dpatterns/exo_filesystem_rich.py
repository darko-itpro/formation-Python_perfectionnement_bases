from abc import ABC, abstractmethod
from rich.tree import Tree
from rich import print

class FileSystemElement(ABC):
    def __init__(self, name:str):
        self.name = name

    @property
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def display(self, tree_element:Tree):
        pass


class File(FileSystemElement):
    def __init__(self, name:str, size:int):
        super().__init__(name)
        self._size = size

    @property
    def size(self):
        return self._size

    def display(self, tree_element=None):
        if tree_element is None:
            print(f'📄 {self.name}')
        else:
            tree_element.add(f'📄 {self.name} - ({self.size} bytes)')

        return tree_element

    def accept(self, visitor:'FileSystemVisitor'):
        visitor.visit_file(self)

    def __str__(self):
        return f'📄 {self.name} ({self.size} bytes)'

class Folder(FileSystemElement):
    def __init__(self, name:str):
        super().__init__(name)
        self._elements = []

    def add_element(self, element:FileSystemElement):
        self._elements.append(element)

    @property
    def elements(self):
        return self._elements.copy()

    @property
    def size(self):
        return sum(element.size for element in self._elements)

    def display(self, tree_element=None):
        current_element = Tree(f':file_folder: {self.name} - ({self.size} bytes)')
        for element in self._elements:
            element.display(current_element)

        if tree_element is None:
            print(current_element)
        else:
            tree_element.add(current_element)

        return tree_element

    def accept(self, visitor:'FileSystemVisitor'):
        visitor.visit_directory(self)

    def __str__(self):
        return f'{self.name} ({len(self._elements)} items)'


class FileSystemVisitor(ABC):
    @abstractmethod
    def visit_file(self, file: File) -> None:
        pass

    @abstractmethod
    def visit_directory(self, directory: Folder):
        pass


class SizeCalculatorVisitor(FileSystemVisitor):
    def __init__(self):
        self.size = 0

    def visit_file(self, file: File):
        self.size += file.size

    def visit_directory(self, directory: Folder):
        for item in directory.elements:
            item.accept(self)


if __name__ == '__main__':
    root = Folder('Documents')
    project = Folder('Project')
    project.add_element(File('README.md', 342))
    project.add_element(File('.gitignore', 256))

    root.add_element(project)

    root.display()

    fsv = SizeCalculatorVisitor()
    root.accept(fsv)
    print(fsv.size)
