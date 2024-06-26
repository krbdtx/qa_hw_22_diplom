import allure
from selene import browser, have

from sofrino_auto_test.test_data.data import Product


class FindProduct:

    @allure.step('Открыть браузер')
    def open_browser(self, url) -> object:
        browser.open(url)
        return self

    @allure.step("Заполнить поле поиска по товарам ")
    def find_product_low(self, value):
        browser.element('.topline__search__input').click()
        browser.element('#searchResultsInput').type(value).press_enter()
        return self

    @allure.step("Проверка результата поиска по товарам ")
    def should_find_product_low(self, value):
        browser.element('.container-header').should(
            have.exact_text(f'Товары по запросу "{value}"'))
        return self

    @allure.step("Проверка результата поиска по не существуюущим товарам ")
    def should_find_non_product_low(self):
        browser.element('.text-box').should(have.text('Нам не удалось найти товар по вашему запросу.'))
        return self


class StepsOnFindPages:

    @allure.step('Проверка работы с поиском по товарам')
    def find_product(self, value: Product):
        findp_roduct.open_browser(url='/')
        findp_roduct.find_product_low(value.product)
        return self

    @allure.step('Результат успешный поиска товара')
    def should_find_product(self, value: Product):
        findp_roduct.should_find_product_low(value.product)
        return self

    @allure.step('Результат не удалось найти товар')
    def should_find_non_product(self):
        findp_roduct.should_find_non_product_low()
        return self


steps_findp_roduct = StepsOnFindPages()
findp_roduct = FindProduct()
