class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTest(TestCase):
    def test_make_in_init_data_with_none_data_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car(None, 'E500', 11, 12)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_in_init_data_with_empty_data_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car('', 'E500', 11, 12)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_init_data_sets_correctly(self):
        car = Car('Merc', 'E500', 11, 12)

        self.assertEqual('Merc', car.make)

    def test_model_in_init_data_with_none_data_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Merc', None, 11, 12)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_in_init_data_with_empty_data_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Merc', '', 11, 12)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_init_data_sets_correctly(self):
        car = Car('Merc', 'E500', 11, 12)

        self.assertEqual('E500', car.model)

    def test_set_zero_fuel_consumption_in_init_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Merc', 'E500', 0, 12)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_negative_fuel_consumption_in_init_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Merc', 'E500', -1, 12)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_correct_fuel_consumption_in_init(self):
        car = Car('Merc', 'E500', 11, 12)

        self.assertEqual(11, car.fuel_consumption)

    def test_set_zero_fuel_capacity_in_init_raises(self):

        with self.assertRaises(Exception) as ex:
            car = Car('Merc', 'E500', 11, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_negative_fuel_capacity_in_init_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car('Merc', 'E500', 11, -1)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_correct_fuel_capacity_in_init(self):
        car = Car('Merc', 'E500', 11, 12)

        self.assertEqual(12, car.fuel_capacity)

    def test_initial_fuel_amount_is_set_to_zero(self):
        car = Car('Merc', 'E500', 11, 12)

        self.assertEqual(0, car.fuel_amount)

    def test_fuel_amount_goes_to_negative_after_drive_raises(self):
        car = Car('Merc', 'E500', 10, 100)
        car.refuel(10)

        with self.assertRaises(Exception) as ex:
            car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_fuel_amount_goes_to_zero_after_drive_wtih_exact_fuel(self):
        car = Car('Merc', 'E500', 10, 100)

        car.refuel(10)
        car.drive(100)

        self.assertEqual(0, car.fuel_amount)

    def test_refuel_with_zero_raises(self):
        car = Car('Merc', 'E500', 11, 12)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_raises(self):
        car = Car('Merc', 'E500', 11, 12)

        with self.assertRaises(Exception) as ex:
            car.refuel(-50)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuelling_adds_fuel(self):
        car = Car('Merc', 'E500', 11, 100)

        car.refuel(90)

        self.assertEqual(90, car.fuel_amount)

    def test_over_refilling_sets_amount_to_max(self):
        car = Car('Merc', 'E500', 10, 100)

        car.refuel(150)

        self.assertEqual(100, car.fuel_amount)

    def test_drive_with_not_enough_fuel_raises(self):
        car = Car('Merc', 'E500', 10, 100)

        car.refuel(20)

        with self.assertRaises(Exception) as ex:
            car.drive(300)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_fuel_is_used_after_driving(self):
        car = Car('Merc', 'E500', 10, 100)
        car.refuel(50)

        car.drive(200)

        self.assertEqual(30, car.fuel_amount)


if __name__ == '__main__':
    main()
