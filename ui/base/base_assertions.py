from playwright.sync_api import Page, expect
import allure
from ui.base.base_page import BasePage


class Assertion(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step('Check current url')
    def check_current_url(self, url):
        expect(self.page).to_have_url(url)
