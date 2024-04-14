import logging.handlers
import sys
import uuid


class Logger:
    @staticmethod
    def setup_logger(name):

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        request_id = str(uuid.uuid4())

        formatter = logging.Formatter(
            f"%(asctime)s | %(name)s | %(levelname)s | {request_id} |\n%(message)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        return logger
