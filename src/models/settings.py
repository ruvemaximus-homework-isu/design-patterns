from pydantic import BaseModel, Field


class Settings(BaseModel):
    """
    Настройки
    """

    inn: str = Field(max_length=12, description="ИНН")
    account: str = Field(max_length=11, description="Счёт")
    organization_name: str = Field(max_length=255, description="Название организации")
    bik: str = Field(max_length=9, description="БИК")
    correspondent_account: str = Field(max_length=11, description="Корреспондентский счёт")
    type_of_property: str = Field(max_length=5, description="Вид собственности")

    class Config:
        validate_assignment = True

    def __eq__(self, other):
        return (
            self.inn == other.inn
            and self.account == other.account
            and self.organization_name == other.organization_name
            and self.bik == other.bik
            and self.correspondent_account == other.correspondent_account
            and self.type_of_property == other.type_of_property
        )
