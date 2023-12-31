import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QFileDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QIcon
import fitz

class PDFPrinter(object):
    def setupUi(self, MainWindow):
        self.resize(447, 250)
        MainWindow.setWindowTitle("DaYe PhotoStudio")
        MainWindow.setWindowIcon(QIcon("resource/logo.png"))
        MainWindow.setStyleSheet("background-color: rgb(59,63,66)")
        self.printButton = QPushButton("Open PDF File\n打开PDF文件")
        self.printButton.setStyleSheet("background-color: rgba(0,0,0,50);color:rgb(255,255,255)")
        self.printButton.clicked.connect(self.printPDF)

        layout = QVBoxLayout()
        layout.addWidget(self.printButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def printPDF(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf)")
        if filename:
            self.printDocument(filename)

    def printDocument(self, filename):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec() == QPrintDialog.PrintDialogAccepted:
            self.printPDFPages(filename, printer)

    def printPDFPages(self, filename, printer):
        doc = fitz.open(filename)
        painter = QPainter(printer)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
            image = pixmap.toImage()
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)
            painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
            painter.drawImage(printer.pageRect(), image, image.rect())
            if page_num < doc.page_count - 1:
                printer.newPage()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFPrinter()
    window.show()
    sys.exit(app.exec())
