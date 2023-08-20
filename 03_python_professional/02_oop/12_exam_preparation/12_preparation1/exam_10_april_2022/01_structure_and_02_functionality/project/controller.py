class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def _get_suppl_by_type(self, type):
        for idx in range(len(self.supplies)-1, -1, -1):
            if self.supplies[idx].__class__.__name__ == type:
                result = self.supplies[idx]
                self.supplies.pop(idx)
                return result

    def add_player(self, *args):
        to_bo_added = []

        for el in args:
            if el not in self.players:
                self.players.append(el)
                to_bo_added.append(el.name)

        return f"Successfully added: {', '.join(to_bo_added)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_player(player_name)
        if not player or sustenance_type not in ["Food", "Drink"]:
            return
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        supply = self._get_suppl_by_type(sustenance_type)

        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        increased_stamina = player.stamina + supply.energy
        player.stamina = increased_stamina if increased_stamina <= 100 else 100
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.find_player(first_player_name)
        player2 = self.find_player(second_player_name)

        players_low_battery = []
        for player in [player1, player2]:
            if player.stamina == 0:
                players_low_battery.append(f"Player {player.name} does not have enough stamina.")
        if players_low_battery:
            return '\n'.join(players_low_battery)

        player_on_turn = sorted([player1, player2], key=lambda x: x.stamina)
        winner = None

        for _ in range(2):
            player_attacks, player_attacked = player_on_turn
            reduced_stamina = player_attacked.stamina - player_attacks.stamina / 2

            if reduced_stamina <= 0:
                player_attacked.stamina = 0
                winner = player_attacks
                break

            player_attacked.stamina = reduced_stamina
            player_on_turn = player_on_turn[::-1]

        if not winner:
            winner = sorted([player1, player2], key=lambda x: x.stamina)[-1]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= (player.age * 2)
            if player.stamina <= 0:
                player.stamina = 0

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)
