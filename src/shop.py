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
