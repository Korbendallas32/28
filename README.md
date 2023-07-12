TASK №28

Объект тестирования: https://b2c.passport.rt.ru

***
* [config.py](https://github.com/Korbendallas32/28/blob/main/config.py) — используемые переменные;
* [README.md](https://github.com/Korbendallas32/28/blob/main/README.md) — содержит информацию о проекте;
* [requirements.txt](https://github.com/Korbendallas32/28/blob/main/requirements) — содержит требования к версиям.
* [interface_test.py](https://github.com/Korbendallas32/28/blob/main/interface_test.py) - файл автотестов;
* [conftest.py](https://github.com/Korbendallas32/28/blob/main/conftest.py) — условия для выполнения тестовых задач.
* [locators.py](https://github.com/Korbendallas32/28/blob/main/locators.py) — описание локаторов;
* [base_page.py](https://github.com/Korbendallas32/28/blob/main/base_page.py) — базовые функции и методы.
* базовые требования от Заказчика прикреплены отдельным файлом

* [Test_cases&bugs](https://docs.google.com/spreadsheets/d/1V4PyTFD7Q12WPleeteiedlJzJGOlK8BuoGLdENxyi5A/edit?usp=sharing)

Техники тест-дизайна: 
 
* эквивалентное разбитие
* анализ граничных значений

Инструменты тестирования:

* [Selenium](https://www.selenium.dev/); DevTools, [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo), PyCharm Community Edition 2022.3.2. 

Как запустить тесты:
1. установить все библиотеки и зависимости: `pip install -r requirements.txt`;
2. загрузите [Selenium WebDriver](https://chromedriver.chromium.org/downloads) → Выбрать совместимую версию → Gрописать путь к драйверу в переменную PATH в файле config.py;
3. запустить тест: `python -m pytest -v --driver Chrome --driver-path 28/interface_test.py`.
