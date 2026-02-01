# QA UI E2E  
Репозиторий с **end-to-end UI-тестами** для YouTrack на стеке Python + Playwright

Текущий фокус - сценарии авторизации, проверка ошибок валидации и негативные кейсы с невалидными данными (с помощью Faker).

---

## 🔹 Tech Stack

<div style="display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0;">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=playwright&logoColor=white)
![Page Object](https://img.shields.io/badge/Page%20Object-in%20progress-orange?style=for-the-badge)
![Allure](https://img.shields.io/badge/Allure-planned-orange?style=for-the-badge)

</div>

**Планируется в будущем:**
- Полноценная Page Object Model / Screenplay
- Allure-отчёты
- Переиспользование сессий / контекста
- Параметризация тестов
- CI (GitHub Actions)

---

## 🔹 Установка

```bash
# 1. Клонируем репозиторий
git clone https://github.com/jetspaser/qa-ui-e2e.git
cd qa-ui-e2e

# 2. Создаём и активируем виртуальное окружение
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Устанавливаем браузеры Playwright (chromium, firefox, webkit)
playwright install

Важно: создай файл .env в корне проекта (или задай переменные окружения):
YOUTRACK_URL=https://your-youtrack-instance.cloud
YOUTRACK_LOGIN=admin@example.com
YOUTRACK_PASSWORD=your-strong-password

---

# Все тесты логина (рекомендуемый вариант)
pytest tests/ui/test_login.py -v

# С видимым браузером (headed mode)
pytest tests/ui/test_login.py --headed -v

# С выводом print / логов в консоль
pytest tests/ui/test_login.py --headed -s

# Только упавшие + короткий traceback
pytest --tb=short

# С трассировкой (очень полезно при дебаге)
pytest --tracing=on

---

```

🔹 Покрываемые сценарии

Успешная авторизация
→ Ввод валидных логина и пароля
→ Проверка, что загрузилась главная страница (дашборд)
Пустые поля
→ Пустой username → ошибка «Необходимо указать значение»
→ Пустой password → ошибка «Необходимо указать значение»
Невалидные данные (Faker)
→ Случайно сгенерированные логин и пароль
→ Ожидаемая ошибка «Некорректное имя пользователя или пароль»

---

🔹 Helpers / Утилиты
В conftest.py и тестах используются вспомогательные методы для читаемости:

open_login_page(page)
fill_username(page, username)
fill_password(page, password)
submit_login(page)
login_as_admin(page) (для быстрого логина валидным пользователем)

Это позволяет писать тесты в декларативном стиле без дублирования кода.
