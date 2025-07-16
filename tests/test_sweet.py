"""
Basic tests for Sweet entity.
Run with:  pytest
"""

import pytest
from src.sweet import Sweet


def test_string_representation():
    sweet = Sweet(1001, "Kaju Katli", "Nut‑Based", 50, 20)
    assert str(sweet) == "Kaju Katli (Nut‑Based) – ₹50 [20]"


def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        Sweet(1002, "Bad Chocolate", "Chocolate", -10, 5)


def test_negative_quantity_raises_error():
    with pytest.raises(ValueError):
        Sweet(1003, "Bad Candy", "Candy", 5, -1)
