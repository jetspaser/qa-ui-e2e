

"""
UI-тесты аутентификации YouTrack.

Проверяется:
- успешная авторизация
- валидация обязательных полей
- обработка невалидных учетных данных

Тесты написаны с использованием Playwright + pytest.
"""

import pytest
from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()


class TestLogin:

    LOGIN_URL = "http://localhost:8080/hub/auth/login"

    DASHBOARD_TITLE = "YouTrack Default Панель мониторинга"
    REQUIRED_FIELD_ERROR = "Необходимо указать значение"
    INVALID_CREDENTIALS_ERROR = "Некорректное имя пользователя или пароль."

    # -------------------------
    # POSITIVE
    # -------------------------

    def test_login_success(self, page: Page) -> None:
        """
        Успешная авторизация с валидными данными
        """
        self.open_login_page(page)
        self.login_as_admin(page)

        expect(page).to_have_title(self.DASHBOARD_TITLE)

    # -------------------------
    # NEGATIVE
    # -------------------------

    def test_login_empty_fields(self, page: Page) -> None:
        """
        Попытка входа с пустыми полями
        """
        self.open_login_page(page)
        self.submit_login(page)

        error = page.locator("text=Необходимо указать значение")
        expect(error).to_be_visible()

    def test_login_invalid_credentials(self, page: Page) -> None:
        """
        Попытка входа с невалидными учетными данными
        """
        self.open_login_page(page)

        self.fill_username(page, fake.user_name())
        self.fill_password(page, fake.password())
        self.submit_login(page)

        error = page.locator(f"text={self.INVALID_CREDENTIALS_ERROR}")
        expect(error).to_be_visible()

    # -------------------------
    # HELPERS
    # -------------------------

    def open_login_page(self, page: Page) -> None:
        page.goto(self.LOGIN_URL)

    def fill_username(self, page: Page, username: str) -> None:
        page.locator('[data-test="username-field"]').fill(username)

    def fill_password(self, page: Page, password: str) -> None:
        page.locator('[data-test="password-field"]').fill(password)

    def submit_login(self, page: Page) -> None:
        page.locator('[data-test="login-button"]').click()

    def login_as_admin(self, page: Page) -> None:
        self.fill_username(page, "admin")
        self.fill_password(page, "admin")
        self.submit_login(page)

    def test_login_empty_fields(self, page: Page) -> None:
        """
        Попытка входа с пустыми полями.
        Ошибка появляется только после того, как поля становятся 'dirty'.
        """
        self.open_login_page(page)

        username = page.locator('[data-test="username-field"]')
        password = page.locator('[data-test="password-field"]')

        # Делаем поля dirty
        username.click()
        username.fill("a")
        username.fill("")
        password.click()
        password.fill("a")
        password.fill("")

        self.submit_login(page)

        error = page.locator(f"text={self.REQUIRED_FIELD_ERROR}")
        expect(error).to_have_count(2)  # 2 ошибки: username + password

