from project.appliances.appliance import Appliance


class Stove(Appliance):
    COST = 0.7

    def __init__(self):
        super().__init__(self.COST)

    def get_monthly_expense(self):
        return 30 * self.cost
