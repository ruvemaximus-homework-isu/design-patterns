import unittest

from pydantic import ValidationError

from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup
from src.models.range_model import RangeModel


class NomenclatureTestCase(unittest.TestCase):
    """Набор тестов для модели номенклатуры"""

    def test_nomenclature_model_valid(self):
        munit = RangeModel.create_gram()
        nomenclature_group = NomenclatureGroup(name="test")

        item = Nomenclature(name="test", full_name="test", nom_gropup=nomenclature_group, measurement_unit=munit)

        assert item.full_name == "test"
        assert item.measurement_unit == munit
        assert item.nom_gropup == nomenclature_group
    
    def test_nomenclature_model_invalid_measurement_unit(self):
        nomenclature_group = NomenclatureGroup(name="test")

        with self.assertRaises(ValidationError):
            Nomenclature(name="test", full_name="test", nom_gropup=nomenclature_group, measurement_unit="asdf")
    
    def test_nomenclature_model_invalid_nomenclature_group(self):
        munit = RangeModel.create_gram()

        with self.assertRaises(ValidationError):
            Nomenclature(name="test", full_name="test", nom_gropup="asdf", measurement_unit=munit)
