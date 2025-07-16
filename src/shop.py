"""
shop.py
--------
Handles sweet inventory operations like add, view, etc.
"""

from src.sweet import Sweet

class SweetShop:
    def __init__(self):
        self._inventory = {}

    def add_sweet(self, sweet):
        if sweet.id in self._inventory:
            raise ValueError("Sweet with this ID already exists.")
        self._inventory[sweet.id] = sweet

    def view_sweets(self):
        return list(self._inventory.values())

    def delete_sweet(self, sweet_id):
        if sweet_id not in self._inventory:
            raise ValueError("Sweet not found.")
        del self._inventory[sweet_id]

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        results = self._inventory.values()

        if name:
            results = [s for s in results if name.lower() in s.name.lower()]
        if category:
            results = [s for s in results if category.lower() == s.category.lower()]
        if min_price is not None:
            results = [s for s in results if s.price >= min_price]
        if max_price is not None:
            results = [s for s in results if s.price <= max_price]

        return results

    def purchase_sweet(self, sweet_id, quantity):
        if sweet_id not in self._inventory:
            raise ValueError("Sweet not found.")
        sweet = self._inventory[sweet_id]
        if quantity > sweet.quantity:
            raise ValueError("Not enough stock available.")
        sweet.quantity -= quantity

    def restock_sweet(self, sweet_id, quantity):
        """Increase quantity of a sweet."""
        if sweet_id not in self._inventory:
            raise ValueError("Sweet not found.")
        self._inventory[sweet_id].quantity += quantity
