import time
from UI.LoveLetter import LoveLetterPage
from PySide6.QtWidgets import QApplication
from UI.menu import Menu
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Menu()
    window.show()
    app.exec()

