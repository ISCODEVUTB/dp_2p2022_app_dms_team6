

from interfaces.document import IDocument
from models.thesis import Thesis
from abstracts.document import DocumentFactory


class ThesisFactory(DocumentFactory):
    def create(self, info: IDocument):
        return Thesis(**info)
