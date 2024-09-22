import unittest

from src.models.warehouse import Warehouse


class WarehouseTestCase(unittest.TestCase):
    def test_warehouse(self):
        item = Warehouse(name="test")
        assert item.name == "test"