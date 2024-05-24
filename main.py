import requests
import random

# Funzione per ottenere i dettagli di un Pokémon casuale
def get_random_pokemon():
    pokemon_id = random.randint(1, 898)  # Ci sono 898 Pokémon fino alla Generazione 8
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Funzione per ottenere un elenco di tutti i Pokémon
def get_pokemon_list():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=898")
    if response.status_code == 200:
        data = response.json()
        return [pokemon['name'] for pokemon in data['results']]
    else:
        return []

# Funzione per generare le opzioni di risposta
def generate_options(correct_pokemon, pokemon_list):
    options = [correct_pokemon]
    while len(options) < 3:
        option = random.choice(pokemon_list)
        if option not in options:
            options.append(option)
    # Mischia le opzioni dei nomi dei pokemon in modo casuale
    random.shuffle(options)
    # Restituisci le opzioni mescolate con anche il nome corretto del Pokémon
    return options

# Funzione per giocare al gioco
def play_game():
    score = 0
    pokemon_list = get_pokemon_list()
    
    #Il gioco viene ripetuto 10 volte
    for _ in range(10):
        pokemon = get_random_pokemon()
        if pokemon:
            correct_pokemon = pokemon['name']
            options = generate_options(correct_pokemon, pokemon_list)
            
            print("Indovina il Pokémon:")
            for i, option in enumerate(options):
                print(f"{i + 1}. {option}")
            
            user_choice = input("Inserisci il numero della tua scelta: ")
            
            # Verifica se l'input dell'utente è un numero e se è un'opzione valida tra 1 e 3
            if user_choice.isdigit() and int(user_choice) in range(1, 4):
                if options[int(user_choice) - 1] == correct_pokemon:
                    print("Corretto!")
                    score += 1
                else:
                    print(f"Sbagliato! La risposta corretta era {correct_pokemon}.")
            else:
                print("Scelta non valida.")
    
    print(f"Il gioco è finito! Il tuo punteggio è: {score}/10")

if __name__ == "__main__":
    play_game()