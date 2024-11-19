import logging


# Creation of formatters
daily_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                 datefmt='%H:%M:%S')
complete_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Handlers creation, one for the console, the other for a file
console_handler = logging.StreamHandler()

file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.ERROR)

# Formatters and handlers association
console_handler.setFormatter(daily_format)
file_handler.setFormatter(complete_format)

# *Custom* logger creation
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Adding handlers to the loggers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug('Un debug')
logger.info('Une info')
logger.warning("Un warning")
logger.error("Une erreur")
logger.critical('Critique')
