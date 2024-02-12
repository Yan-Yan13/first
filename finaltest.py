import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.browser import set_up_browser


@allure.feature("Final test")
@allure.story("First tests")
class TestCase:
    @allure.title("добавление товара в корзину")
    def test_case_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]'
        ).click()

    @allure.title("удалить товар из корзины")
    def test_case_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[class="remove"]').click()

    @allure.title("изменить кол-во товара в корзине")
    def test_case_3(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[type="number"]').click().send_keys(
            "2" + Keys.ENTER
        )

    @allure.title("в карточку товара")
    def test_case_4(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(By.CSS_SELECTOR, '[title="Подробнее"]').click()

    @allure.title("строка поиска")
    def test_case_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[name="s"]').click()
        driver.find_element(By.CSS_SELECTOR, '[type="number"]').click().send_keys(
            "десерт" + Keys.ENTER
        )

    @allure.title("выбор товара с условиями")
    def test_case_6(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(
            By.CSS_SELECTOR,
            '[href="http://pizzeria.skillbox.cc/product-category/menu/"]',
        ).hover()
        driver.find_element(
            By.CSS_SELECTOR,
            '[href="http://pizzeria.skillbox.cc/product-category/menu/deserts/"]',
        ).click()
        el = driver.find_element(
            By.XPATH, '(//*[contains(@class, "ui-slider-handle")])[2]'
        )
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(el).move_by_offset(
            xoffset=-350, yoffset=0
        ).perform()
        action_chains.release().perform()
        driver.find_element(By.XPATH, '(// *[contains( @ type, "submit")])[2]').click()

    @allure.title("изменения бортика пиццы")
    def test_case_7(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[title="Пицца «4 в 1»"]').click()
        driver.find_element(By.CSS_SELECTOR, '[value="65.00"]').click()

    @allure.title("применение промокода")
    def test_case_8(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[name="coupon_code"]').click().send_keys(
            "GIVEMEHALYAVA" + Keys.ENTER
        )

    @allure.title("применение промокода дважды")
    def test_case_9(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(By.CSS_SELECTOR, '[href="?add-to-cart=423"]').click()
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/cart/"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[name="coupon_code"]').click().send_keys(
            "GIVEMEHALYAVA" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[name="coupon_code"]').click().send_keys(
            "GIVEMEHALYAVA" + Keys.ENTER
        )

    @allure.title("регистрация аккаунта")
    def test_case_10(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[class ="custom-register-button"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[name="username"]').click().send_keys(
            "Jan" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[type="email"]').click().send_keys(
            "Zy@yandex.ru" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[name="password"]').click().send_keys(
            "123qwe!" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[name="register"]').click()

    @allure.title("оформлени доставки")
    def test_case_11(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(
            By.CSS_SELECTOR, 'href="http://pizzeria.skillbox.cc/cart/"'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[id="billing_first_name"]'
        ).click().send_keys("Jan")
        driver.find_element(
            By.CSS_SELECTOR, '[id="billing_last_name"]'
        ).click().send_keys("Ivanov")
        driver.find_element(
            By.CSS_SELECTOR, '[id="billing_address_1_field"]'
        ).click().send_keys("Lenina")
        driver.find_element(
            By.CSS_SELECTOR, '[id="billing_city_field"]'
        ).click().send_keys("Petrozavodsk")
        driver.find_element(By.CSS_SELECTOR, '[id="billing_state]').click().send_keys(
            "Severo-Zapad"
        )
        driver.find_element(
            By.CSS_SELECTOR, '[id="billing_postcode_field"]'
        ).click().send_keys("185000")
        driver.find_element(By.CSS_SELECTOR, '[id="billing_phone"]').click().send_keys(
            "+79112223344"
        )
        driver.find_element(By.CSS_SELECTOR, '[name="terms"]').click()
        driver.find_element(By.CSS_SELECTOR, '[id="place_order"]').click()

    @allure.title("оформлени заказа")
    def test_case_12(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://pizzeria.skillbox.cc/")
        driver.find_element(
            By.CSS_SELECTOR, '[href="http://pizzeria.skillbox.cc/my-account/"]'
        ).click()
        driver.find_element(By.CSS_SELECTOR, '[name="username"]').click().send_keys(
            "Zy@yandex.ru" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[name="password"]').click().send_keys(
            "123qwe!" + Keys.ENTER
        )
        driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
