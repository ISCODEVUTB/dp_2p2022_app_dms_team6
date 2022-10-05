

import pytest
from models.manager import DocumentManager, CreateDocumentInput, FileType
from models.book import Book


def fake_doc() -> CreateDocumentInput:
    return CreateDocumentInput(
        file_name='test',
        file_type=FileType.BOOK,
        data={
            'ISBN': '123',
            'year': 2022,
            'title': 'The Book',
            'pages': 500,
            'edition': 'The edition',
            'formats': ['AUDIO', 'PRINTED'],
            'authors': ['The Crhis'],
            'editorial': 'The editorial',
            'languages': ['es', 'en'],
        }
    )


def test_document_manger_singleton():
    manager1 = DocumentManager()
    manager2 = DocumentManager()
    assert manager1 == manager2
    assert manager1.length_files == 0


def test_should_add_and_remove_document():
    manager = DocumentManager()
    manager.create_document(fake_doc())

    assert manager.length_files == 1
    assert isinstance(manager.files[0].file, Book)

    manager.delete_file(0)
    assert manager.length_files == 0


def test_should_raise_exception_on_remove_file():
    manager = DocumentManager()

    with pytest.raises(ValueError, match='Index out of range: 1'):
        manager.delete_file(1)


def test_should_raise_exception_on_duplicate_file():
    manager = DocumentManager()

    with pytest.raises(ValueError, match='Index out of range: 1'):
        manager.duplicate_file(1)
