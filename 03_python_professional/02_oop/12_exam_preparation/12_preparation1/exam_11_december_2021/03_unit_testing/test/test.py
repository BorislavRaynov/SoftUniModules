from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self):
        self.t = Team("Merc")
        self.t_members = {
            "Alonso": 35, "Ivan": 30
        }

    def test_init_valid_data(self):

        self.assertEqual("Merc", self.t.name)
        self.assertEqual({}, self.t.members)

    def test_set_name_with_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.t.name = "Merc1"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_not_existing_member(self):
        result = self.t.add_member(Gosho=25, Pesho=20)

        self.assertEqual({"Gosho": 25, "Pesho": 20}, self.t.members)
        self.assertEqual("Successfully added: Gosho, Pesho", result)

    def test_add_already_existing_member(self):
        self.t.members = {
            "Alonso": 35, "Ivan": 30
        }

        result = self.t.add_member(Alonso=35)

        self.assertEqual("Successfully added: ", result)

    def test_remove_existing_member(self):
        self.t.members = {
                "Alonso": 35, "Ivan": 30
            }

        result = self.t.remove_member("Alonso")

        self.assertEqual({"Ivan": 30}, self.t.members)
        self.assertEqual("Member Alonso removed", result)

    def test_remove_not_existing_member(self):
        self.t.members = {
                "Alonso": 35, "Ivan": 30
            }

        result = self.t.remove_member("Gosho")

        self.assertEqual({"Alonso": 35, "Ivan": 30}, self.t.members)
        self.assertEqual("Member with name Gosho does not exist", result)

    def test___gt__returns_correct_data(self):
        self.t.members = {
            "Alonso": 35, "Ivan": 30
        }
        second_team = Team("Ferrari")
        second_team.members = {
            "Gosho": 31
        }
        result = self.t > second_team

        self.assertEqual(True, result)

    def test__gt__returns_valid_data(self):
        self.t.members = {
            "Gosho": 31
        }
        second_team = Team("Ferrari")
        second_team.members = {
            "Alonso": 35, "Ivan": 30
        }

        result = self.t > second_team

        self.assertEqual(False, result)

    def test__len__returns_valid_data(self):
        self.t.members = {
            "Alonso": 35, "Ivan": 30
        }

        result = len(self.t)

        self.assertEqual(2, result)

    def test__add__method_return_correct_data(self):
        self.t.members = {"Gosho": 31}
        second_team = Team("Ferrari")
        second_team.members = {"Pesho": 20}

        third_team = self.t.__add__(second_team)

        self.assertEqual("MercFerrari", third_team.name)
        self.assertEqual({"Gosho": 31, "Pesho": 20}, third_team.members)

    def test__str__method_returns_valid_data(self):
        self.t.members = {
           "Ivan": 30,  "Alonso": 35
        }

        result = str(self.t)
        expected = "Team name: Merc\nMember: Alonso - 35-years old\nMember: Ivan - 30-years old"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
