import pytest
from pydantic import ValidationError

from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup
from src.models.range_model import RangeModel


@pytest.fixture
def nomenclature_group() -> NomenclatureGroup:
    return NomenclatureGroup(name="test")


@pytest.fixture
def gram_unit() -> RangeModel:
    return RangeModel.create_gram()


def test_nomenclature_model_valid(nomenclature_group, gram_unit):
    item = Nomenclature(name="test", full_name="test", nom_gropup=nomenclature_group, measurement_unit=gram_unit)

    assert item.full_name == "test"
    assert item.measurement_unit == gram_unit
    assert item.nom_gropup == nomenclature_group


def test_nomenclature_model_invalid_measurement_unit(nomenclature_group):
    with pytest.raises(ValidationError):
        Nomenclature(name="test", full_name="test", nom_gropup=nomenclature_group, measurement_unit="asdf")


def test_nomenclature_model_invalid_nomenclature_group(gram_unit):
    with pytest.raises(ValidationError):
        Nomenclature(name="test", full_name="test", nom_gropup="asdf", measurement_unit=gram_unit)
