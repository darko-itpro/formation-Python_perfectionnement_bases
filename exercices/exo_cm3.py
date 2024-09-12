import os
from pathlib import Path

class ChangeDir:
    def __init__(self, target_dir):
        self._target_dir = Path(target_dir)

    def __enter__(self):
        self._old_dir = Path(os.getcwd())
        if self._target_dir.is_dir():
            os.chdir(self._target_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._old_dir)
        self._old_dir = None

print(os.getcwd())

with ChangeDir('/tmp'):
    print(os.getcwd())
    with ChangeDir('/etc'):
        print(os.getcwd())
    print(os.getcwd())
print(os.getcwd())