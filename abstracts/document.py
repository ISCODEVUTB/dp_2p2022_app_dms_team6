from abc import ABC, abstractmethod
from dataclasses import dataclass

from interfaces.document import IDocument


@dataclass
class Document(ABC, IDocument):

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def equals(self) -> bool:
        pass

    @abstractmethod
    def get_hash_code(self) -> int:
        pass

    @abstractmethod
    def to_string(self) -> str:
        pass

    @abstractmethod
    def clone(self) -> 'Document':
        pass


class DocumentFactory:
    @abstractmethod
    def create(self):
        pass
