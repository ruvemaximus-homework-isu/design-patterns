from src.models.nomenclature_group import NomenclatureGroup


def test_nomenclature_group():
    item = NomenclatureGroup(name="test")
    assert item.name == "test"
