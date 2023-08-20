from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plant_factory = Plantation(100)

    def test_correct_init_data(self):

        self.assertEqual(100, self.plant_factory.size)
        self.assertEqual({}, self.plant_factory.plants)
        self.assertEqual([], self.plant_factory.workers)

    def test_set_negative_size_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plant_factory.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_already_hired_raises(self):
        self.plant_factory.hire_worker("Ivan")

        with self.assertRaises(ValueError) as ve:
            self.plant_factory.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_add_successful(self):
        result = self.plant_factory.hire_worker("Ivan")

        self.assertEqual(["Ivan"], self.plant_factory.workers)
        self.assertEqual("Ivan successfully hired.", result)

    def test__len__method_calculate_correctly(self):
        self.plant_factory.plants = {
            "Ivan": ["plant_1"],
            "Pesho": ["plant_2"],
            "Gosho": ["plant_3", "plant_4"]
        }

        self.assertEqual(4, len(self.plant_factory))

    def test_planting_with_not_existing_worker_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.plant_factory.planting("Ivan", "flower_1")

        self.assertEqual("Worker with name Ivan is not hired!", str(ve.exception))

    def test_planting_with_no_room_in_plantation_raises(self):
        self.plant_factory.size = 1
        self.plant_factory.plants = {"Ivan": "flower_1"}
        self.plant_factory.hire_worker("Gosho")

        with self.assertRaises(ValueError) as ve:
            self.plant_factory.planting("Gosho", "plant_2")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_worker_already_planted_plant(self):
        self.plant_factory.hire_worker("Ivan")
        self.plant_factory.plants = {"Ivan": ["flower_1"]}

        result = self.plant_factory.planting("Ivan", "flower_2")

        self.assertEqual(["flower_1", "flower_2"], self.plant_factory.plants["Ivan"])
        self.assertEqual("Ivan planted flower_2.", result)

    def test_worker_plant_for_first_time(self):
        self.plant_factory.hire_worker("Gosho")

        result = self.plant_factory.planting("Gosho", "tree_1")

        self.assertEqual(["tree_1"], self.plant_factory.plants["Gosho"])
        self.assertEqual("Gosho planted it's first tree_1.", result)

    def test__str__method_correct(self):
        self.plant_factory.hire_worker("Ivan")
        self.plant_factory.hire_worker("Gosho")
        self.plant_factory.planting("Ivan", "tree_1")
        self.plant_factory.planting("Gosho", "flower_2")

        result = str(self.plant_factory)
        expected = "Plantation size: 100\nIvan, Gosho\nIvan planted: tree_1\nGosho planted: flower_2"

        self.assertEqual(expected, result)

    def test__repr__method_correct(self):
        self.plant_factory.hire_worker("Ivan")
        self.plant_factory.hire_worker("Gosho")

        result = repr(self.plant_factory)
        expected = "Size: 100\nWorkers: Ivan, Gosho"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
