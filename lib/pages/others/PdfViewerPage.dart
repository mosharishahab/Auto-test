// [AutoFix by GPT] Style added
import 'package:flutter/material.dart';
import 'package:easy_pdf_viewer/easy_pdf_viewer.dart';

class PdfViewerPage extends StatelessWidget {
  final PDFDocument document;

  PdfViewerPage({required this.document});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('PDF Viewer', style: TextStyle(fontSize: 16)),
      ),
      body: PDFViewer(
        document: document,
        lazyLoad: false,
        scrollDirection: Axis.horizontal,
        showPicker: false,
        showIndicator: false,
        showNavigation: false,
      ),
    );
  }
}
