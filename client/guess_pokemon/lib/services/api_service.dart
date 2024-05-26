import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  final String baseUrl = 'http://localhost:50ù00';

  Future<Map<String, dynamic>> startQuiz() async {
    final response = await http.post(Uri.parse('$baseUrl/gioca'));

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to load question');
    }
  }

  Future<Map<String, dynamic>> submitAnswer(String answer) async {
    final response = await http.post(
      Uri.parse('$baseUrl/invia'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{'answer': answer}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to submit answer');
    }
  }
}
