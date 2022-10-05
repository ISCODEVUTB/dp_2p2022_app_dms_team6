

from abstracts.document import DocumentFactory
from interfaces.document import IDocument
from models.magazine import Magazine


class MagazineFactory(DocumentFactory):
    def create(self, info: IDocument):
        return Magazine(**info)
