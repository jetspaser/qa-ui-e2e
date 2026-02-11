

from playwright.sync_api import Page


class BasePage:
    """
    Базовый класс для всех Page Object.

    Содержит общую логику работы со страницей:
    - хранение объекта Playwright Page
    - базовые действия, не привязанные к конкретной странице
    """

    def __init__(self, page: Page):
        """
        Инициализация базовой страницы.

        :param page: объект страницы Playwright
        """
        self.page = page

    def open(self, url: str) -> None:
        """
        Открывает переданный URL в браузере.

        :param url: адрес страницы
        """
        self.page.goto(url)
