from typing import Optional

from pydantic import Field

from src.models.base.base_reference import BaseReference


class RangeModel(BaseReference):
    base_range: Optional[BaseReference] = None
    coeff: int = Field(gt=0, default=1, description="Коэффициент")

    @staticmethod
    def create_gram(gram: int) -> "RangeModel":
        return RangeModel(name="грамм", coeff=gram)

    @staticmethod
    def create_kilogram(kilogram: int) -> "RangeModel":
        return RangeModel(name="килограмм", coeff=kilogram)
