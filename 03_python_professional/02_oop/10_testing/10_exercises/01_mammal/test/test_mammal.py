from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def test_name_is_initialized(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        self.assertEqual("Test", m.name)

    def test_type_is_initialized(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        self.assertEqual("Test_type", m.type)

    def test_sound_is_initialized(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        self.assertEqual("Test_sound", m.sound)

    def test_kingdom_is_set_on_initializing(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        self.assertEqual("animals", m._Mammal__kingdom)

    def test_make_sound_returns_correct_data(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        result = m.make_sound()
        expected = f"{m.name} makes {m.sound}"

        self.assertEqual(expected, result)

    def test_get_kingdom_returns_correct_data(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        result = m.get_kingdom()
        expected = m._Mammal__kingdom

        self.assertEqual(expected, result)

    def test_get_info_returns_correct_data(self):
        m = Mammal("Test", "Test_type", "Test_sound")

        result = m.info()
        expected = f"{m.name} is of type {m.type}"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
