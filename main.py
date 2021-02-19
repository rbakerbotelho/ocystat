from potentiostat import Potentiostat
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar, QToolBar, QAction
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My Ocy UI")
        self.setCentralWidget(QLabel("I'm a Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction(' &Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm a status bar")
        self.setStatusBar(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
