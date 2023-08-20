from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.p = PetShop("Test")

    def test_init_valid_data(self):
        self.assertEqual("Test", self.p.name)
        self.assertEqual({}, self.p.food)
        self.assertEqual([], self.p.pets)

    def test_add_food_with_zero_quantity_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.p.add_food("cat_food", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_with_negative_quantity_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.p.add_food("cat_food", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_not_existing_food(self):
        result = self.p.add_food("cat_food", 10)

        self.assertEqual({"cat_food": 10}, self.p.food)
        self.assertEqual(f"Successfully added 10.00 grams of cat_food.", result)

    def test_add_updates_quantity_to_existing_food(self):
        self.p.add_food("cat_food", 10)

        result = self.p.add_food("cat_food", 5)

        self.assertEqual({"cat_food": 15}, self.p.food)
        self.assertEqual(f"Successfully added 5.00 grams of cat_food.", result)

    def test_add_existing_pet_raises(self):
        self.p.add_pet("dog")

        with self.assertRaises(Exception) as ex:
            self.p.add_pet("dog")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_valid_pet(self):
        result = self.p.add_pet("dog")

        self.assertEqual(["dog"], self.p.pets)
        self.assertEqual(f"Successfully added dog.", result)

    def test_feed_pet_invalid_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.p.feed_pet("granules", "dog")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_not_existing_food(self):
        self.p.add_pet("dog")

        result = self.p.feed_pet("granules", "dog")

        self.assertEqual('You do not have granules', result)

    def test_feed_pet_with_lt_100gr_(self):
        self.p.add_pet("dog")
        self.p.add_food("granules", 99)

        result = self.p.feed_pet("granules", "dog")

        self.assertEqual({"granules": 1099.00}, self.p.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_current_food_mt_100(self):
        self.p.add_pet("dog")
        self.p.add_food("granules", 101)

        result = self.p.feed_pet("granules", "dog")

        self.assertEqual({"granules": 1.00}, self.p.food)
        self.assertEqual("dog was successfully fed", result)

    def test__repr__valid_data(self):
        self.p.add_pet("dog")
        self.p.add_pet("cat")

        result = str(self.p)
        expected = "Shop Test:\nPets: dog, cat"

        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
