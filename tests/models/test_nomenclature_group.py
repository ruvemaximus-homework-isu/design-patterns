import unittest

from src.models.nomenclature_group import NomenclatureGroup


class NomenclatureGroupTestCase(unittest.TestCase):
    """Набор текстов для модели группы номенклатуры"""

    def test_nomenclature_group(self):
        item = NomenclatureGroup(name="test")
        assert item.name == "test"
