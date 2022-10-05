from dataclasses import dataclass
from abstracts.document import Document


@dataclass
class File:
    id: int
    path: str
    doc: Document
