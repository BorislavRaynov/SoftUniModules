class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.cost = sum(t for t in toys_cost) + self.food_cost

    def get_monthly_expense(self):
        return 30 * self.cost
