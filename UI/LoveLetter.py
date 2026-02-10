from PySide6.QtCore import QSize, Qt,QUrl, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from PySide6.QtGui import QPixmap, QMovie
import os
from UI.SoundFx import SoundFx
from PySide6.QtGui import QColor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")


class LoveLetterPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.sfx = SoundFx()

        # Image Sunset
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 680, 680)
        img_path = os.path.join(ASSETS_DIR, "sunset_love_letter.png")
        pixmap = QPixmap(img_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        # Letter

        self.letter_label = QLabel("Hola Amor\n" 
                                   "\n"
                                   " Te hice esta aplicacion para mostrarte mi amor y cariño, te amo \n"
                                   "un monton, sos lo mas bonito que me dio este mundo en tantos años.\n"
                                   " Ahora estamos juntos en Portugal y estoy tan contento!. Me imagino\n"
                                   "que te daras cuenta por mi cara. A la vez podemos escuchar el mar\n"
                                   "de tamsui. Escuchas las olas?\n"
                                   " Anyways, Mi pecho late tan fuerte cuando estoy contigo, y me \n"
                                   "emociona ser tu pareja, gracias por tanto amor, sos gentil, \n"
                                   "inteligente, amorosa, todo lo que esta bien en mi mundo. Te amo amor\n"
                                   "\n"
                                   "Feliz San Valentin jeje"


                                     , self)
        self.letter_label.setGeometry(50, 130, 600, 220)
        self.letter_label.setWordWrap(True)
        self.letter_label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: white;
            }
        """)
        shadow = QGraphicsDropShadowEffect(self.letter_label)
        shadow.setBlurRadius(10)
        shadow.setOffset(1, 1)
        shadow.setColor(QColor(0, 0, 0))
        self.letter_label.setGraphicsEffect(shadow)

        # home_button_was_clicked button handler
        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(300, 600, 100, 50)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

    def home_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(1))
        pass

    def on_enter(self):
        print("on_enter")

    def on_leave(self):
        print("on_leave")