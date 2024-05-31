from pokemon import PokemonQuiz

# Definizione della classe Quiz
class Quiz:
    def __init__(self):
        self.pokemon_quiz = PokemonQuiz()  # Istanza del quiz Pokémon
        self.current_question = 0  # Numero della domanda corrente
        self.AllPokemon = self.pokemon_quiz.get_pokemon_list()  # Lista di tutti i Pokémon
        self.correct_answer = None  # Risposta corretta della domanda corrente
        self.score = 0  # Punteggio totale
        self.turns = 0  # Numero di turni
        self.question = "Qual è questo Pokémon?"  # Testo della domanda

    # Funzione per ottenere la prossima domanda
    def get_next_question(self):
        if self.current_question <= 10:  # Verifica se ci sono ancora domande da fare
            pokemon = self.pokemon_quiz.get_random_pokemon()  # Ottiene un Pokémon casuale
            if pokemon:
                self.correct_answer = pokemon  # Imposta la risposta corretta
                options = self.pokemon_quiz.generate_options(self.correct_answer, self.AllPokemon)  # Genera le opzioni di risposta
                self.current_question += 1  # Incrementa il numero della domanda corrente
                return self.question, options, pokemon['image_url']  # Ritorna la domanda, le opzioni e l'URL dell'immagine del Pokémon
        else:
            return None  # Nessuna domanda rimasta
    
    # Funzione per inviare una risposta
    def submit_answer(self, answer):
        if answer == self.correct_answer['name']:  # Verifica se la risposta è corretta
            self.score += 1  # Incrementa il punteggio se la risposta è corretta
            correct = True  # Imposta il flag di risposta corretta
        else:
            correct = False  # Imposta il flag di risposta errata
        self.turns += 1  # Incrementa il numero di turni
        question, options, image_url = self.get_next_question()  # Ottiene la prossima domanda
        return correct, question, options, image_url  # Ritorna se la risposta era corretta, la prossima domanda, le opzioni e l'URL dell'immagine
    
    # Metodo per resettare il quiz
    def reset(self):
        self.current_question = 0  # Resetta il numero della domanda corrente
        self.score = 0  # Resetta il punteggio
        self.correct_answer = None  # Resetta la risposta corretta
        self.turns = 0  # Resetta il numero di turni