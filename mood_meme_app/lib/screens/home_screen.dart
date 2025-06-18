// home_screen.dart
import 'package:flutter/material.dart';
import '../services/api_service.dart';
import '../screens/camera_view.dart';
import '../widgets/meme_display.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String emotion = '';
  String memeCaption = '';
  bool isLoading = false;

  Future<void> _detectEmotionAndGenerateMeme() async {
    setState(() => isLoading = true);

    try {
      // Step 1: Send image to backend (simulate for now)
      emotion = await ApiService.detectEmotion(); // Expects "happy" etc.
      memeCaption = await ApiService.getMemeForEmotion(emotion);
    } catch (e) {
      memeCaption = "Error: ${e.toString()}";
    }

    setState(() => isLoading = false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF9F0FF),
      appBar: AppBar(title: const Text('Mood Meme Generator')),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text("Camera Feed", style: TextStyle(fontSize: 20)),
          const SizedBox(height: 10),
          const SizedBox(width: 640, height: 480, child: CameraView()),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: isLoading ? null : _detectEmotionAndGenerateMeme,
            child: const Text("Detect Emotion & Generate Meme"),
          ),
          const SizedBox(height: 20),
          if (emotion.isNotEmpty)
            Text(
              "Detected Emotion: $emotion",
              style: const TextStyle(fontSize: 18),
            ),
          if (memeCaption.isNotEmpty) MemeDisplay(caption: memeCaption),
        ],
      ),
    );
  }
}
