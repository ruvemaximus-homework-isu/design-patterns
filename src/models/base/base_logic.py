from abc import ABC, abstractmethod
from typing import Optional


class BaseLogic(ABC):
    """
    Класс для работы с базовой логикой приложения
    """

    __error: Optional[str] = None

    @property
    def error(self) -> Optional[str]:
        return (self.__error or "").strip()

    def has_error(self) -> bool:
        return self.__error is not None

    @abstractmethod
    def set_exception(self, ex: Exception):
        pass
