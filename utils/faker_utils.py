

from faker import Faker


class FakerData:
    """
    Обертка над библиотекой Faker.

    Используется для централизованной генерации
    тестовых данных и избежания дублирования.
    """

    def __init__(self, locale: str = "ru_RU"):
        """
        Инициализация Faker с заданной локалью.

        :param locale: локаль для генерации данных
        """
        self._faker = Faker(locale)

    def username(self) -> str:
        """
        Генерирует случайное имя пользователя.
        """
        return self._faker.user_name()

    def password(self) -> str:
        """
        Генерирует случайный пароль.
        """
        return self._faker.password()
