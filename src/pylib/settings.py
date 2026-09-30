"""
Fichier à importer pour utiliser le logger.

Ce fichier doit être importé en premier. Vous devez également importer `logging` dans
le fichier où vous utiliserez le logger.

Les fichiers de données sont écrits dans les répertoires spécifiques des systèmes utilisés. Voir :
 https://platformdirs.readthedocs.io/en/latest/platforms.html pour les détails.
"""

import logging
from pathlib import Path
from platformdirs import user_data_path, user_log_path

APP_NAME = "formation-python-perf"

DATA_PATH = user_data_path(APP_NAME, ensure_exists=True)
LOG_FILE = user_log_path(APP_NAME, ensure_exists=True) / "file.log"

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%H:%M:%S",
                    filename=LOG_FILE
                    )
