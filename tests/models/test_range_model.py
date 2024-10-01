import pytest
from pydantic import ValidationError

from src.models.range_model import RangeModel


def test_model_create_killogram():
    """Проверяем создание киллограмм"""

    item = RangeModel.create_kilogram()
    assert item.name == "килограмм"
    assert item.base_range.name == "грамм"
    assert item.coeff == 1000


def test_model_create_gram():
    """Проверяем создание грамма"""

    item = RangeModel.create_gram()
    assert item.name == "грамм"
    assert item.base_range is None
    assert item.coeff == 1


def test_model_invalid_coeff():
    """Проверяем ошибку при невалидном коэффициенте"""

    with pytest.raises(ValidationError):
        RangeModel(name="foobar", base_range=None, coeff=0)
