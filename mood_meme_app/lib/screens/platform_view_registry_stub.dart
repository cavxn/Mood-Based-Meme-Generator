class PlatformViewRegistry {
  void registerViewFactory(String viewType, dynamic Function(int) viewFactory) {
    throw UnsupportedError(
      'platformViewRegistry is not supported on this platform',
    );
  }
}

final platformViewRegistry = PlatformViewRegistry();
