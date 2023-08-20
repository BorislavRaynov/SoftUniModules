from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for hero in self.players:
            if hero.name == player_name:
                hero.guild = 'Unaffiliated'
                self.players.remove(hero)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}" + '\n'
        for hero in self.players:
            result += f"{Player.player_info(hero)}"
        return result + '\n'
