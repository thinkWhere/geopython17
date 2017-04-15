import logging


class EnvironmentConfig:
    """ Base class for config that is shared between environments """
    LOG_DIR = 'logs'


class ProdConfig(EnvironmentConfig):
    """ Production Environment Config """
    LOG_LEVEL = logging.ERROR


class DevConfig(EnvironmentConfig):
    """ Production Environment Config """
    LOG_LEVEL = logging.DEBUG
