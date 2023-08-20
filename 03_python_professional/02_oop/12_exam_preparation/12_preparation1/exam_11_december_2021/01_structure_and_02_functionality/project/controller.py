
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CAR_TYPES:
            if model in [car.model for car in self.cars]:
                raise Exception(f"Car {model} is already created!")
            self.cars.append(self.VALID_CAR_TYPES[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = list(filter(lambda c: c.__class__.__name__ == car_type and not c.is_taken, self.cars))[-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            driver.car.is_taken = False
            old_car_model = driver.car.model
            car.is_taken = True
            driver.car = car
            return f"Driver {driver.name} changed his car from {old_car_model} to {car.model}."

        car.is_taken = True
        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        all_drivers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)
        final_result = []
        for i in range(3):
            current_driver = all_drivers[i]
            current_driver.number_of_wins += 1
            current_driver_result = f"Driver {current_driver.name} wins the {race_name} race" \
                                    f" with a speed of {current_driver.car.speed_limit}."
            final_result.append(current_driver_result)

        return '\n'.join(final_result)
