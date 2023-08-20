from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self):
        self.l = Library("Test")

    def test_init_with_valid_data(self):
        self.assertEqual("Test", self.l.name)
        self.assertEqual({}, self.l.books_by_authors)
        self.assertEqual({}, self.l.readers)

    def test_set_name_incorrect_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.l.name = ''

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_author_and_book_with_correct_data(self):
        self.l.add_book("author", "book")

        self.assertEqual({"author": ["book"]}, self.l.books_by_authors)

    def test_add_book_to_existing_author_correct(self):
        self.l.books_by_authors = {"author": ["book"]}

        self.l.add_book("author", "book1")

        self.assertEqual({"author": ["book", "book1"]}, self.l.books_by_authors)

    def test_add_reader_correct(self):
        self.l.add_reader("Ivan")

        self.assertEqual({"Ivan": []}, self.l.readers)

    def test_add_existing_reader_return(self):
        self.l.readers = {"Ivan": []}

        result = self.l.add_reader("Ivan")
        expected = f"Ivan is already registered in the Test library."

        self.assertEqual(result, expected)

    def test_rent_with_not_existing_reader_returns(self):
        result = self.l.rent_book("Gosho", "author", "book")

        expected = f"Gosho is not registered in the Test Library."

        self.assertEqual(expected, result)

    def test_rent_with_not_existing_author_return(self):
        self.l.books_by_authors = {"author": ["book"]}
        self.l.readers = {"Ivan": []}

        result = self.l.rent_book("Ivan", "author1", "book1")
        expected = "Test Library does not have any author1's books."

        self.assertEqual(expected, result)

    def test_rent_with_not_existing_book_return(self):
        self.l.books_by_authors = {"author": ["book"]}
        self.l.readers = {"Ivan": []}

        result = self.l.rent_book("Ivan", "author", "book1")
        expected = """Test Library does not have author's "book1"."""

        self.assertEqual(expected, result)

    def test_rent_book_correctly(self):
        self.l.books_by_authors = {"author": ["book"]}
        self.l.readers = {"Ivan": []}

        self.l.rent_book("Ivan", "author", "book")

        self.assertEqual({"Ivan": [{"author": "book"}]}, self.l.readers)
        self.assertEqual({"author": []}, self.l.books_by_authors)


if __name__ == "__main__":
    main()
