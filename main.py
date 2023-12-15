# ---------- ENV SETUP ----------
from utils.const import PATH
from dotenv import load_dotenv
load_dotenv(PATH.ENV_PATH)

# ---------- LOGGING ----------
import os
import logging
from utils.log import FORMATTER, CONSOLE_HANDLER

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LOG_PATH = PATH.LOG_DIR.joinpath(os.path.basename(__file__).removesuffix('.py') + '.log')
file_handler = logging.FileHandler(LOG_PATH)
file_handler.setFormatter(FORMATTER)

logger.addHandler(CONSOLE_HANDLER)
logger.addHandler(file_handler)

# ---------- IMPORTS ----------
import asyncio

async def main():
  pass

if __name__ == '__main__':
  asyncio.run(main())