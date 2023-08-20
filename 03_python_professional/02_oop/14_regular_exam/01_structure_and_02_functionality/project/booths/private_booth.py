from project.booths.booth import Booth


class PrivateBooth(Booth):
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        result = number_of_people * 3.50
        self.price_for_reservation = result
        self.is_reserved = True

    def calculate_bill(self):
        result = self.price_for_reservation
        result += sum([d.price for d in self.delicacy_orders])

        return result

    def free_and_empty_booth(self):
        self.delicacy_orders = []
        self.is_reserved = False
        self.price_for_reservation = 0
