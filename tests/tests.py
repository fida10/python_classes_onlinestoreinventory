import unittest
from src.ans import StoreInventory

class TestStoreInventory(unittest.TestCase):
    def setUp(self):
        self.store = StoreInventory("BestStore")

    def test_add_product(self):
        self.store.add_product("Laptop", 10)
        self.assertIn("Laptop", self.store.inventory)
        self.assertEqual(self.store.inventory["Laptop"], 10)

    def test_remove_product(self):
        self.store.add_product("Mouse", 15)
        self.store.remove_product("Mouse")
        self.assertNotIn("Mouse", self.store.inventory)

    def test_check_stock(self):
        self.store.add_product("Keyboard", 20)
        self.assertEqual(self.store.check_stock("Keyboard"), 20)


if __name__ == '__main__':
    unittest.main()
