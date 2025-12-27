class BurgerElemName:
    CRATOR_BURGER = "Краторная булка N-200i"
    SPICY_SAUCE_X = "Соус Spicy-X"

class BuildBurgerLocators:
    CRATOR_BURGER_BUN = "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']"
    SPICY_SAUCE_X = "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']"
    BUSKET_LIST = "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    TOTAL_PRICE = "//p[contains(@class,'text_type_digits-medium')]"
