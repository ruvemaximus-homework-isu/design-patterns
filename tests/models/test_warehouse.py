import pytest

from src.models.warehouse import Warehouse


def test_warehouse():
    item = Warehouse(name="test")
    assert item.name == "test"