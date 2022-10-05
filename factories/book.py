

from abstracts.document import DocumentFactory
from interfaces.document import IDocument
from models.book import Book


class BookFactory(DocumentFactory):
    def create(self, info: IDocument):
        return Book(**info)
