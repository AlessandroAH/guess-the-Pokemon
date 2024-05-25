import requests
import random

class PokemonQuiz:
    # Funzione per ottenere i dettagli di un Pokémon casuale
    def get_random_pokemon(self):
        pokemon_id = random.randint(1, 898)  # Ci sono 898 Pokémon fino alla Generazione 8
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=20)
        if response.status_code == 200:
            pokemon = response.json()
            return pokemon['name']
        else:
            return None

    # Funzione per ottenere un elenco di tutti i Pokémon
    def get_pokemon_list(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon", timeout=20)  #response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=898", timeout=20)
        if response.status_code == 200:
            data = response.json()
            return [pokemon['name'] for pokemon in data['results']]
        else:
            return []

    # Funzione per generare le opzioni di risposta
    def generate_options(self,correct_pokemon, pokemon_list):
        options = [correct_pokemon]
        while len(options) < 3:
            option = random.choice(pokemon_list)
            if option not in options:
                options.append(option)
        # Mischia le opzioni dei nomi dei pokemon in modo casuale
        random.shuffle(options)
        # Restituisci le opzioni mescolate con anche il nome corretto del Pokémon
        return options