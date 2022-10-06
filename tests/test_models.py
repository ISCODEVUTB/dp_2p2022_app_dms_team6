

from models.book import Book
from models.magazine import Magazine
from models.scientific import Scientific
from models.thesis import Thesis
from tests.fake_data import fake_data


def test_book_class():
    doc = Book(**fake_data())
    clone = doc.clone()
    assert doc == clone
    assert isinstance(doc.operation(), str)
    assert isinstance(doc.get_hash_code(), str)
    assert isinstance(doc.to_string(), str)
    assert isinstance(doc.category(), str)
    assert isinstance(doc.equals(), bool)


def test_thesis_class():
    doc = Thesis(**fake_data())
    clone = doc.clone()
    assert doc == clone
    assert isinstance(doc.operation(), str)
    assert isinstance(doc.get_hash_code(), str)
    assert isinstance(doc.to_string(), str)
    assert isinstance(doc.category(), str)
    assert isinstance(doc.download(), str)
    assert isinstance(doc.equals(), bool)


def test_magazine_class():
    doc = Magazine(**fake_data())
    clone = doc.clone()
    assert doc == clone
    assert isinstance(doc.operation(), str)
    assert isinstance(doc.get_hash_code(), str)
    assert isinstance(doc.download(), str)
    assert isinstance(doc.to_string(), str)
    assert isinstance(doc.category(), str)
    assert isinstance(doc.equals(), bool)


def test_scientific_class():
    doc = Scientific(**fake_data())
    clone = doc.clone()
    assert doc == clone
    assert isinstance(doc.operation(), str)
    assert isinstance(doc.get_hash_code(), str)
    assert isinstance(doc.to_string(), str)
    assert isinstance(doc.category(), str)
    assert isinstance(doc.download(), str)
    assert isinstance(doc.equals(), bool)
