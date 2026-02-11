from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.login_page_elements import LoginPageElements


class LoginPage(BasePage):
    """
    Page Object для страницы логина YouTrack.
    Содержит методы взаимодействия с формой логина,
    валидацией обязательных полей и ошибками невалидных данных.
    """

    URL = "http://localhost:8080/hub/auth/login"

    def __init__(self, page):
        super().__init__(page)
        self.elements = LoginPageElements(page)

    def open(self) -> None:
        """
        Открывает страницу логина.
        """
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Заполняет поля логина и пароля и отправляет форму.
        """
        self.elements.username_input.fill(username)
        self.elements.password_input.fill(password)
        self.elements.submit_button.click()

    def submit(self) -> None:
        """
        Отправляет форму логина (кнопка Enter или Submit).
        """
        self.elements.submit_button.click()

    def make_fields_dirty(self) -> None:
        """
        Делает поля 'dirty', чтобы проявилась валидация.
        Нажимает, вводит любой текст и очищает его,
        затем уходит из поля (blur).
        """
        for field in (
            self.elements.username_input,
            self.elements.password_input,
        ):
            field.click()
            field.fill("a")
            field.fill("")
            field.press("Tab")

        # Небольшая пауза для того, чтобы UI успел отрисовать ошибки
        self.page.wait_for_timeout(200)

    def required_field_errors_count(self) -> int:
        """
        Возвращает количество видимых ошибок "Обязательно к заполнению".
        Ждёт появления первой ошибки до 2 секунд.
        """
        try:
            # Ждем появления хотя бы одного сообщения об ошибке
            self.elements
            self.elements.username_error.wait_for(state="visible", timeout=2000)
        except:
            # Если ошибки не появились
            return 0

        # Считаем общее количество ошибок полей
        return self.elements.required_field_errors.count()

    def is_invalid_credentials_error_visible(self) -> bool:
        """
        Проверяет, отображается ли ошибка при неверных учетных данных.
        Ждёт появления ошибки до 2 секунд.
        """
        try:
            self.elements.invalid_credentials_error.wait_for(
                state="visible", timeout=2000
            )
            return True
        except:
            return False
