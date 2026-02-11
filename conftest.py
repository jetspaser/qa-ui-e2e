

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_data_test_attribute(playwright):
    """
    Устанавливает кастомный data-атрибут для всех тестов.

    После этого все методы playwright типа get_by_test_id()
    будут искать элементы по атрибуту "data-test" вместо стандартного.
    """
    playwright.selectors.set_test_id_attribute("data-test")
