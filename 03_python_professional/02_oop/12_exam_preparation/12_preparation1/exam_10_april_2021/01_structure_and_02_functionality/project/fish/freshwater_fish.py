from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    VALID_AQUARIUMS = ["FreshwaterAquarium"]

    def __init__(self, name: str, species: str, price: float, size: int = 3):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 3
