from configparser import ConfigParser

import inspect
import logging


def read_configuration(category, key):
    config = ConfigParser()
    config.read("configurations/behave.ini")
    return config.get(category, key)


def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger
