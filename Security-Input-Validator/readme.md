Security Validator
https://img.shields.io/badge/python-3.8+-blue.svg
https://img.shields.io/badge/license-MIT-green.svg
https://img.shields.io/badge/status-active-success.svg
https://img.shields.io/badge/%D1%81%D1%82%D1%83%D0%B4%D0%B5%D0%BD%D1%82-1%2520%D0%BA%D1%83%D1%80%D1%81-brightgreen.svg

Валидатор безопасности на Python для обнаружения опасных паттернов в тексте.

Возможности
Обнаружение SQL-инъекций

Выявление XSS-атак

Защита от Path Traversal

Блокировка команд ОС

Логирование в JSON

Оценка уровня опасности

Быстрый старт
bash
git clone https://github.com/ваш-ник/security-validator.git
cd security-validator
python validator.py
Использование
Выберите "Проверить текст"

Введите текст для анализа

Получите результат

Пример:

text
Введите текст: ' OR '1'='1
НАЙДЕНО: SQL инъекция
УРОВЕНЬ ОПАСНОСТИ: ВЫСОКИЙ
Что проверяет
SQL-инъекции: ' OR ', UNION SELECT, DROP TABLE

XSS-атаки: <script>, javascript:, события onload/onerror

Команды ОС: ; rm, &&, |, `

Path Traversal: ../, ..\

Логирование
Все проверки сохраняются в security_logs.json

Лицензия
MIT License
