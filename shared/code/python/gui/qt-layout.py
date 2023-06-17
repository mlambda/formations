class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)