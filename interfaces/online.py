
from abc import ABCMeta, abstractmethod


class IOnLine(metaclass=ABCMeta):
    @abstractmethod
    def download(self):
        raise NotImplementedError("Implement this method")
