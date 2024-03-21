from abc import ABC, abstractmethod
from typing import Optional
from file import File

class PositionProvider(ABC):
  @abstractmethod
  @property
  def position(self) -> tuple[int,int]:
    pass
  @abstractmethod
  def getPosition(self) -> tuple[int,int]:
    pass

class Component(ABC):

  @abstractmethod
  def init(self, file: Optional[File] = None) -> Component:
    pass

  @abstractmethod
  @property
  def position(self) -> PositionProvider | tuple[int,int]:
      pass

  @abstractmethod
  @property
  def zIndex(self) -> int:
      pass

  @abstractmethod
  @property
  def clickAble(self) -> bool:
      pass

  @abstractmethod
  @property
  def moveAble(self) -> bool:
      pass
  
  @abstractmethod
  def move(self, fromEntity: PositionProvider, toEntity: PositionProvider):
    pass

  @abstractmethod
  def click(self, clickPos: PositionProvider):
    pass
