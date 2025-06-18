import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(MoodMemeApp());
}

class MoodMemeApp extends StatelessWidget {
  const MoodMemeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mood Meme Generator',
      theme: ThemeData(
        brightness: Brightness.light,
        primarySwatch: Colors.purple,
      ),
      home: HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
