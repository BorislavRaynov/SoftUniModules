from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    VALID_AQUARIUMS = ["SaltwaterAquarium"]

    def __init__(self, name: str, species: str, price: float, size: int = 5):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 2
