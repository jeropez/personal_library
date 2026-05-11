import pytest
from unittest.mock import MagicMock
from personal_library.services import LibroService


@pytest.fixture
def libro_service():
    mock_storage = MagicMock()
    return LibroService(mock_storage)