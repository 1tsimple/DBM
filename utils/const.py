# ---------- IMPORTS ----------
from pathlib import Path
from dataclasses import dataclass

_BASE_DIR = Path(__file__).parent.parent

@dataclass
class PATH:
  BASE_DIR: Path = _BASE_DIR
  ENV_PATH: Path = _BASE_DIR.joinpath(".env")
  LOG_DIR: Path = _BASE_DIR.joinpath('logs')

class _Marketplace:
  def __init__(self, id: str, name: str, _short: str, channel: str) -> None:
    self.id = id
    self.name = name
    self._short = _short
    self.channel = channel

  def __str__(self) -> str:
    return self._short

@dataclass
class Marketplace:
  US = _Marketplace(id="ATVPDKIKX0DER", name="United States", _short="US", channel="Amazon.com")
  CA = _Marketplace(id="A2EUQ1WTGCTBG2", name="Canada", _short="CA", channel="Amazon.ca")
  MX = _Marketplace(id="A1AM78C64UM0Y8", name="Mexico", _short="MX", channel="Amazon.com.mx")