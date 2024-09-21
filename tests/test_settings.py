import unittest

from src.settings_manager import SettingsManager


class SettingsTestCase(unittest.TestCase):
    """
    Набор тестов для проверки работы с настройками
    """

    def test_settings_manager_open(self):
        """
        Проверить открытие и загрузку настроек
        """

        manager = SettingsManager()

        result = manager.open("../settings.json")

        assert result is True

    def test_settings_manager_singletone(self):
        """
        Проверить работу шаблона singletone
        """
        manager1 = SettingsManager()
        manager1.open("../settings.json")

        manager2 = SettingsManager()

        assert manager1.current_settings == manager2.current_settings
