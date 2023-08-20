from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def test_initialising_data(self):
        car = Vehicle(10.0, 200.0)

        self.assertEqual(10.0, car.fuel)
        self.assertEqual(10.0, car.capacity)
        self.assertEqual(200.0, car.horse_power)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_not_enough_fuel_raises(self):
        car = Vehicle(10.0, 200.0)

        with self.assertRaises(Exception) as ex:
            car.drive(15)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_decreasing_after_drive_with_enough_fuel(self):
        car = Vehicle(10.0, 200.0)

        car.drive(4)

        self.assertEqual(5, car.fuel)

    def test_refueling_wit_too_much_fuel_raises(self):
        car = Vehicle(10.0, 200.0)

        with self.assertRaises(Exception) as ex:
            car.refuel(5)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_after_drive_adds_fuel(self):
        car = Vehicle(10.0, 200.0)

        car.drive(4)
        car.refuel(3)

        self.assertEqual(8, car.fuel)

    def test_string_method_after_drive_and_refuel(self):
        car = Vehicle(10.0, 200.0)

        car.drive(4)
        car.refuel(2)

        expected = f"The vehicle has 200.0 horse power with 7.0 fuel left and 1.25 fuel consumption"
        result = str(car)

        self.assertEqual(expected, result)
