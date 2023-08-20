from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.t = Train("Test", 3)

    def test_init_data(self):
        self.assertEqual("Test", self.t.name)
        self.assertEqual(3, self.t.capacity)
        self.assertEqual([], self.t.passengers)

        self.assertEqual("Train is full", self.t.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.t.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.t.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.t.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.t.PASSENGER_REMOVED)
        self.assertEqual(0, self.t.ZERO_CAPACITY)

    def test_add_passenger_with_no_room_raises(self):
        self.t.passengers = ["Ivo", "Ivan", "Gosho"]
        with self.assertRaises(ValueError) as ve:
            self.t.add("Peter")

        self.assertEqual("Train is full", str(ve.exception))

    def test_add_existing_passenger(self):
        self.t.passengers = ["Ivo", "Ivan"]
        with self.assertRaises(ValueError) as ve:
            self.t.add("Ivan")

        self.assertEqual("Passenger Ivan Exists", str(ve.exception))

    def test_add_passenger_valid_data(self):
        self.t.passengers = ["Ivo", "Ivan"]

        result = self.t.add("Gosho")
        expected = "Added passenger Gosho"

        self.assertEqual(["Ivo", "Ivan", "Gosho"], self.t.passengers)
        self.assertEqual(expected, result)

    def test_remove_not_existing_passenger_raises(self):
        self.t.passengers = ["Ivo", "Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.t.remove("Gosho")

        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_valid_data(self):
        self.t.passengers = ["Ivo", "Ivan"]

        result = self.t.remove("Ivan")
        expected = "Removed Ivan"

        self.assertEqual(["Ivo"], self.t.passengers)
        self.assertEqual(expected, result)

