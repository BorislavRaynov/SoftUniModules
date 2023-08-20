from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self):
        self.fact = PaintFactory("Test", 10)

    def test_correct_init_data(self):
        self.assertEqual("Test", self.fact.name)
        self.assertEqual(10, self.fact.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.fact.valid_ingredients)
        self.assertEqual({}, self.fact.products)

    def test_can_add_with_invalid_data(self):
        self.fact.ingredients = {"black": 9}
        result = self.fact.can_add(2)

        self.assertEqual(False, result)

    def test_can_add_with_valid_data(self):
        self.fact.ingredients = {"black": 8}
        result = self.fact.can_add(2)

        self.assertEqual(True, result)

    def test_can_add_with_valid_data_positive(self):
        self.fact.ingredients = {"black": 7}
        result = self.fact.can_add(2)

        self.assertEqual(True, result)

    def test_add_not_valid_product_raises(self):

        with self.assertRaises(TypeError) as te:
            self.fact.add_ingredient("black", 5)

        self.assertEqual(f"Ingredient of type black not allowed in PaintFactory", str(te.exception))

    def test_add_with_valid_product_not_have_room_raises(self):
        self.fact.ingredients = {"black": 9}

        with self.assertRaises(ValueError) as ve:
            self.fact.add_ingredient("black", 2)

        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_can_add_not_existing_product_correct(self):
        self.fact.ingredients = {"black": 6}
        self.fact.add_ingredient("red", 2)

        self.assertEqual({"black": 6, "red": 2}, self.fact.ingredients)
        self.assertEqual({"black": 6, "red": 2}, self.fact.products)

    def test_can_add_existing_product_update_qty(self):
        self.fact.ingredients = {"black": 6}
        self.fact.add_ingredient("black", 2)

        self.assertEqual({"black": 8}, self.fact.ingredients)
        self.assertEqual({"black": 6}, self.fact.products)

    def test_remove_not_existing_product_raises(self):
        self.fact.ingredients = {"black": 6}

        with self.assertRaises(KeyError) as ke:
            self.fact.remove_ingredient("red", 2)

        self.assertEqual("No such ingredient in the factory", str(ke.exception))

    def test_remove_more_than_have_qty_raises(self):
        self.fact.ingredients = {"black": 6}

        with self.assertRaises(ValueError) as ve:
            self.fact.remove_ingredient("black", 7)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_correct_remove_product_correct(self):
        self.fact.ingredients = {"black": 6, "red": 2}

        self.fact.remove_ingredient("black", 6)

        self.assertEqual({"black": 0, "red": 2}, self.fact.products)
        self.assertEqual({"black": 0, "red": 2}, self.fact.ingredients)

    def test__repr__correct(self):
        self.fact.ingredients = {"black": 6, "red": 2}

        result = str(self.fact)
        expected = f"Factory name: Test with capacity 10.\nblack: 6\nred: 2\n"

        self.assertEqual(expected, result)
