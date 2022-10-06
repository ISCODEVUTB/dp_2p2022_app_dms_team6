
from abc import ABCMeta, abstractmethod


class IMultimedia(metaclass=ABCMeta):
    @abstractmethod
    def play(self,):
        raise NotImplementedError("Implement this method")
