from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AQUARIUMS_TYPES = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    DECORATION_TYPES = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    FISH_TYPES = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def _find_aquarium_by_name(self, name):
        for f in self.aquariums:
            if f.name == name:
                return f

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in Controller.AQUARIUMS_TYPES:
            return "Invalid aquarium type."

        aquarium = Controller.AQUARIUMS_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(aquarium)

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in Controller.DECORATION_TYPES:
            return "Invalid decoration type."

        decor = Controller.DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(decor)

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decor = self.decorations_repository.find_by_type(decoration_type)
        current_aquarium = self._find_aquarium_by_name(aquarium_name)

        if decor == "None":
            return f"There isn't a decoration of type {decoration_type}."

        current_aquarium.decorations.append(decor)
        self.decorations_repository.remove(decor)

        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in Controller.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."

        fish = Controller.FISH_TYPES[fish_type](fish_name, fish_species, price)
        current_aquarium = self._find_aquarium_by_name(aquarium_name)

        return current_aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self._find_aquarium_by_name(aquarium_name)
        aquarium.feed()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self._find_aquarium_by_name(aquarium_name)
        result = 0
        result += sum([f.price for f in aquarium.fish])
        result += sum([d.price for d in aquarium.decorations])

        return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        result = []
        for a in self.aquariums:
            result.append(str(a))

        return '\n'.join(result)
