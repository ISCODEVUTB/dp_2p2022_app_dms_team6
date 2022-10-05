from dataclasses import dataclass
from abstracts.document import Document
from interfaces.online import IOnLine
from interfaces.pdf import IPdf


@dataclass
class Scientific(Document, IOnLine, IPdf):
    def category(self) -> str:
        return 'Scientific category'

    def download(self):
        return 'Downloading...'

    def operation(self) -> str:
        return 'Scientific operation...'

    def get_hash_code(self) -> int:
        return self.to_string()

    def equals(self) -> bool:
        return False

    def to_string(self) -> str:
        return self.__str__()

    def clone(self) -> 'Scientific':
        return type(self)(
            **self.__dict__,
        )
