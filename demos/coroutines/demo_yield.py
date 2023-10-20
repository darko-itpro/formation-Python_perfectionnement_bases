import logging

def repas():
    yield "entrée"
    yield "plat"
    yield "dessert"

def ticket():
    number = 0
    while True:
        number += 1
        yield number


from demos.coroutines.cordeco import coroutine

@coroutine
def receiver():
    logging.info("Setting up")
    while True:
        data = yield
        print(f"Got {data}")


from pathlib import Path
from pyflix.loaders import file_helpers as fh
@coroutine
def loader(paths:list):
    for path in (Path(p).resolve() for p in paths):
        if path.is_dir():
            yield from fh.load_from_filenames(path)
        elif path.is_file():
            yield from fh.load_from_csv(path)
        else:
            logging.error(f"No source for {path}")
