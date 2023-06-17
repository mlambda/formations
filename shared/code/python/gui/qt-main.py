import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QMainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()