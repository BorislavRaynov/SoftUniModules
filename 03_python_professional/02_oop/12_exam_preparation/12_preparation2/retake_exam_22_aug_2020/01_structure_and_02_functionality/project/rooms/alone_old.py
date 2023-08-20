from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float, members_count: int = 1):
        super().__init__(family_name, pension, members_count)
        self.room_cost = 10

    def __str__(self):
        result = [f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, "
                  f"Expenses: {self.expenses:.2f}$"]

        return result
