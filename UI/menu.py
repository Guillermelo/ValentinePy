from numpy.lib.recfunctions import structured_to_unstructured

from UI.LoveLetter import LoveLetterPage

import sys
import random
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtCore import QUrl, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer, QRandomGenerator
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget, QMessageBox
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from UI.Counter import CounterPage
from UI.Game import GamePage
from UI.SoundFx import SoundFx
from UI.LoveStory import LoveStoryPage
from UI.LoveLetter import LoveLetterPage
from UI.Gallery import GalleryPage

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
GIFS_DIR = os.path.join(ASSETS_DIR, "GIF")


class StartPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.setMouseTracking(True)
        self.escape_radius = 100

        self.sfx = SoundFx()

        # Text
        self.label = QLabel("Do you want to be my Valentine?", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("""
                                font-size: 22px;
                                font-weight: 900;
                                letter-spacing: 1px;
                                color: #f2f7ff;
                                """)
        self.label.setGeometry(50, 20, 600, 200)  # no funciona solucionar

        # gif handler
        self.fheart_gif = QLabel(self)
        self.fheart_gif.setGeometry(0, 0, 700, 700)
        self.fheart_gif.setStyleSheet("background: transparent; border-radius: 12px;")
        self.fheart_gif.setScaledContents(True)
        gif_path = os.path.join(GIFS_DIR, "valentine.gif")
        self.movie = QMovie(gif_path)
        self.fheart_gif.setMovie(self.movie)


        # yes button handler
        self.yes_button = QPushButton("Yes", self)
        self.yes_button.setObjectName("moss")
        self.yes_button.setGeometry(100, 200, 120, 60)
        self.yes_button.clicked.connect(self.yes_button_was_clicked)
        self.yes_button.clicked.connect(self.sfx.play_click)

        self.no_button = QPushButton("No", self)
        self.no_button.setObjectName("danger")
        self.no_button.setGeometry(450, 200, 120, 60)
        self.no_button.clicked.connect(self.no_button_was_clicked)



        # No button handler
        self.no_anim = QPropertyAnimation(self.no_button, b"pos", self)
        self.no_anim.setDuration(400)  # ms 1000
        self.no_anim.setEasingCurve(QEasingCurve.OutCubic)

    def mouseMoveEvent(self, event):
        mouse_pos = event.position().toPoint()

        btn_center = self.no_button.geometry().center()
        distance = (mouse_pos - btn_center).manhattanLength()

        if distance < self.escape_radius:
            self.move_no_button()
            pass

    def move_no_button(self):
        if self.no_anim.state() == QPropertyAnimation.Running:
            return

        max_x = self.width() - self.no_button.width()
        max_y = self.height() - self.no_button.height()

        x = random.randint(0, max_x)
        y = random.randint(80, max_y)

        start_pos = self.no_button.pos()
        end_pos = QPoint(x, y)

        self.no_anim.stop()
        self.no_anim.setStartValue(start_pos)
        self.no_anim.setEndValue(end_pos)
        self.no_anim.start()

    def no_button_was_clicked(self):
        w = self.no_button.width() - 20
        h = self.no_button.height() - 10
        self.no_button.resize(w, h)

        w2 = self.yes_button.width() + 200
        h2 = self.yes_button.height() + 100
        self.yes_button.resize(w2, h2)
        self.move_no_button()
        self.label.setText("Amor te habras equivocado... espero que selecciones el correcto...")
        self.label.setStyleSheet("""
                                        font-size: 13px;
                                        font-weight: 900;
                                        letter-spacing: 1px;
                                        color: #f2f7ff;
                                        """)
        pass

    def yes_button_was_clicked(self):
        self.label.setText("GRACIAS AMOR, TE AMO ❤️❤️")
        self.label.setStyleSheet("""
                                font-size: 35px;
                                font-weight: 900;
                                letter-spacing: 1px;
                                color: #f2f7ff;
                                """)
        self.movie.start()
        QTimer.singleShot(2000, lambda : self.go_next_page(1)) # 2500
        pass

class SecondPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.setObjectName("screen")
        self.sfx = SoundFx()

        self.label = QLabel("Where do u want to go?", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(150, 20, 400, 40)

        self.scene = QLabel(self)
        self.scene.setGeometry(0, 0, 700, 700)
        self.scene.setPixmap(QPixmap(os.path.join(ASSETS_DIR, "background_2.png")))
        self.scene.setScaledContents(True)



        # counter_button_was_clicked button handler
        self.counter_button = QPushButton("Counter", self)
        self.counter_button.setGeometry(100, 100, 150, 75)
        self.counter_button.clicked.connect(self.sfx.play_click)
        self.counter_button.clicked.connect(self.counter_button_was_clicked)

        # letter_button_was_clicked button handler
        self.letter_button = QPushButton("Love Letter", self)
        self.letter_button.setGeometry(450, 100, 150, 75)
        self.letter_button.clicked.connect(self.sfx.play_click)
        self.letter_button.clicked.connect(self.letter_button_was_clicked)

        # game_button_was_clicked button handler
        self.game_button = QPushButton("Game", self)
        self.game_button.setGeometry(100, 300, 150, 75)
        self.game_button.clicked.connect(self.sfx.play_click)
        self.game_button.clicked.connect(self.game_button_was_clicked)

        # game_button_was_clicked button handler
        self.gallery_button = QPushButton("Mi Persona Fav", self)
        self.gallery_button.setGeometry(450, 300, 150, 75)
        self.gallery_button.clicked.connect(self.sfx.play_click)
        self.gallery_button.clicked.connect(self.gallery_button_was_clicked)

        # love_button_was_clicked button handler
        self.love_button = QPushButton("Love Story", self)
        self.love_button.setGeometry(100, 500, 150, 75)
        self.love_button.clicked.connect(self.sfx.play_click)
        self.love_button.clicked.connect(self.love_story_button_was_clicked)

        # error_button_was_clicked button handler
        self.error_button = QPushButton("???", self)
        self.error_button.setGeometry(450, 500, 150, 75)
        self.error_button.clicked.connect(self.error_button_was_clicked)


        # style
        self.label.setObjectName("title")
        self.counter_button.setObjectName("primary")
        self.letter_button.setObjectName("primary")
        self.game_button.setObjectName("primary")
        self.gallery_button.setObjectName("primary")
        self.love_button.setObjectName("primary")
        self.error_button.setObjectName("danger")

    def letter_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(2))
        pass

    def counter_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(4))
        pass

    def game_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(3))
        pass

    def gallery_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(6))
        pass

    def love_story_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(5))
        pass

    def error_button_was_clicked(self):
        QMessageBox.critical(
            None,
            "Error",
            "Ocurrió un error"
        )

        self.errors = []

        # Zona permitida (en coordenadas globales de pantalla)
        screen = QApplication.primaryScreen()
        avail = screen.availableGeometry()  # evita taskbar

        # Ejemplo: zona central (60% del ancho/alto de la pantalla)
        zone_w = int(avail.width() * 0.60)
        zone_h = int(avail.height() * 0.60)
        zone_x = avail.x() + (avail.width() - zone_w) // 2
        zone_y = avail.y() + (avail.height() - zone_h) // 2

        for i in range(15):
            QApplication.beep()

            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("TOO MUCH LOVE!!")
            msg.setText(f"TE AMO #{i + 1}")

            # Importante: mostrar primero para que tenga tamaño real
            msg.show()
            msg.adjustSize()

            w = msg.frameGeometry().width()
            h = msg.frameGeometry().height()

            # Random dentro de la zona, asegurando que no se salga
            max_x = zone_x + max(0, zone_w - w)
            max_y = zone_y + max(0, zone_h - h)

            rx = QRandomGenerator.global_().bounded(zone_x, max_x + 1)
            ry = QRandomGenerator.global_().bounded(zone_y, max_y + 1)

            msg.move(rx, ry)

            self.errors.append(msg)

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sfx = SoundFx()

        # background music
        self.audio_out_lobby = QAudioOutput(self)
        self.audio_out_lobby.setVolume(0.8)
        self.lobby_music = QMediaPlayer(self)
        self.lobby_music.setAudioOutput(self.audio_out_lobby)
        self.lobby_music.setSource(QUrl.fromLocalFile(
            os.path.join(ASSETS_DIR, "Fondo.wav")
        ))
        self.lobby_music.setLoops(QMediaPlayer.Loops.Infinite)

        self.lobby_music.play()

        self.audio_out_story = QAudioOutput()
        # self.audio_out.setVolume(0.8)
        self.story_music = QMediaPlayer(self)
        self.story_music.setAudioOutput(self.audio_out_story)
        self.story_music.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "cuando_me_enamoro_chill.wav")))
        self.story_music.setLoops(QMediaPlayer.Loops.Infinite)

        self.audio_out_waves = QAudioOutput(self)
        self.waves_music =QMediaPlayer(self)
        self.waves_music.setAudioOutput(self.audio_out_waves)
        self.waves_music.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "waves.wav")))
        self.waves_music.setLoops(QMediaPlayer.Loops.Infinite)

        # Base Windows Adjustments
        self.setObjectName("screen")
        self.setWindowTitle("For Lisa")
        self.setFixedSize(700,700)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.index_page = 0

        # Page indexing
        self.page1 = StartPage(self.go_to_next)  # index 0
        self.page2 = SecondPage(self.go_to_next)  # index 1
        self.page3 = LoveLetterPage(self.go_to_next)  # index 2
        self.page4 = GamePage(self.go_to_next)  # index 3
        self.page5 = CounterPage(self.go_to_next)  # index 4
        self.page6 = LoveStoryPage(self.go_to_next)  # index 5
        self.page7 = GalleryPage(self.go_to_next)  # index 6

        self.stack.addWidget(self.page1)  # index 0
        self.stack.addWidget(self.page2)  # index 1
        self.stack.addWidget(self.page3)  # index 2
        self.stack.addWidget(self.page4)  # index 3
        self.stack.addWidget(self.page5)  # index 4
        self.stack.addWidget(self.page6)  # index 5
        self.stack.addWidget(self.page7)  # index 6

    def go_to_next(self, index_page):

        current = self.stack.currentWidget()
        # self.sfx.play_click()
        if hasattr(current, "on_leave"): # before changing the index
            current.on_leave()
        self.stack.setCurrentIndex(index_page)
        new_page = self.stack.currentWidget()

        if hasattr(new_page, "on_enter"):
            new_page.on_enter()

        pages_with_music = {0,1,3,4}

        if index_page in pages_with_music :
            self.lobby_music.play()
        else :
            self.lobby_music.stop()

        if index_page == 5:
            self.story_music.play()
        else:
            self.story_music.stop()

        if index_page == 2:
            self.waves_music.play()
        else:
            self.waves_music.stop()




