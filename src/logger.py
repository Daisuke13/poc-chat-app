import logging
import sys
import os

def init_logger(name):
    logger = logging.getLogger(name)
    for h in logger.handlers:
        logger.removeHandler(h)
    h = logging.StreamHandler(sys.stdout)
    log_format = '[%(levelname)s] %(message)s'
    h.setFormatter(logging.Formatter(log_format))
    logger.addHandler(h)
    if (os.environ.get('DEBUG') and os.environ.get('DEBUG').lower() in ('true', '1', 't')):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)
    return logger