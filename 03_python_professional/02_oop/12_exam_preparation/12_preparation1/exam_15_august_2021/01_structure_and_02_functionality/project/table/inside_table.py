from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if 1 <= value <= 50:
            self.__table_number = value
        else:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        result = 0
        for product in self.food_orders:
            result += product.price

        for product in self.drink_orders:
            result += product.price

        return result

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
