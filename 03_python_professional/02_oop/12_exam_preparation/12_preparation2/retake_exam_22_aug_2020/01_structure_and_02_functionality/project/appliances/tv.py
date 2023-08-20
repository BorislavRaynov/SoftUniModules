from project.appliances.appliance import Appliance


class TV(Appliance):
    COST = 1.5

    def __init__(self):
        super().__init__(self.COST)

    def get_monthly_expense(self):
        return 30 * self.cost
