

"""
UI-тесты аутентификации YouTrack.

Проверяется:
- успешная авторизация
- валидация обязательных полей
- обработка невалидных учетных данных

Тесты написаны с использованием Playwright + pytest.
"""

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


class TestLogin:
    """
    Набор UI-тестов для страницы логина YouTrack.
    """

    DASHBOARD_TITLE = "YouTrack Default Панель мониторинга"
    INVALID_CREDENTIALS_ERROR = "Некорректное имя пользователя или пароль."

    # -------------------------
    # POSITIVE
    # -------------------------

    def test_login_success(self, page: Page) -> None:
        """
        Успешная авторизация с валидными учетными данными.
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.login(username="admin", password="admin")

        expect(page).to_have_title(self.DASHBOARD_TITLE)

    # -------------------------
    # NEGATIVE
    # -------------------------

    def test_login_empty_fields(self, page: Page) -> None:
        """
        Попытка входа с пустыми полями.

        Ошибка обязательного поля отображается
        только после того, как поля становятся 'dirty'.
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.make_fields_dirty()
        login_page.submit()

        assert login_page.required_field_errors_count() == 2

    def test_login_invalid_credentials(self, page: Page) -> None:
        """
        Попытка входа с невалидными учетными данными.
        """
        login_page = LoginPage(page)

        login_page.open()
        login_page.login(username="invalid_user", password="invalid_password")

        assert login_page.is_invalid_credentials_error_visible(
            self.INVALID_CREDENTIALS_ERROR
        )
