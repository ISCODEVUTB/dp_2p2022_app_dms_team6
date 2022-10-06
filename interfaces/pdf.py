
from abc import ABCMeta, abstractmethod


class IPdf(metaclass=ABCMeta):
    @abstractmethod
    def operation(self,) -> str:
        raise NotImplementedError("Implement this method")
