from time import sleep
import allure
import pytest


@allure.title('Register user - UI Test')
@allure.description('UI Test Success registration')
@pytest.mark.register
def test_register_ui(register_page, assertions):
    register_page.open_register_page()
    register_page.fill_register_field()
    register_page.click_submit_btn()
    assertions.check_current_url(
        "https://stellarburgers.education-services.ru/login"
    )
