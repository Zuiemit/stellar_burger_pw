from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url

    @allure.suite('Open page')
    def open_page(self, url):
        self.page.goto(url)

    @allure.step('Click on page')
    def click_on_elem(self, locator):
        self.page.click(selector=locator)

    @allure.step('Fill field')
    def fill_field(self, locator, text):
        self.page.fill(selector=locator, value=text)
