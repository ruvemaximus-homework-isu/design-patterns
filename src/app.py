"""Точка входа приложения"""

from src.models.base.base_logic import BaseLogic


class StartService(BaseLogic):
    """Сервис запуска приложения"""

    # TODO добавить DataRepository
    __repository: None

    def __create_nomenclature_groups(self):
        """Сформировать группы номенклатуры"""

        # TODO

        # list = []
        # list.append(group_model.default_group_cold())
        # list.append(group_model.default_group_source())
        # self.__reposity.data[data_reposity.group_key()] = list

    def create_receipts(self) -> None:
        """Формирование рецептов"""

    def create(self):
        """Метод генерации данных"""

        # TODO Метод должен формировать и сохранять данные по:
        # - Номенклатуре
        # - Единицам измерения
        # - Группам

        self.__create_nomenclature_groups()
