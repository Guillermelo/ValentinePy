from PySide6.QtCore import QUrl, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from UI.SoundFx import SoundFx
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

class GalleryPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.sfx = SoundFx()

        self.songs = [
            os.path.join(ASSETS_DIR, "cuando_me_enamoro.wav"),
        ]

        self.audio_out_lobby = QAudioOutput(self)
        self.audio_out_lobby.setVolume(0.8)
        self.playlist_music = QMediaPlayer(self)
        self.playlist_music.setAudioOutput(self.audio_out_lobby)
        self.playlist_music.setSource(QUrl.fromLocalFile(
            os.path.join(ASSETS_DIR, "waves.wav")
        ))
        self.playlist_music.setLoops(QMediaPlayer.Loops.Infinite)





        # song_1_button_was_clicked button handler
        self.song_1_button = QPushButton("Cuando Me Enamoro", self)
        self.song_1_button.setGeometry(100, 100, 180, 75)
        self.song_1_button.clicked.connect(self.sfx.play_click)
        self.song_1_button.clicked.connect(self.song_1_button_was_clicked)



        # home_button_was_clicked button handler
        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(290, 600, 100, 50)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

    def home_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(1))

    def song_1_button_was_clicked(self):
        self.playlist_music.setSource(QUrl.fromLocalFile(
            self.songs[0]
        ))
        self.playlist_music.play()
        pass



    def on_enter(self):
        self.playlist_music.play()
        print("on_enter")

    def on_leave(self):
        self.playlist_music.stop()
        print("on_leave")
