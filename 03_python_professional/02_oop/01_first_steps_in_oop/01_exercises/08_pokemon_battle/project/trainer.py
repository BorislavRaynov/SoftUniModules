from project.pokemon import Pokemon


class Trainer:
    pokemons = []

    def __init__(self, name):
        self.name = name

    def add_pokemon(self, pokemon: Pokemon):
        for p in self.pokemons:
            if pokemon == p:
                return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}" + '\n'
        result += f"Pokemon count {len(self.pokemons)}" + '\n'
        for p in self.pokemons:
            result += f"- {p.pokemon_details()}"
        return result
