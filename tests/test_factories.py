

from factories.book import BookFactory
from factories.magazine import MagazineFactory
from factories.scientific import ScientificFactory
from factories.thesis import ThesisFactory
from models.book import Book
from models.magazine import Magazine
from models.scientific import Scientific
from models.thesis import Thesis
from tests.fake_data import fake_data


def test_book_factory():
    factory = BookFactory()
    book = factory.create(fake_data())
    assert isinstance(book, Book)


def test_magazine_factory():
    factory = MagazineFactory()
    magazine = factory.create(fake_data())
    assert isinstance(magazine, Magazine)


def test_thesis_factory():
    factory = ThesisFactory()
    thesis = factory.create(fake_data())
    assert isinstance(thesis, Thesis)


def test_scientific_factory():
    factory = ScientificFactory()
    scientific = factory.create(fake_data())
    assert isinstance(scientific, Scientific)
