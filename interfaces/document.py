from abc import ABCMeta
from dataclasses import dataclass
from enum import Enum
from typing import List


class Format(Enum):
    PRINTED = "PRINTED"
    DIGITAL = "DIGITAL"
    AUDIO = "AUDIO"


@dataclass
class IDocument(metaclass=ABCMeta):
    ISBN: str
    year: int
    title: str
    pages: int
    edition: str
    formats: List[Format]
    authors: List[str]
    editorial: str
    languages: List[str]
