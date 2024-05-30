import 'package:flutter/material.dart';
import 'services/api_service.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Pokémon Quiz',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.red),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Pokémon Quiz Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final ApiService apiService = ApiService();
  List<String> _options = [];
  String _question = '';
  int _score = 0;
  int _turns = 0;
  bool _isLoading = false;
  String _message = '';

  void _startQuiz() async {
    if (mounted) {
      setState(() {
        _isLoading = true;
        _message = '';
      });
    }

    try {
      final data = await apiService.startQuiz();
      print('Quiz started: $data');
      if (mounted) {
        setState(() {
          _question = data['question'];
          _options = List<String>.from(data['options']);
          _isLoading = false;
        });
      }
    } catch (e) {
      print('Failed to start quiz: $e');
      if (mounted) {
        setState(() {
          _isLoading = false;
          _message = 'Failed to load question';
        });
      }
    }
  }

  void _submitAnswer(String answer) async {
    if (mounted) {
      setState(() {
        _isLoading = true;
        _message = '';
      });
    }

    try {
      final data = await apiService.submitAnswer(answer);
      if (mounted) {
        setState(() {
          _score = data['score'];
          _turns = data['turns'];
          _message = data['correct'] ? 'Correct!' : 'Incorrect!';
          _question = data['question'] ?? '';
          _options = List<String>.from(data['options'] ?? []);
          _isLoading = false;
        });
      }
    } catch (e) {
      print('Failed to submit answer: $e');
      if (mounted) {
        setState(() {
          _isLoading = false;
          _message = 'Failed to submit answer';
        });
      }
    }
  }

  @override
  void initState() {
    super.initState();
    _startQuiz();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
        backgroundColor: Colors.red,
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  if (_question.isNotEmpty)
                    Column(
                      children: [
                        Text(
                          'Choose the correct Pokémon:',
                          style: Theme.of(context).textTheme.headline6,
                        ),
                        for (var option in _options)
                          ElevatedButton(
                            onPressed: () => _submitAnswer(option),
                            child: Text(option),
                          ),
                      ],
                    ),
                  if (_message.isNotEmpty) Text(_message),
                  const SizedBox(height: 20),
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
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: _startQuiz,
        tooltip: 'Restart Quiz',
        child: const Icon(Icons.refresh),
      ),
    );
  }
}