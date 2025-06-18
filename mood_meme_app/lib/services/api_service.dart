// api_service.dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const baseUrl = "http://127.0.0.1:8000";

  static Future<String> detectEmotion() async {
    // Simulate image-based emotion detection
    final response = await http.post(Uri.parse("$baseUrl/detect_emotion"));
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['emotion'];
    } else {
      throw Exception("Failed to detect emotion");
    }
  }

  static Future<String> getMemeForEmotion(String emotion) async {
    final response = await http.post(
      Uri.parse("$baseUrl/generate_caption"),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'emotion': emotion}),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['caption'];
    } else {
      throw Exception("Failed to generate meme");
    }
  }
}
