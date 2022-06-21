import allure
from selene.support.shared import browser
from selene import by, be, have


def test_google():
    with allure.step("Открыть страницу поиска"):
        browser.open('https://google.com/ncr')
    with allure.step("Найти по слову selenium"):
        browser.element(by.name('qq')).should(be.blank).type('selenium').press_enter()
    with allure.step("Проверить, что в первой статье есть текст 'Selenium automates browsers'"):
        browser.all('.g').first.should(have.text('Selenium automates browsers'))