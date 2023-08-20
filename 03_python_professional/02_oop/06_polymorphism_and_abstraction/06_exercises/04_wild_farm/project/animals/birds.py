from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_food(self):
        return [Meat]

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_food(self):
        return [Vegetable, Meat, Seed, Fruit]

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
