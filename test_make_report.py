from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# 1. Registration

def test_sign_up(browser):

    # Data
    success_sigh_up_message = "Спасибо за регистрацию!"
    success_message_locator = "alertinner"

    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.create_new_user()

    # Assert
    success_message = browser.find_element_by_class_name(success_message_locator)
    assert success_sigh_up_message in success_message.text, \
        "Sign up page should contain valid success message" % (success_message, success_sigh_up_message)
