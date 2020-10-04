from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    login_link = "#login_link"

    def __int__(self, browser):
        BasePage.__init__(self, browser, MainPage.main_page_link)

    def go_to_login_page(self):
        login_link = self.find_element(By.CSS_SELECTOR, MainPage.login_link)
        login_link.click()
