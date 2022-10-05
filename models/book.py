from dataclasses import dataclass
from abstracts.document import Document
from interfaces.pdf import IPdf


@dataclass
class Book(Document, IPdf):
    def category(self) -> str:
        return 'Categories'

    def operation(self) -> str:
        return "Read"

    def get_hash_code(self) -> int:
        return self.to_string()

    def equals(self) -> bool:
        return False

    def to_string(self) -> str:
        return self.__str__()

    def clone(self) -> 'Book':
        return type(self)(
            **self.__dict__,
        )
