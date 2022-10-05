from dataclasses import dataclass
from abstracts.document import Document
from interfaces.online import IOnLine


@dataclass
class Thesis(Document, IOnLine):
    def category(self) -> str:
        return 'self.category'

    def operation(self) -> str:
        return 'Turnitin'

    def download(self):
        return 'Downloading...'

    def get_hash_code(self) -> int:
        return self.to_string()

    def equals(self) -> bool:
        return False

    def to_string(self) -> str:
        return self.__str__()

    def clone(self) -> 'Thesis':
        return type(self)(
            **self.__dict__,
        )
