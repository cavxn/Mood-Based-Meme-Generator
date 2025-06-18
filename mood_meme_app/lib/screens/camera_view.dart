import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:flutter/material.dart';
import 'platform_view_registry.dart' as platform_view_registry;

import 'dart:html' as html;

class CameraView extends StatefulWidget {
  const CameraView({super.key});

  @override
  State<CameraView> createState() => _CameraViewState();
}

class _CameraViewState extends State<CameraView> {
  late html.VideoElement _video;

  @override
  void initState() {
    super.initState();

    if (kIsWeb) {
      _video = html.VideoElement()
        ..autoplay = true
        ..width = 640
        ..height = 480
        ..style.border =
            '1px solid black' // optional: to see video bounds
        ..style.objectFit = 'cover';

      html.window.navigator.mediaDevices
          ?.getUserMedia({'video': true})
          .then((stream) {
            _video.srcObject = stream;
          })
          .catchError((e) {
            print("Error accessing camera: $e");
          });

      platform_view_registry.platformViewRegistry.registerViewFactory(
        'camera-html',
        (int viewId) => _video,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (!kIsWeb) {
      return const Center(child: Text('Camera only supported on Web'));
    }

    return Center(
      child: SizedBox(
        width: 640,
        height: 480,
        child: const HtmlElementView(viewType: 'camera-html'),
      ),
    );
  }
}
