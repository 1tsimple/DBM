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
from os import getenv
from motor.motor_asyncio import AsyncIOMotorClient

from utils.singleton import Singleton

class AsyncIOMotorClientWrapper(Singleton):
  __slots__ = ('client', )
  
  def __init__(self) -> None:
    logger.info(f'AsyncIOMotorClientWrapper object has been created and initialized. {{"id": {id(self)}}}')
  
  def __enter__(self):
    self.client = AsyncIOMotorClient(getenv('MONGODB_CONN_TXT'))
    return self.client
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.client.close()

class DBManager(Singleton):
  __slots__ = ('client', )
  
  def __init__(self) -> None:
    self.client = AsyncIOMotorClientWrapper()
    logger.info(f'DBManager object has been created and initialized. {{"id": {id(self)}}}')
  
  async def find(self):
    with self.client as client:
      collection = client.amazon.orders
      documents = collection.find().limit(10)
      async for document in documents:
        print(document)