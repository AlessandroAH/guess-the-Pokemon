import requests
import random

class PokemonQuiz:
    def __init__(self):
        self.session = requests.Session()

    def get_random_pokemon(self):
        pokemon_id = random.randint(1, 898)
        try:
            response = self.session.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=20)
            response.raise_for_status()
            pokemon = response.json()
            return {
                'name': pokemon['name'],
                'image_url': pokemon['sprites']['front_default']
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching random Pokémon: {e}")
            return None

    def get_pokemon_list(self):
        try:
            response = self.session.get("https://pokeapi.co/api/v2/pokemon?limit=898", timeout=20)
            response.raise_for_status()
            data = response.json()
            return [pokemon['name'] for pokemon in data['results']]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Pokémon list: {e}")
            return []

    def generate_options(self, correct_pokemon, pokemon_list):
        options = [correct_pokemon['name']]
        while len(options) < 3:
            option = random.choice(pokemon_list)
            if option not in options:
                options.append(option)
        random.shuffle(options)
        return options

#Per ignorare momentaneamente la verifica dei certificati SSL
#verify=False