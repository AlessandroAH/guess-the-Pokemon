from pokemon import PokemonQuiz

class Quiz:
    def __init__(self):
        self.pokemon_quiz = PokemonQuiz()
        self.current_question = 0
        self.AllPokemon = self.pokemon_quiz.get_pokemon_list()
        self.correct_answer = None
        self.score = 0
        self.turns = 0
        self.question = "Qual è questo Pokémon?"

    # Funzione per ottenere la prossima domanda
    def get_next_question(self):
        if self.current_question < 10:
            pokemon = self.pokemon_quiz.get_random_pokemon()
            if pokemon:
                self.correct_answer = pokemon
                options = self.pokemon_quiz.generate_options(self.correct_answer,self.AllPokemon)
                self.current_question += 1
                self.turns += 1
                return self.question, options , pokemon['image_url']
        else:
            return None
    
    # Funzione per inviare una risposta
    def submit_answer(self, answer):
        if answer == self.correct_answer['name']:
            self.score += 1
            correct = True
        else:
            correct = False
        question , options, image_url  = self.get_next_question()
        return correct, question , options , image_url 
    
    #Metodo per resettare il quiz
    def reset(self):
        self.current_question = 0
        self.score = 0
        self.correct_answer = None
        self.turns = 0