from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self):
        self.cart = ShoppingCart("Test", 100)

    def test_init_data(self):
        self.assertEqual("Test", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_set_name_with_lower_case_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "test"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_set_name_with_non_alpha_letter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "158/ asd+-*"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_more_expensive_product_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Bmw", 101)

        self.assertEqual("Product Bmw cost too much!", str(ve.exception))

    def test_successfully_add_product_to_cart(self):
        result = self.cart.add_to_cart("apples", 50)

        self.assertEqual({"apples": 50}, self.cart.products)
        self.assertEqual("apples product was successfully added to the cart!", result)

    def test_remove_not_existing_product_raises(self):
        self.cart.add_to_cart("apples", 50)

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("bananas")

        self.assertEqual("No product with name bananas in the cart!", str(ve.exception))

    def test_successful_remove_product_(self):
        self.cart.add_to_cart("apples", 50)
        self.cart.add_to_cart("bananas", 20)

        result = self.cart.remove_from_cart("bananas")

        self.assertEqual({"apples": 50}, self.cart.products)
        self.assertEqual("Product bananas was successfully removed from the cart!", result)

    def test__add__method_creates_new_cart(self):
        self.cart.add_to_cart("apples", 50)
        self.cart.add_to_cart("bananas", 20)
        cart_2 = ShoppingCart("Testing", 150)
        cart_2.add_to_cart("cabbage", 30)

        cart_3 = self.cart.__add__(cart_2)

        self.assertEqual("TestTesting", cart_3.shop_name)
        self.assertEqual(250, cart_3.budget)
        expected_products = {
            "apples": 50, "bananas": 20, "cabbage": 30
        }
        self.assertEqual(expected_products, cart_3.products)

    def test_buy_expensive_products_raises(self):
        self.cart.add_to_cart("apples", 50)
        self.cart.add_to_cart("bananas", 51)

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 1.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_successful_bought_products(self):
        self.cart.add_to_cart("apples", 50)
        self.cart.add_to_cart("bananas", 50)

        result = self.cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 100.00lv.'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
