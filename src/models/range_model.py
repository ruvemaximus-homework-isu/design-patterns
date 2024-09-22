from typing import Optional

from pydantic import Field

from src.models.base.base_reference import BaseReference


class RangeModel(BaseReference):
    base_range: Optional[BaseReference] = None
    coeff: int = Field(gt=0, default=1, description="Коэффициент")

    @staticmethod
    def create_gram() -> "RangeModel":
        return RangeModel(name="грамм", base_range=None, coeff=1)

    @staticmethod
    def create_kilogram() -> "RangeModel":
        base = RangeModel.create_gram()
        return RangeModel(name="килограмм", base_range=base, coeff=1000)
