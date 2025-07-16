"""
shop.py
--------
Handles sweet inventory operations like add, view, etc.
"""

from src.sweet import Sweet

class SweetShop:
    def __init__(self):
        self._inventory = {}

    def add_sweet(self, sweet: Sweet):
        """Adds a sweet to inventory. If it exists, raises an error."""
        if sweet.id in self._inventory:
            raise ValueError("Sweet with this ID already exists.")
        self._inventory[sweet.id] = sweet

    def view_sweets(self):
        """Returns a list of all available sweets."""
        return list(self._inventory.values())
