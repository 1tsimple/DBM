import logging
import sys
from .const import PATH

FORMATTER = logging.Formatter('[ %(asctime)s ] - %(thread)d - %(filename)s - %(funcName)s - [ %(levelname)s ] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
CONSOLE_HANDLER.setFormatter(FORMATTER)

if (not PATH.LOG_DIR.exists()):
  PATH.LOG_DIR.mkdir(parents=True, exist_ok=True)
