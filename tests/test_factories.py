

from factories.book import BookFactory
from factories.magazine import MagazineFactory
from factories.scientific import ScientificFactory
from factories.thesis import ThesisFactory
from models.book import Book
from models.magazine import Magazine
from models.scientific import Scientific
from models.thesis import Thesis


def fake_doc():
    return {
        'ISBN': '123',
        'year': 2021,
        'title': 'The Fake Book',
        'pages': 250,
        'edition': 'The edition',
        'formats': ['AUDIO', 'PRINTED'],
        'authors': ['The Crhis'],
        'editorial': 'The editorial',
        'languages': ['es', 'en'],
    }


def test_book_factory():
    factory = BookFactory()
    book = factory.create(fake_doc())
    assert isinstance(book, Book)


def test_magazine_factory():
    factory = MagazineFactory()
    magazine = factory.create(fake_doc())
    assert isinstance(magazine, Magazine)


def test_thesis_factory():
    factory = ThesisFactory()
    thesis = factory.create(fake_doc())
    assert isinstance(thesis, Thesis)


def test_scientific_factory():
    factory = ScientificFactory()
    scientific = factory.create(fake_doc())
    assert isinstance(scientific, Scientific)
