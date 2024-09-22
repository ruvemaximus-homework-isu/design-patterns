from pydantic import Field

from src.models.base.base_reference import BaseReference
from src.models.settings import Settings


class Company(BaseReference):
    """Модель организации"""

    inn: str = Field(max_length=12, min_length=12, description="ИНН")
    bik: str = Field(max_length=9, min_length=9, description="БИК")
    bill: str | None = Field(description="Счет", default=None)
    ownership_type: str = Field(max_length=5, min_length=5, description="Форма собственности")

    @classmethod
    def from_settings(cls, name: str, settings: Settings, bill: str | None = None) -> "Company":
        return cls(name=name, inn=settings.inn, bik=settings.bik, ownership_type=settings.ownership_type, bill=bill)
