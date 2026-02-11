

from playwright.sync_api import Page

class LoginPageElements:
    """
    Класс с локаторами страницы логина.
    Использует кастомный data-test атрибут.
    """

    def __init__(self, page: Page):
        self.username_input = page.get_by_test_id("username-field")
        self.password_input = page.get_by_test_id("password-field")
        self.submit_button = page.get_by_test_id("login-button")
        self.required_field_errors = page.get_by_test_id("required-field-error")
