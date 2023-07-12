TASK №28

Объект тестирования: https://b2c.passport.rt.ru

***
* [config.py](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/config.py) — переменные используемые в проекте;
* [README.md](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/README.md) — содержит информацию о проекте;
* [requirements.txt](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/requirements.txt) — содержит требования к версиям.
* [test_authorization_interface.py](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/tests/test_authorization_interface.py) - файл автотестов;
* [conftest.py](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/tests/conftest.py) — условия для выполнения тестовых задач.
* [locators.py](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/pages/locators.py) — содержит описание локаторов проекта;
* [base_page.py](https://github.com/DenisZhutaev/Final_work_QAP1031/blob/master/pages/base_page.py) — содержит базовые функции и методы.
* базовые требования от Заказчика прикреплены отдельным файлом

* [Test_cases&bugs](https://docs.google.com/spreadsheets/d/1V4PyTFD7Q12WPleeteiedlJzJGOlK8BuoGLdENxyi5A/edit?usp=sharing)

Техники тест-дизайна: 
 
* эквивалентное разбитие
* анализ граничных значений

Инструменты тестирования:

* [Selenium](https://www.selenium.dev/); DevTools, [ChroPath](https://chrome.google.com/webstore/detail/chropath/ljngjbnaijcbncmcnjfhigebomdlkcjo), PyCharm Community Edition 2022.3.2. 

Как запустить тесты:
1. установить все библиотеки и зависимости: `pip install -r requirements.txt`;
2. загрузите [Selenium WebDriver](https://chromedriver.chromium.org/downloads) → Выбрать совместимую версию → прописать путь к драйверу в переменную PATH в файле config.py;
3. запустить тест: `python -m pytest -v --driver Chrome --driver-path 28/interface_test.py`.
