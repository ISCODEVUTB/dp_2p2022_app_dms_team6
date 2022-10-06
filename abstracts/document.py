from abc import ABC, abstractmethod
from dataclasses import dataclass

from interfaces.document import IDocument


@dataclass
class Document(ABC, IDocument):

    @abstractmethod
    def category(self) -> str:
        raise NotImplementedError("Category is not implemented")

    @abstractmethod
    def equals(self) -> bool:
        raise NotImplementedError("Equals is not implemented")

    @abstractmethod
    def get_hash_code(self) -> int:
        raise NotImplementedError("GetHashCode is not implemented")

    @abstractmethod
    def to_string(self) -> str:
        raise NotImplementedError("ToString is not implemented")

    @abstractmethod
    def clone(self) -> 'Document':
        raise NotImplementedError("Clone is not implemented")


class DocumentFactory:
    @abstractmethod
    def create(self):
        raise NotImplementedError("Create is not implemented")
