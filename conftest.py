from trace import Trace
import requests
import allure
import pytest
from ui.fixtures.page_fixture import register_page, assertions, build_burger_page
from ui.fixtures.auth_fixture import new_user, auth_tokens


@pytest.fixture(autouse=True)
def browser_conftest(browser_context_args):
    viewport = {'width': 1680, 'height': 1080}
    args = {
            **browser_context_args,
            'ignore_https_errors': True,
            'viewport': viewport,
        }
    return args
