from dataclasses import dataclass
from abstracts.document import Document
from interfaces.online import IOnLine


@dataclass
class Magazine(Document, IOnLine):
    def category(self) -> str:
        return 'Magazine category'

    def get_hash_code(self) -> int:
        return self.to_string()

    def equals(self) -> bool:
        return False

    def to_string(self) -> str:
        return self.__str__()

    def operation(self) -> str:
        return 'Scroll'

    def download(self):
        return 'Downloading...'

    def clone(self) -> 'Magazine':
        return type(self)(
            **self.__dict__,
        )
