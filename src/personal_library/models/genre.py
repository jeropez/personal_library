from dataclasses import dataclass


@dataclass
class Genre:
    """Represents a genre in the personal library."""
    id: int
    name: str

    def __post_init__(self):
        self._validate_name()

    def _validate_name(self):
        if not self.name.strip():
            raise ValueError("Genre name cannot be empty")