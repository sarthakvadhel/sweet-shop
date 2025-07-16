from src.sweet import Sweet
from src.shop import SweetShop
import pytest

def test_add_sweet_successfully():
    shop = SweetShop()
    sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)

    shop.add_sweet(sweet)
    sweets = shop.view_sweets()

    assert len(sweets) == 1
    assert sweets[0].name == "Kaju Katli"
    assert sweets[0].price == 50


def test_add_duplicate_sweet_raises_error():
    shop = SweetShop()
    sweet1 = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
    sweet2 = Sweet(1001, "Duplicate Katli", "Nut-Based", 60, 10)

    shop.add_sweet(sweet1)

    with pytest.raises(ValueError):
        shop.add_sweet(sweet2)
