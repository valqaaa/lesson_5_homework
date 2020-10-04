from selenium.webdriver.common.by import By

class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_link = (By.LINK_TEXT, "login")
    login_form = (By.ID, "id_login-redirect_url")
    registration_form = (By.ID, "id_registration-redirect_url")
