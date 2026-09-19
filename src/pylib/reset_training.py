# scripts/reset_training.py
import shutil
from platformdirs import user_data_path, user_log_path

APP_NAME = "formation-python-perf"

for directory in (
    user_data_path(APP_NAME),
    user_log_path(APP_NAME),
):
    if directory.exists():
        shutil.rmtree(directory)
        print(f"Deleted : {directory}")
