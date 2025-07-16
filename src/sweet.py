"""
sweet.py
---------
Domain entity representing a single sweet in the shop.
"""

class Sweet:
    """A simple value object for sweets."""

    def __init__(self, sweet_id: int, name: str,
                 category: str, price: float, quantity: int) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # ----- Dunder helpers ----------------------------------------------------
    def __str__(self) -> str:                           # human‑readable
        return f"{self.name} ({self.category}) – ₹{self.price} [{self.quantity}]"

    def __repr__(self) -> str:                          # unambiguous
        return (f"Sweet(id={self.id!r}, name={self.name!r}, "
                f"category={self.category!r}, price={self.price!r}, "
                f"quantity={self.quantity!r})")

    # ----- Equality & hashing (helps with tests, sets, dict keys) -----------
    def __eq__(self, other) -> bool:
        return isinstance(other, Sweet) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
