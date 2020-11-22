from logging.config import dictConfig

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
    'filters': {
        'low-pass': {
            '()': 'filters.LowPassError',
        },
        'info': {
            '()': 'filters.Info',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'console',
            'class': 'logging.StreamHandler',
            'filters': ['low-pass'],
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


