from .base_page import BasePage
import random
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    sign_up_email_input_locator = "id_registration-email"
    sign_up_password_input_locator = "id_registration-password1"
    confirm_sign_up_password_input_locator = "id_registration-password2"
    password_1 = "karandash123"
    sign_up_submit_locator = "registration_submit"


    def create_new_user(self):
        domen = ""
        email = ""
        for x in range(12):
            domen = domen + random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnm"))
            email = domen + "@" + "mail.ru"
        print(email)

        email_input = self.browser.find_element(By.ID, LoginPage.sign_up_email_input_locator)
        email_input.send_keys(email)
        password_input = self.browser.find_element(By.ID, LoginPage.sign_up_password_input_locator)
        password_input.send_keys(LoginPage.password_1)
        confirm_password_input = self.browser.find_element(By.ID, LoginPage.confirm_sign_up_password_input_locator)
        confirm_password_input.send_keys(LoginPage.password_1)
        confirm_registration_button = self.browser.find_element(By.NAME, LoginPage.sign_up_submit_locator)
        confirm_registration_button.click()

    def should_be_registration_form(self):
        assert self.browser.is_element_present(By.ID, "id_registration-redirect_url"), "Registration form is not presented"
