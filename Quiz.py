from pokemon import PokemonQuiz

class Quiz:
    def __init__(self):
        self.pokemon_quiz = PokemonQuiz()
        self.current_question = 0
        self.AllPokemon = self.pokemon_quiz.get_pokemon_list()
        self.correct_answer = None

    # Funzione per ottenere la prossima domanda
    def get_next_question(self):
        if self.current_question < 10:
            pokemon = self.pokemon_quiz.get_random_pokemon()
            if pokemon:
                self.correct_answer = pokemon
                options = self.pokemon_quiz.generate_options(self.correct_answer,self.AllPokemon)
                self.current_question += 1
                return options
        else:
            return None