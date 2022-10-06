

import pytest
from models.magazine import Magazine
from models.manager import DocumentManager, CreateDocumentInput, FileType
from models.book import Book
from models.scientific import Scientific
from models.thesis import Thesis
from tests.fake_data import fake_data


def fake_doc(type_doc: FileType) -> CreateDocumentInput:
    return CreateDocumentInput(
        file_name='test',
        file_type=type_doc,
        data=fake_data()
    )


def test_document_manger_singleton():
    manager1 = DocumentManager()
    manager2 = DocumentManager()
    assert manager1 == manager2
    assert manager1.length_files == 0


def test_should_add_and_remove_document():
    manager = DocumentManager()
    manager.create_document(fake_doc(FileType.BOOK))
    manager.create_document(fake_doc(FileType.MAGAZINE))
    manager.create_document(fake_doc(FileType.SCIENTIFIC))
    manager.create_document(fake_doc(FileType.THESIS))

    assert manager.length_files == 4
    assert isinstance(manager.files[0].doc, Book)
    assert isinstance(manager.files[1].doc, Magazine)
    assert isinstance(manager.files[2].doc, Scientific)
    assert isinstance(manager.files[3].doc, Thesis)

    manager.delete_file(0)
    manager.delete_file(0)
    manager.delete_file(0)
    manager.delete_file(0)
    assert manager.length_files == 0


def test_should_duplicate_a_document():
    manager = DocumentManager()
    manager.create_document(fake_doc(FileType.BOOK))
    manager.duplicate_file(0)

    assert manager.length_files == 2
    manager.delete_file(0)
    manager.delete_file(0)


def test_should_raise_exception_on_remove_file():
    manager = DocumentManager()

    with pytest.raises(ValueError, match='Index out of range: 1'):
        manager.delete_file(1)


def test_should_raise_exception_on_duplicate_file():
    manager = DocumentManager()

    with pytest.raises(ValueError, match='Index out of range: 1'):
        manager.duplicate_file(1)
