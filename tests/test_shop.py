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

def test_delete_existing_sweet():
    shop = SweetShop()
    sweet = Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50)
    shop.add_sweet(sweet)
    shop.delete_sweet(1002)
    assert len(shop.view_sweets()) == 0

def test_delete_nonexistent_sweet_raises_error():
    shop = SweetShop()
    with pytest.raises(ValueError):
        shop.delete_sweet(9999)

def test_search_by_name():
    shop = SweetShop()
    shop.add_sweet(Sweet(1, "Kaju Katli", "Nut-Based", 50, 10))
    shop.add_sweet(Sweet(2, "Gulab Jamun", "Milk-Based", 30, 20))

    results = shop.search_sweets(name="katli")
    assert len(results) == 1
    assert results[0].name == "Kaju Katli"

def test_search_by_category():
    shop = SweetShop()
    shop.add_sweet(Sweet(3, "Gajar Halwa", "Veg-Based", 20, 5))
    shop.add_sweet(Sweet(4, "Rasgulla", "Milk-Based", 25, 12))

    results = shop.search_sweets(category="Milk-Based")
    assert len(results) == 1
    assert results[0].name == "Rasgulla"

def test_search_by_price_range():
    shop = SweetShop()
    shop.add_sweet(Sweet(5, "Barfi", "Nut-Based", 60, 8))
    shop.add_sweet(Sweet(6, "Ladoo", "Gram-Based", 15, 25))

    results = shop.search_sweets(min_price=10, max_price=50)
    assert len(results) == 1
    assert results[0].name == "Ladoo"

def test_purchase_sweet_success():
    shop = SweetShop()
    sweet = Sweet(1010, "Ladoo", "Gram-Based", 15, 10)
    shop.add_sweet(sweet)
    shop.purchase_sweet(1010, 3)
    assert sweet.quantity == 7

def test_purchase_more_than_stock_raises_error():
    shop = SweetShop()
    sweet = Sweet(1011, "Barfi", "Nut-Based", 50, 5)
    shop.add_sweet(sweet)
    with pytest.raises(ValueError):
        shop.purchase_sweet(1011, 10)

def test_purchase_nonexistent_sweet_raises_error():
    shop = SweetShop()
    with pytest.raises(ValueError):
        shop.purchase_sweet(9999, 1)

def test_restock_sweet_success():
    shop = SweetShop()
    sweet = Sweet(1020, "Jalebi", "Sugar-Based", 12, 10)
    shop.add_sweet(sweet)

    shop.restock_sweet(1020, 5)
    assert sweet.quantity == 15


def test_restock_nonexistent_sweet_raises_error():
    shop = SweetShop()
    with pytest.raises(ValueError):
        shop.restock_sweet(8888, 5)
