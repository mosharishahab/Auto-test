```dart
import 'package:flutter/material.dart';

void main() {
  runApp(DualApp());
}

class DualApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dual App',
      home: Scaffold(
        appBar: AppBar(title: Text('Dual App')),
        body: Center(child: Text('Hello, World!')),
      ),
    );
  }
}
```