import unittest

from pydantic import ValidationError

from src.models.range_model import RangeModel


class RangeModelTestCase(unittest.TestCase):
    """Тесты для модели RangeModel"""

    def test_model_create_killogram(self):
        """Проверяем создание киллограмм"""

        item = RangeModel.create_kilogram()
        assert item.name == "килограмм"
        assert item.base_range.name == "грамм"
        assert item.coeff == 1000

    def test_model_create_gram(self):
        """Проверяем создание грамма"""

        item = RangeModel.create_gram()
        assert item.name == "грамм"
        assert item.base_range is None
        assert item.coeff == 1

    def test_model_invalid_coeff(self):
        """Проверяем ошибку при невалидном коэффициенте"""

        with self.assertRaises(ValidationError):
            RangeModel(name="foobar", base_range=None, coeff=0)
