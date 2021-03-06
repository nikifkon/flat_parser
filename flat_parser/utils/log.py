import logging
import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'class': 'logging.Formatter',
            'format': '[%(levelname)s]: %(message)s'
        },
        'verbose': {
            'class': 'logging.Formatter',
            'format': '[%(levelname)s:%(name)s]: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'WARNING',
            'class': 'flat_parser.utils.log.FileHandlerUTFEncoding',
            'filename': 'flat_parser.log',
            'formatter': 'verbose'
        }
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG'
    },
}


class FileHandlerUTFEncoding(logging.FileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, encoding='utf-8', **kwargs)


def setup_logging(config=None):
    if config is None:
        config = LOGGING_CONFIG
    logging.config.dictConfig(config)
