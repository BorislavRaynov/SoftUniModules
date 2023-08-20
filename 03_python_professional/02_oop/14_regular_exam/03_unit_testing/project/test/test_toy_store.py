from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_correct_init_data(self):
        self.assertEqual({"A": None, "B": None, "C": None, "D": None,
            "E": None, "F": None, "G": None}, self.store.toy_shelf)

    def test_add_toy_not_existing_shelf_raises(self):
        self.store.toy_shelf = {"A": None, "B": None}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("C", "test")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_existing_shelf_and_existing_toy_raises(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "test")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_full_shelf_raises(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "test_1")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_adds_it_correctly(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        result = self.store.add_toy("A", "test_1")

        self.assertEqual({"A": "test_1", "B": "test"}, self.store.toy_shelf)
        self.assertEqual(f"Toy:test_1 placed successfully!", result)

    def test_remove_toy_from_not_existing_shelf_raises(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("C", "test_2")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_not_existing_toy_from_existing_shelf_raises(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "test_2")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_valid_remove_toy_from_shelf_set_it_empty(self):
        self.store.toy_shelf = {"A": None, "B": "test"}

        result = self.store.remove_toy("B", "test")

        self.assertEqual({"A": None, "B": None}, self.store.toy_shelf)
        self.assertEqual("Remove toy:test successfully!", result)


if __name__ == "__main__":
    main()
