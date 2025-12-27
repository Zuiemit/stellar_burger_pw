from ui.base.base_page import BasePage
from playwright.sync_api import Page, expect
import allure
from ui.locators.register_page_locators import RegisterPageLocators
from api.endpoints.endpoints import Url
import uuid


class RegisterPage(BasePage):

    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)

    @allure.step('Open register page')
    def open_register_page(self):
        self.open_page(f'{Url.BASE_URL}{Url.REGISTER_URL}')

    @allure.step('Fill field on register page')
    def fill_register_field(self):
        self.fill_field(locator=RegisterPageLocators.NAME_FIELD, text='Andrey')
        self.fill_field(locator=RegisterPageLocators.EMAIL_FIELD, text=f'andrey{uuid.uuid4().hex[:8]}@gmail.com')
        self.fill_field(locator=RegisterPageLocators.PASSWORD_FIELD, text='123qwezxc')

    @allure.step('click on register button')
    def click_submit_btn(self):
        self.click_on_elem(locator=RegisterPageLocators.SUBMIT_BTN)
