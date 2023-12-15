import threading
import _warnings
from typing import Self

class SingletonMeta(type):
  def __init__(cls, name, bases, dct):
    if name != 'Singleton' and '__new__' in dct:
      _warnings.warn(f'{cls.__name__} may not follow the singleton pattern. Avoid overriding __new__.', RuntimeWarning)
    super().__init__(name, bases, dct)

class Singleton(metaclass=SingletonMeta):
  __instance = None
  __lock = threading.Lock()

  def __new__(cls, *args, **kwargs) -> Self:
    if cls.__instance is None: 
      with cls.__lock:
          if not cls.__instance:
            cls.__instance = super().__new__(cls)
    return cls.__instance
