import logging
from logging.config import dictConfig


class LowPassError(logging.Filter):
    """
    Defines low-pass filter that blocks everything equal or above ERROR level.
    """

    def filter(self, record):
        """
        Determine if the specified record is to be logged.
        :param record: some build in record object
        :return: bool
        """
        return record.levelno < logging.ERROR


class Info(logging.Filter):
    """
    Defines filter that blocks everything equal INFO level.
    """

    def filter(self, record):
        """
        Determine if the specified record is to be logged.
        :param record: some build in record object
        :return: bool
        """
        return record.levelno == logging.INFO


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console': {
            'format': '%(name)s - %(levelname)s - %(filename)s::%(lineno)d - %(message)s'
        },
        'file': {
            'format': '%(asctime)s - %(levelname)s - %(filename)s::%(lineno)d - %(message)s'
        },
        'error': {
            'format': '%(asctime)s - %(process)d - %(levelname)s - %(name)s - %(filename)s::%(lineno)d - %(message)s'
        },
    },
    # 'filters': {
    #     'low-pass': {
    #         '()': 'LowPassError',
    #     },
    #     'info': {
    #         '()': 'Info',
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'console',
            'class': 'logging.StreamHandler',
            # 'filters': ['low-pass'],
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'error',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',  # Default is stderr
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'file',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'filename': 'log.log',
            'interval': 1,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {
            'handlers': ['console', 'error', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

dictConfig(LOGGING_CONFIG)

LOGGER = logging.getLogger('')

LOGGER.debug('BBB')

LOGGER.info('AAAA')