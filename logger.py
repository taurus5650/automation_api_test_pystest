import logging.handlers
import sys

class Logger:
    @staticmethod
    def setup_logger():

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s |\n%(message)s | %(threadName)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        return logger
