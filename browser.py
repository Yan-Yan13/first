from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.get('http://pizzeria.skillbox.cc/')
    yield driver
    driver.quit()

# from selenium.webdriver import Remote
# import pytest
#
#
# @pytest.fixture()
# def set_up_browser():
#    driver = Remote(desired_capabilities={
#        "browserName": "chrome",
#        "browserVersion": "latest"
#    }, command_executor="http://127.0.0.1:4444/wd/hub")
#    yield driver
#    driver.quit()
