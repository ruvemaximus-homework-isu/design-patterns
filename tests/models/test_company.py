import unittest

from pydantic import ValidationError

from src.models.company import Company
from src.models.settings import Settings


class CompanyTestCase(unittest.TestCase):
    """Набор тестов для проверки модели компании"""

    def setUp(self) -> None:
        self.settings = Settings(
            inn="380080920202",
            account="DEFAULT",
            organization_name="Рога и копыта (default)",
            bik="0" * 9,
            correspondent_account="DEFAULT",
            ownership_type="12345",
        )

    def test_model_valid(self):
        """Проверим, что при создании компании с использованием Settings данные валидны"""

        company = Company.from_settings(name="Test Company", settings=self.settings, bill="1234567890")
        assert company.inn == self.settings.inn
        assert company.bik == self.settings.bik
        assert company.bill == "1234567890"
        assert company.ownership_type == self.settings.ownership_type

    def test_model_invalid_inn(self):
        """Проверим, что при создании компании с невалидным ИНН будет исключение"""

        with self.assertRaises(ValidationError):
            obj = Company.from_settings(name="Test Company", settings=self.settings, bill="1234567890")
            obj.inn = "123"
    
    def test_model_invalid_bik(self):
        """Проверим, что при создании компании с невалидным БИК будет исключение"""

        with self.assertRaises(ValidationError):
            obj = Company.from_settings(name="Test Company", settings=self.settings, bill="1234567890")
            obj.bik = "123"
    
    def test_model_invalid_ownership_type(self):
        """Проверим, что при создании компании с невалидным видом собственности будет исключение"""

        with self.assertRaises(ValidationError):
            obj = Company.from_settings(name="Test Company", settings=self.settings, bill="1234567890")
            obj.ownership_type = "123"
