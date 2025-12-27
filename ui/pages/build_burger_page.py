from ui.base.base_drag_and_drop_page import BaseDragAndDropPage
from playwright.sync_api import Page, expect
import allure
from ui.locators.build_burger_locators import BuildBurgerLocators, BurgerElemName
from api.endpoints.endpoints import Url


class BuildBurgerPage(BaseDragAndDropPage):

    def __init__(self, page:Page, base_url):
        super().__init__(page, base_url)

    @allure.step('Open burger page')
    def open_burger_page(self):
        self.open_page(f'{Url.BASE_URL}')

    @allure.step("Перенести булочку")
    def drag_and_drop_burger(self):
        self.drag_and_drop(
            BuildBurgerLocators.CRATOR_BURGER_BUN,
            BuildBurgerLocators.BUSKET_LIST,
        )

    @allure.step("Перенести соус")
    def drag_and_drop_sauce(self):
        self.drag_and_drop(
            BuildBurgerLocators.SPICY_SAUCE_X,
            BuildBurgerLocators.BUSKET_LIST,
        )

    def get_total_price(self) -> int:
        text = self.page.locator(BuildBurgerLocators.TOTAL_PRICE).inner_text()
        return int(text.strip())

    @allure.step("Проверить, что сумма заказа = {expected}")
    def assert_total_price_equals(self, expected: int):
        total = self.page.locator(BuildBurgerLocators.TOTAL_PRICE)
        expect(total).to_have_text(str(expected))
