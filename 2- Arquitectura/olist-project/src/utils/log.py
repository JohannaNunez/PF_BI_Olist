from datetime import datetime
import logging
import os
from settings.url_constants import MAIN_DIR

logger = logging.getLogger('bi-course-project')
logger.setLevel(logging.INFO)

def logInfo(event):
    print(event)
    while len(logger.handlers)>0:
        logger.removeHandler(logger.handlers[0])
    FILENAME = datetime.today().strftime('%Y-%d-%m')
    fh = logging.FileHandler(os.path.join(MAIN_DIR, 'logs', f'logs_{FILENAME}.log'))
    logger.addHandler(fh)
    logger.info(f'[{datetime.now()}] - {event}')
    pass
