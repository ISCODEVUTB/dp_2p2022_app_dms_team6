

from models.book import Book
from models.magazine import Magazine
from models.scientific import Scientific
from models.thesis import Thesis


def fake_data():
    return {
        'ISBN': '32',
        'year': 2021,
        'title': 'The Fake Book 2',
        'pages': 150,
        'edition': 'The edition 2 ',
        'formats': ['PRINTED'],
        'authors': ['The Crhis'],
        'editorial': 'The editorial',
        'languages': ['es', 'en'],
    }


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
