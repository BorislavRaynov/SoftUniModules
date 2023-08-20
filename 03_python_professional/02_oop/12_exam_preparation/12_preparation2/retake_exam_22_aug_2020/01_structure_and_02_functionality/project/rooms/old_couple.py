from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float, members_count=2):
        super().__init__(family_name, pension_one + pension_two, members_count)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.total_expenses = self.appliances + self.children
        self.expenses = self.calculate_expenses(*self.total_expenses)

    @staticmethod
    def calculate_expenses(*args):
        result = 0
        for el in args:
            result += el.get_monthly_expense()

        return result

    def __str__(self):
        result = [f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, "
                  f"Expenses: {self.expenses:.2f}$"]

        appliances_monthly = sum(a.get_monthly_expense() for a in self.appliances)

        result.append(f"--- Appliances monthly cost: {appliances_monthly:.2f}$")

        return '\n'.join(result)
