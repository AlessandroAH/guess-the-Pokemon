import requests
import random

# Definizione della classe PokemonQuiz
class PokemonQuiz:
    def __init__(self):
        self.session = requests.Session()  # Crea una sessione HTTP per le richieste

    # Funzione per ottenere un Pokémon casuale
    def get_random_pokemon(self):
        pokemon_id = random.randint(1, 898)  # Genera un ID casuale tra 1 e 898 (numero totale di Pokémon)
        try:
            response = self.session.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=20)  # Effettua una richiesta HTTP per ottenere i dati del Pokémon
            response.raise_for_status()  # Verifica che la richiesta sia andata a buon fine
            pokemon = response.json()  # Converte la risposta JSON in un dizionario
            return {
                'name': pokemon['name'],  # Nome del Pokémon
                'image_url': pokemon['sprites']['front_default']  # URL dell'immagine frontale del Pokémon
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching random Pokémon: {e}")  # Stampa un messaggio di errore in caso di fallimento
            return None

    # Funzione per ottenere la lista di tutti i Pokémon
    def get_pokemon_list(self):
        try:
            response = self.session.get("https://pokeapi.co/api/v2/pokemon?limit=898", timeout=20)  # Effettua una richiesta HTTP per ottenere la lista dei Pokémon
            response.raise_for_status()  # Verifica che la richiesta sia andata a buon fine
            data = response.json()  # Converte la risposta JSON in un dizionario
            return [pokemon['name'] for pokemon in data['results']]  # Ritorna una lista con i nomi di tutti i Pokémon
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Pokémon list: {e}")  # Stampa un messaggio di errore in caso di fallimento
            return []

    # Funzione per generare le opzioni di risposta
    def generate_options(self, correct_pokemon, pokemon_list):
        options = [correct_pokemon['name']]  # Inizia la lista delle opzioni con il nome del Pokémon corretto
        while len(options) < 3:  # Continua finché non ci sono almeno 3 opzioni
            option = random.choice(pokemon_list)  # Seleziona un nome casuale dalla lista di Pokémon
            if option not in options:  # Verifica che il nome non sia già presente nelle opzioni
                options.append(option)  # Aggiunge il nome alle opzioni
        random.shuffle(options)  # Mescola le opzioni in modo casuale
        return options  # Ritorna le opzioni mescolate

# Per ignorare momentaneamente la verifica dei certificati SSL
# verify=False