from abc import ABC, abstractmethod
from dataclasses import dataclass

from interfaces.document import IDocument


@dataclass
class Document(ABC, IDocument):

    @abstractmethod
    def category(self) -> str:
        raise NotImplementedError("Implement this method")

    @abstractmethod
    def equals(self) -> bool:
        raise NotImplementedError("Implement this method")

    @abstractmethod
    def get_hash_code(self) -> int:
        raise NotImplementedError("Implement this method")

    @abstractmethod
    def to_string(self) -> str:
        raise NotImplementedError("Implement this method")

    @abstractmethod
    def clone(self) -> 'Document':
        raise NotImplementedError("Implement this method")


class DocumentFactory:
    @abstractmethod
    def create(self):
        raise NotImplementedError("Implement this method")
