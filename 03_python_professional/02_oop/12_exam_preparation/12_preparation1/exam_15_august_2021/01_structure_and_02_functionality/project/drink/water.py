from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str, price: float = 1.50):
        super().__init__(name, portion, price, brand)

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
