from enum import Enum
from typing import Dict, List, Optional
from abstracts.document import DocumentFactory
from factories.book import BookFactory
from factories.magazine import MagazineFactory
from factories.scientific import ScientificFactory
from factories.thesis import ThesisFactory
from interfaces.singleton import Singleton
from models.file import File
from pydantic import BaseModel


class FileType(Enum):
    BOOK = 'BOOK'
    MAGAZINE = 'MAGAZINE'
    SCIENTIFIC = 'SCIENTIFIC'
    THESIS = 'THESIS'


class CreateDocumentInput(BaseModel):
    file_name: Optional[str] = None
    file_type: FileType
    data: Dict


class DocumentManager(metaclass=Singleton):
    _files: List[File] = []

    @property
    def files(self) -> List[File]:
        return self._files

    @property
    def length_files(self) -> int:
        return len(self._files)

    def create_document(self, input: CreateDocumentInput):
        factory: DocumentFactory

        if FileType.BOOK == input.file_type:
            factory = BookFactory()
        elif FileType.MAGAZINE == input.file_type:
            factory = MagazineFactory()
        elif FileType.SCIENTIFIC == input.file_type:
            factory = ScientificFactory()
        elif FileType.THESIS == input.file_type:
            factory = ThesisFactory()

        if not factory:
            raise ValueError('DocumentFactory must be a valid FileType')

        doc = factory.create(input.data)
        new_file = File(
            id=self.length_files,
            path='./models/{}'.format(
                input.file_name if input.file_name else
                'new_document-{}'.format(self.length_files + 1)),
            doc=doc
        )

        self._files.append(new_file)

    def delete_file(self, idx: int):
        if idx > self.length_files:
            raise ValueError('Index out of range: %d' % idx)
        self._files.pop(idx)

    def duplicate_file(self, idx: int):
        if idx > self.length_files:
            raise ValueError('Index out of range: %d' % idx)
        new_id = self.length_files + 1
        self._files.append(File(
            id=new_id,
            path='{}-{}'.format(self._files[idx].path, new_id),
            doc=self._files[idx].doc.clone()
        ))
