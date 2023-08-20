from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    DRINKS_TYPE = {"Water": Water, "Tea": Tea}
    FOODS_TYPE = {"Bread": Bread, "Cake": Cake}
    TABLES_TYPE = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(Bakery.FOODS_TYPE[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(Bakery.DRINKS_TYPE[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(Bakery.TABLES_TYPE[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        try:
            table = next(filter(lambda x: not x.is_reserved and x.capacity >= number_of_people, self.tables_repository))
        except StopIteration:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def find_food_by_name(self, food_name):
        for f in self.food_menu:
            if f.name == food_name:
                return f

    def find_drink_by_name(self, drink_name):
        for d in self.drinks_menu:
            if d.name == drink_name:
                return d

    def order_food(self, table_number: int, *food_names):
        try:
            table = next(filter(lambda x: x.table_number == table_number, self.tables_repository))
        except StopIteration:
            return f"Could not find table {table_number}"

        ordered = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.name} does not have in the menu:"]

        for food_name in food_names:
            food = self.find_food_by_name(food_name)
            if food:
                table.order_food(food)
                ordered.append(str(food))
            else:
                not_in_menu.append(food_name)

        result = ordered + not_in_menu

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drink_names):
        try:
            table = next(filter(lambda x: x.table_number == table_number, self.tables_repository))
        except StopIteration:
            return f"Could not find table {table_number}"

        ordered = [f"Table {table_number} ordered:"]
        not_in_menu = [f"{self.name} does not have in the menu:"]

        for drink_name in drink_names:
            drink = self.find_drink_by_name(drink_name)
            if drink:
                table.order_drink(drink)
                ordered.append(str(drink))
            else:
                not_in_menu.append(drink_name)

        result = ordered + not_in_menu

        return '\n'.join(result)

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        current_bill = table.get_bill()
        self.total_income += current_bill
        table.clear()
        return f"Table: {table_number}\nBill: {current_bill:.2f}"

    def get_free_tables_info(self):

        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())

        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
