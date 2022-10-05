

from abstracts.document import DocumentFactory
from interfaces.document import IDocument
from models.scientific import Scientific


class ScientificFactory(DocumentFactory):
    def create(self, info: IDocument):
        return Scientific(**info)
