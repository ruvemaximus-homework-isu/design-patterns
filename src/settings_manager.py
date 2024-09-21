import json
from pathlib import Path

from pydantic import ValidationError

from src.core.singleton import Singleton
from src.models.settings import Settings

BASE_DIR = Path(__file__).resolve().parent


class SettingsManager(metaclass=Singleton):
    """
    Менеджер настроек
    """

    __file_name = "settings.json"
    __settings: Settings = None

    def __init__(self) -> None:
        if self.__settings is None:
            self.__settings = self.__default_setting()

    def open(self, file_name: str = ""):
        """
        Открыть и загрузить настройки
        """

        if not isinstance(file_name, str):
            raise TypeError("Некорректно переданы параметры!")

        file_name = file_name or self.__file_name

        try:
            with open(BASE_DIR / file_name) as stream:
                data = json.load(stream)
            self.__settings = self._convert(data)
            return True

        except ValidationError as e:
            print(f"Validation error while loading settings: {e}. Using default settings.")
            self.__settings = self.__default_setting()
            return False

        except Exception as e:
            print(f"Unexpected error while loading settings: {e}. Using default settings.")
            self.__settings = self.__default_setting()
            return False

    def _convert(self, data: dict):
        """
        Конвертирует словарь в настройки
        """

        return Settings(**data)

    @property
    def current_settings(self) -> Settings:
        """
        Загруженные настройки
        """

        return self.__settings

    def __default_setting(self) -> Settings:
        """
        Набор настроек по умолчанию
        """

        return Settings(
            inn="380080920202",
            account="DEFAULT",
            organization_name="Рога и копыта (default)",
            bik="DEFAULT",
            correspondent_account="DEFAULT",
            type_of_property="12345",
        )
