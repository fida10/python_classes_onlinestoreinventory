""" 
Question 3: Online Store Inventory

Description:

Create a class called StoreInventory. It should have the following attributes and methods:

Attributes: store_name (string) and inventory (dictionary with product names as keys and quantities as values).

Methods:

add_product(product_name, quantity): Adds or updates a product in the inventory.

remove_product(product_name): Removes a product from the inventory.

check_stock(product_name): Returns the quantity of the specified product.
"""

class StoreInventory:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = {}
    
    def add_product(self, item, quantity):
        self.inventory[item] = quantity
    
    def remove_product(self, item):
        self.inventory.pop(item)
        
    def check_stock(self, item):
        return self.inventory[item]