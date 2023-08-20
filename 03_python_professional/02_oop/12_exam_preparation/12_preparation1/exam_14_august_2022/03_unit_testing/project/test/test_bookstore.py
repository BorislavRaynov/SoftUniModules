from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):

    def test_data_initialising(self):
        store = Bookstore(15)

        self.assertEqual(15, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store.total_sold_books)

    def test_set_books_limit_to_zero_raises(self):
        store = Bookstore(15)

        with self.assertRaises(ValueError) as ve:
            store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_set_books_limit_to_negative_raises(self):
        store = Bookstore(15)

        with self.assertRaises(ValueError) as ve:
            store.books_limit = -5

        self.assertEqual("Books limit of -5 is not valid", str(ve.exception))

    def test__len__method_returns_correct_result(self):
        store = Bookstore(15)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6, "Test_book_2": 4
        }

        self.assertEqual(10, len(store))

    def test_receive_book_with_no_room_raises(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6, "Test_book_2": 4
        }

        with self.assertRaises(Exception) as ex:
            store.receive_book("Python", 1)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_new_book_correct(self):
        store = Bookstore(10)

        result = store.receive_book("Test_book_2", 3)
        expected = "3 copies of Test_book_2 are available in the bookstore."

        self.assertEqual(expected, result)
        self.assertEqual({"Test_book_2": 3}, store.availability_in_store_by_book_titles)

    def test_receive_book_in_store_updates_copies(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6, "Test_book_2": 3
        }

        result = store.receive_book("Test_book_1", 1)
        expected = "7 copies of Test_book_1 are available in the bookstore."

        self.assertEqual(expected, result)

    def test_sell_book_which_is_not_in_stock_raises(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6
        }

        with self.assertRaises(Exception) as ex:
            store.sell_book("Test_book_2",  4)

        self.assertEqual("Book Test_book_2 doesn't exist!", str(ex.exception))

    def test_sell_book_with_not_enough_quantities_raises(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6, "Test_book_2": 3
        }

        with self.assertRaises(Exception) as ex:
            store.sell_book("Test_book_1", 7)

        self.assertEqual("Test_book_1 has not enough copies to sell. Left: 6", str(ex.exception))

    def test_sell_book_with_correct_data(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6, "Test_book_2": 3
        }

        result = store.sell_book("Test_book_1", 6)

        self.assertEqual("Sold 6 copies of Test_book_1", result)
        self.assertEqual(6, store.total_sold_books)
        self.assertEqual({"Test_book_1": 0, "Test_book_2": 3}, store.availability_in_store_by_book_titles)

    def test_string_method_returns_correct_data(self):
        store = Bookstore(10)
        store.availability_in_store_by_book_titles = {
            "Test_book_1": 6
        }
        store.sell_book("Test_book_1", 3)

        result = str(store)
        expected = "Total sold books: 3\nCurrent availability: 3\n - Test_book_1: 3 copies"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
