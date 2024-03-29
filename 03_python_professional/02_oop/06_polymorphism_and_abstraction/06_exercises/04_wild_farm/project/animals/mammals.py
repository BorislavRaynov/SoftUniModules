from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Meat]

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Meat]

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1 * food.quantity
        self.food_eaten += food.quantity
