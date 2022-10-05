
from abc import ABCMeta, abstractmethod


class IMultimedia(metaclass=ABCMeta):
    @abstractmethod
    def play(self,):
        pass
