

import pytest

from abstracts.document import Document, DocumentFactory
from tests.fake_data import fake_data


def test_document_clone():
    Document.__abstractmethods__ = frozenset()
    doc = Document(**fake_data())

    with pytest.raises(NotImplementedError, match='Clone is not implemented'):
        doc.clone()


def test_document_to_string():
    Document.__abstractmethods__ = frozenset()
    doc = Document(**fake_data())

    with pytest.raises(NotImplementedError, match='ToString is not implemented'):
        doc.to_string()


def test_document_hash_code():
    Document.__abstractmethods__ = frozenset()
    doc = Document(**fake_data())

    with pytest.raises(NotImplementedError, match='GetHashCode is not implemented'):
        doc.get_hash_code()


def test_document_equals():
    Document.__abstractmethods__ = frozenset()
    doc = Document(**fake_data())

    with pytest.raises(NotImplementedError, match='Equals is not implemented'):
        doc.equals()


def test_document_category():
    Document.__abstractmethods__ = frozenset()
    doc = Document(**fake_data())

    with pytest.raises(NotImplementedError, match='Category is not implemented'):
        doc.category()


def test_document_class():
    DocumentFactory.__abstractmethods__ = frozenset()
    factory = DocumentFactory()

    with pytest.raises(NotImplementedError, match='Create is not implemented'):
        factory.create()
