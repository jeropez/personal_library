import pytest
from unittest.mock import MagicMock
from personal_library.services.book_service import BookService



@pytest.fixture
def libro_service():
    mock_storage = MagicMock()
    return BookService(mock_storage)