import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    # задаем опцию для запуска "браузер"
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # задаем опцию для запуска "язык"
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope='function')
def browser(request):
    # считываем язык и браузер
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        # инициализируем браузер chrome с нужными опциями
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == 'firefox':
        # инициализируем браузер firefox с нужными опциями
        print("\nstart firefox browser for test..")
        options = OptionsFirefox()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # закрытие браузера после работы
    print("\nquit browser..")
    browser.quit()
