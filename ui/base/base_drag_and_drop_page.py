import allure
from playwright.sync_api import Page
from ui.base.base_page import BasePage


class BaseDragAndDropPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

    @allure.step("Перенести элемент")
    def drag_and_drop(self, source_locator: str, target_locator: str):
        source = self.page.locator(source_locator)
        target = self.page.locator(target_locator)
        source.drag_to(target)
