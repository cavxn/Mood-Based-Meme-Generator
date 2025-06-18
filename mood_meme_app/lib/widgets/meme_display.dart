// meme_display.dart
import 'package:flutter/material.dart';

class MemeDisplay extends StatelessWidget {
  final String caption;

  const MemeDisplay({super.key, required this.caption});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const SizedBox(height: 10),
        Text(
          caption,
          textAlign: TextAlign.center,
          style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
        ),
      ],
    );
  }
}
