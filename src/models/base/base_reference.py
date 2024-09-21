import uuid

from pydantic import BaseModel, Field


class BaseReference(BaseModel):
    """Базовая модель приложения"""

    uniq_code: str = Field(default_factory=lambda: str(uuid.uuid4()), frozen=True)
    name: str = Field(max_length=50, default="")

    class Config:
        validate_assignment = True

    def set_compare_mode(self, other) -> bool:
        if other is None:
            return False

        if not isinstance(other, BaseReference):
            return False

        return self.uniq_code == other.uniq_code

    def __eq__(self, other) -> bool:
        return self.set_compare_mode(other)
