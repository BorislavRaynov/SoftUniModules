from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.expenses + room.room_cost
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        result = []
        for r in self.rooms:
            bill = r.expenses + r.room_cost
            if r.budget >= bill:
                r.budget -= bill
                result.append(f"{r.family_name} paid {bill:.2f}$ and have {r.budget:.2f}$ left.")
            else:
                result.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(r)

        return '\n'.join(result)

    def status(self):
        population = sum([r.members_count for r in self.rooms])
        result = [f"Total population: {population}"]
        for r in self.rooms:
            result.append(str(r))

        return '\n'.join(result)
