import pytest
from pydantic import ValidationError

from src.models.company import Company
from src.models.settings import Settings


@pytest.fixture(scope="module")
def settings() -> Settings:
    return Settings(
        inn="380080920202",
        account="DEFAULT",
        organization_name="Рога и копыта (default)",
        bik="0" * 9,
        correspondent_account="DEFAULT",
        ownership_type="12345",
    )


@pytest.fixture
def company(settings) -> Company:
    return Company.from_settings(name="Test Company", settings=settings, bill="1234567890")


def test_model_valid(settings, company):
    """Проверим, что при создании компании с использованием Settings данные валидны"""

    assert company.inn == settings.inn
    assert company.bik == settings.bik
    assert company.bill == "1234567890"
    assert company.ownership_type == settings.ownership_type


def test_model_invalid_inn(company):
    """Проверим, что при создании компании с невалидным ИНН будет исключение"""

    with pytest.raises(ValidationError):
        company.inn = "123"


def test_model_invalid_bik(company):
    """Проверим, что при создании компании с невалидным БИК будет исключение"""

    with pytest.raises(ValidationError):
        company.bik = "123"


def test_model_invalid_ownership_type(company):
    """Проверим, что при создании компании с невалидным видом собственности будет исключение"""

    with pytest.raises(ValidationError):
        company.ownership_type = "123"
