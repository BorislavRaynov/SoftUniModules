from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str, capacity: int = 25):
        super().__init__(name, capacity)

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) < self.capacity:
            if self.__class__.__name__ in fish.VALID_AQUARIUMS:
                self.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {self.name}."
            return f"Water not suitable."
        return "Not enough capacity."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        result = [f"{self.name}:"]

        if self.fish:
            result.append(f"Fish: {' '.join([f.name for f in self.fish])}")
        else:
            result.append("Fish: none")

        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(result)
