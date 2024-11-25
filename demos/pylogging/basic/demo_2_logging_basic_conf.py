import logging

# config with a level
logging.basicConfig(level=logging.INFO)

# config with a level and format
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s",
#                     datefmt="%H:%M:%S")

# config with a level, format and file
# logging.basicConfig(filename="file.log", encoding='utf-8',
#                     level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s")

logging.debug('Un debug')
logging.info('Une info')
logging.warning("Un warning")
logging.error("Une erreur")
logging.critical('Critique')
