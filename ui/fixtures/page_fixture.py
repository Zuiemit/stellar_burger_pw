import pytest
from playwright.sync_api import Page
from ui.base.base_assertions import Assertion
from ui.pages import RegisterPage, BasePage
from api.endpoints.endpoints import Url
from ui.pages.build_burger_page import BuildBurgerPage


@pytest.fixture
def register_page(page: Page):
    return RegisterPage(page, base_url=Url.BASE_URL)

@pytest.fixture
def assertions(page: Page):
    return Assertion(page, base_url=Url.BASE_URL)

@pytest.fixture
def build_burger_page(page: Page):
    return BuildBurgerPage(page, base_url=Url.BASE_URL)
