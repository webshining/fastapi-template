from pathlib import Path

import logging

LOGS_DIR = f"{Path(__file__).absolute().parent}/logs"

# Loggers
logger = logging.getLogger("app")
database_logger = logging.getLogger("database")
uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_error_logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.INFO)

# Handlers
logger_ch = logging.StreamHandler()
logger_fh = logging.FileHandler(filename=f'{LOGS_DIR}/app.log', mode='a')
database_ch = logging.StreamHandler()
database_fh = logging.FileHandler(filename=f'{LOGS_DIR}/database.log', mode='a')
uvicorn_fh = logging.FileHandler(filename=f'{LOGS_DIR}/uvicorn.log', mode='a')
logger.addHandler(logger_ch)
logger.addHandler(logger_fh)
database_logger.addHandler(database_ch)
database_logger.addHandler(database_fh)
uvicorn_logger.addHandler(uvicorn_fh)
uvicorn_error_logger.addHandler(uvicorn_fh)

# Formatters
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
logger_fh.setFormatter(formatter)
logger_ch.setFormatter(formatter)
