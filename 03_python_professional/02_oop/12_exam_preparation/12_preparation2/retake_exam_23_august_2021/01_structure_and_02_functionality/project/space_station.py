from collections import deque

from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    VALID_ASTRONAUTS = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions_completed = 0
        self.missions_not_completed = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in SpaceStation.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.add(SpaceStation.VALID_ASTRONAUTS[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        valid_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]

        if not valid_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        valid_astronauts = deque(sorted(valid_astronauts, key=lambda x: -x.oxygen)[:5])
        went_out = 0

        while True:
            if not planet.items:
                self.missions_completed += 1
                return f"Planet: {planet_name} was explored. {went_out} astronauts participated in collecting items."

            if not valid_astronauts:
                self.missions_not_completed += 1
                return "Mission is not completed."

            current_astronaut = valid_astronauts[0]
            went_out += 1

            while planet.items:
                current_astronaut.backpack.append(planet.items.pop())
                current_astronaut.breathe()
                if current_astronaut.oxygen <= 0:
                    valid_astronauts.popleft()
                    break

    def report(self):
        output = [f"{self.missions_completed} successful missions!",
                  f"{self.missions_not_completed} missions were not completed!", "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(f'Name: {astronaut.name}')
            output.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                output.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                output.append(f"Backpack items: none")

        return '\n'.join(output)
