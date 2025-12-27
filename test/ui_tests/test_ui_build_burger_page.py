from time import sleep
import allure
import pytest
from ui.data.burger_prices import CRATOR_PRICE, SPICY_SAUCE_PRICE


@allure.title('Build burger - UI Test')
@allure.description('UI Test Success build burger')
@pytest.mark.register
def test_build_burger_ui(build_burger_page, assertions):
    expected_total = 0
    build_burger_page.open_burger_page()
    build_burger_page.drag_and_drop_burger()
    build_burger_page.drag_and_drop_burger()
    expected_total = 2 * CRATOR_PRICE
    build_burger_page.assert_total_price_equals(expected_total)
    build_burger_page.drag_and_drop_sauce()
    expected_total += SPICY_SAUCE_PRICE
    build_burger_page.assert_total_price_equals(expected_total)
