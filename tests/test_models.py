

from models.book import Book


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
