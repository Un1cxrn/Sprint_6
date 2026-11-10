 Sprint 6 — Автотесты для Яндекс.Самокат

Проект содержит UI-тесты для учебного сервиса Яндекс.Самокат(https://qa-scooter.praktikum-services.ru/).


 Структура проекта
- 'pages/' — Page Object классы ('MainPage', 'OrderPage')
- 'tests/' — Тесты ('test_order.py', 'test_questions.py')
- 'conftest.py' — Фикстура запуска браузера
- 'pytest.ini' — Настройки pytest

 Установка и запуск

1. Установи зависимости:
   ```bash
   pip install -r requirements.txt