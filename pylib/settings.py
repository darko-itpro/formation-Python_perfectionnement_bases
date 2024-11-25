import logging
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%H:%M:%S",
                    filename=ROOT_PATH / "file.log",
                    )
