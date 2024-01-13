import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from vectormanagementwindow import VectorManagementWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Singleton list")

        vector_management_window = VectorManagementWindow(self)
        self.setCentralWidget(vector_management_window)  # uses the preset layout of a QMainWindow, cf https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html#qt-main-window-framework


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window1 = MainWindow()
    window1.show()

    window2 = MainWindow()
    window2.show()

    sys.exit(app.exec())
