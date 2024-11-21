import os
from pathlib import Path

class ChangeDir:
    def __init__(self, targetpath):
        self._targetpath = Path(targetpath)
        if not self._targetpath.is_dir():
            raise ValueError("")
        self.origin = None


    def __enter__(self):
        self.origin = os.getcwd()
        os.chdir(self._targetpath)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.origin)

print(os.getcwd())
dir_changer = ChangeDir('/opt')
os.chdir("..")
print(os.getcwd())

with dir_changer:
    print(os.getcwd())
    with ChangeDir('/home'):
        with dir_changer:
            print(os.getcwd())
    print(os.getcwd())

print(os.getcwd())