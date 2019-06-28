# logging_example.py

import logging
from datetime import datetime
# Create a custom logger

logger = logging.getLogger(__name__)

date_time = datetime.now().strftime('%Y%m%d_%H%M%S.%f')

logName = 'aawaz_logging_' + date_time +  '.log'
print('log file name: ', str(logName))

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(logName)
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.setLevel(logging.DEBUG)

logger.info('Logger configured')
