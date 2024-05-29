import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  final String baseUrl = 'http://172.22.169.183:8000';

  // Metodo per iniziare il quiz
  Future<Map<String, dynamic>> startQuiz() async {
    //richiesta POST all'URL e attende la risposta al server
    final response = await http.post(Uri.parse('$baseUrl/gioca'));

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to load question');
    }
  }

  // Metodo per inviare la risposta
  Future<Map<String, dynamic>> submitAnswer(String answer) async {
    final response = await http.post(
      Uri.parse('$baseUrl/invia'),
      headers: <String, String>{'Content-Type': 'application/json; charset=UTF-8',},
      body: jsonEncode(<String, String>{'answer': answer}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to submit answer');
    }
  }
}
