import 'package:flutter/material.dart';
import 'services/api_service.dart';

// Funzione principale che avvia l'app
void main() {
  runApp(const MyApp());
}

// Definizione della classe MyApp che estende StatelessWidget
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Pokémon Quiz', // Titolo dell'app
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.red), // Tema dell'app basato sul colore rosso
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Pokémon Quiz Home Page'), // Pagina iniziale dell'app
    );
  }
}

// Definizione della classe MyHomePage che estende StatefulWidget
class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title; // Titolo della pagina

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

// Definizione della classe di stato _MyHomePageState per MyHomePage
class _MyHomePageState extends State<MyHomePage> {
  final ApiService apiService = ApiService(); // Istanza del servizio API
  List<String> _options = []; // Lista delle opzioni di risposta
  String _question = ''; // Testo della domanda
  String _imageUrl = ''; // URL dell'immagine
  int _score = 0; // Punteggio
  int _turns = 0; // Numero di turni
  bool _isLoading = false; // Indica se il quiz è in fase di caricamento
  String _message = ''; // Messaggio di stato
  bool _finished = false; // Indica se il quiz è terminato

  // Funzione che avvia il quiz
  void _startQuiz() async {
    if (mounted) {
      setState(() {
        _isLoading = true;
        _message = '';
        _finished = false;
      });
    }

    try {
      final data = await apiService.startQuiz(); // Richiesta per avviare il quiz
      print('Quiz started: $data');
      if (mounted) {
        setState(() {
          _question = data['question'];
          _options = List<String>.from(data['options']);
          _imageUrl = data['image_url'];
          _isLoading = false;
        });
      }
    } catch (e) {
      print('Failed to start quiz: $e');
      if (mounted) {
        setState(() {
          _isLoading = false;
          _message = 'Failed to load question'; // Messaggio di errore in caso di fallimento
        });
      }
    }
  }

  // Funzione che riavvia il quiz
  void _restartQuiz() {
    if (mounted) {
      setState(() {
        _score = 0;
        _turns = 0;
        _message = '';
        _finished = false;
      });
      apiService.restartQuiz(); // Richiesta per riavviare il quiz
      _startQuiz(); // Avvia nuovamente il quiz
    }
  }

  // Funzione che invia la risposta selezionata
  void _submitAnswer(String answer) async {
    if (mounted) {
      setState(() {
        _isLoading = true;
        _message = '';
      });
    }

    try {
      final data = await apiService.submitAnswer(answer); // Richiesta per inviare la risposta
      if (mounted) {
        setState(() {
          _score = data['score'];
          _turns = data['turns'];
          _message = data['correct'] ? 'Correct!' : 'Incorrect!'; // Messaggio di esito della risposta
          if (data['finished'] == true) {
            _finished = true;
            _question = '';
            _options = [];
            _imageUrl = '';
          } else {
            _question = data['question'] ?? '';
            _options = List<String>.from(data['options'] ?? []);
            _imageUrl = data['image_url'] ?? '';
          }
          _isLoading = false;
        });
      }
    } catch (e) {
      print('Failed to submit answer: $e');
      if (mounted) {
        setState(() {
          _isLoading = false;
          _message = 'Failed to submit answer'; // Messaggio di errore in caso di fallimento
        });
      }
    }
  }

  @override
  void initState() {
    super.initState();
    _startQuiz(); // Avvia il quiz all'inizializzazione dello stato
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        backgroundColor: Colors.red, // Colore di sfondo della barra dell'app
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator()) // Indicatore di caricamento
          : Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  if (_finished)
                    Column(
                      children: [
                        Text(
                          'Finito il quiz!',
                          style: Theme.of(context).textTheme.headline4,
                        ),
                        Text(
                          'Score: $_score',
                          style: Theme.of(context).textTheme.headline5,
                        ),
                        Text(
                          'Turns: $_turns',
                          style: Theme.of(context).textTheme.headline5,
                        ),
                      ],
                    )
                  else if (_question.isNotEmpty)
                    Column(
                      children: [
                        if (_imageUrl.isNotEmpty)
                          Image.network(_imageUrl, height: 220, width: 220), // Per modificare la grandezza dell'immagine
                        Text(
                          'Choose the correct Pokémon:',
                          style: Theme.of(context).textTheme.headline6,
                        ),
                        for (var option in _options)
                          ElevatedButton(
                            onPressed: () => _submitAnswer(option), // Invio della risposta selezionata
                            child: Text(option),
                          ),
                      ],
                    ),
                  if (_message.isNotEmpty) Text(_message), // Visualizzazione del messaggio di stato
                  const SizedBox(height: 20),
                  if (!_finished)
                    Column(
                      children: [
                        Text(
                          'Score: $_score',
                          style: Theme.of(context).textTheme.headline5,
                        ),
                        Text(
                          'Turns: $_turns',
                          style: Theme.of(context).textTheme.headline5,
                        ),
                      ],
                    ),
                ],
              ),
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _restartQuiz, // Riavvio del quiz
        tooltip: 'Restart Quiz',
        child: const Icon(Icons.refresh),
      ),
    );
  }
}
