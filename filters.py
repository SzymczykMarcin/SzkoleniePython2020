import logging

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