from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.m = Movie("Testname", 2000, 10.0)

    def test_init_data(self):

        self.assertEqual("Testname", self.m.name)
        self.assertEqual(2000, self.m.year)
        self.assertEqual(10.0, self.m.rating)
        self.assertEqual([], self.m.actors)

    def test_set_empty_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.m.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_set_year_before_given_limit_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.m.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_not_existing_actor_add_it_correct(self):
        self.m.add_actor("Johny")

        self.assertEqual(["Johny"], self.m.actors)

    def test_existing_actor_do_not_add_it(self):
        self.m.add_actor("Johny")

        result = self.m.add_actor("Johny")

        self.assertEqual(["Johny"], self.m.actors)
        self.assertEqual("Johny is already added in the list of actors!", result)

    def test__gt__method_correct(self):
        m_2 = Movie("Test_2", 1999, 8.5)

        result = self.m > m_2

        self.assertEqual('"Testname" is better than "Test_2"', result)

    def test__gt__method_second_movie_is_better_correct(self):
        m_2 = Movie("Test_2", 1999, 10.5)

        result = self.m > m_2

        self.assertEqual('"Test_2" is better than "Testname"', result)

    def test__repr__method_Correct(self):
        self.m.add_actor("Johny")
        self.m.add_actor("Blaze")

        result = str(self.m)
        expected = "Name: Testname\nYear of Release: 2000\nRating: 10.00\nCast: Johny, Blaze"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()