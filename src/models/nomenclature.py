from pydantic import Field

from src.models.base.base_reference import BaseReference


class Nomenclature(BaseReference):
    """Модель номенклатуры"""

    nom_gropup: BaseReference | None = Field(description="Группа номенклатуры", default=None)
    measurement_unit: BaseReference | None = Field(description="Единица измерения", default=None)
    full_name: str = Field(max_length=255, description="Наименование")
