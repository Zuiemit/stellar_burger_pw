import allure
import pytest


@allure.title('Register user')
@allure.description('Success registration')
@pytest.mark.api
def test_register_user(new_user):
    assert new_user["accessToken"].startswith("Bearer ")
    assert "@example.com" in new_user["email"]

@allure.title('Login')
@allure.description('Success login')
@pytest.mark.api
def test_login_user(auth_tokens):
    assert auth_tokens["success"] is True
    assert auth_tokens["accessToken"].startswith("Bearer ")
    assert len(auth_tokens["accessToken"]) > 50
