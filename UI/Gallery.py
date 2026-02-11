from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtMultimedia import QMediaDevices, QCamera, QMediaCaptureSession
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPixmap, QMovie
import os
from UI.SoundFx import SoundFx

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
GIFS_DIR = os.path.join(ASSETS_DIR, "GIF")

class GalleryPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.sfx = SoundFx()

        # ---------- UI ----------
        self.header_label = QLabel("El amor de mi vida", self)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setGeometry(50, 20, 600, 50)
        self.header_label.setStyleSheet("""
            QLabel {
                background-color: rgba(20, 20, 30, 180);
                color: #F2F4FF;
                padding: 10px 16px;
                border-radius: 12px;
                font-size: 16px;
            }
        """)

        # gif handler
        self.stars_gif = QLabel(self)
        self.stars_gif.setGeometry(0, 0, 700, 700)
        self.stars_gif.setStyleSheet("background: transparent; border-radius: 12px;")
        self.stars_gif.setScaledContents(True)
        gif_path = os.path.join(GIFS_DIR, "stars.gif")
        self.movie = QMovie(gif_path)
        self.stars_gif.setMovie(self.movie)
        self.movie.start()

        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(290, 600, 100, 50)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

        # Widget donde se ve el video
        self.video_widget = QVideoWidget(self)
        self.video_widget.setGeometry(50, 90, 600, 430)
        self.video_widget.setStyleSheet("background: black; border-radius: 12px;")

        # ---------- CAM SETUP ----------
        self.capture_session = QMediaCaptureSession()
        self.capture_session.setVideoOutput(self.video_widget)

        self.camera = None  # se crea al prender

    def home_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(1))

    # Llamá esto cuando entres a la página si querés que se prenda sola
    def on_enter(self):
        self.start_camera()

    def on_leave(self):
        self.stop_camera()

    def start_camera(self):
        if self.camera is not None:
            return

        cameras = QMediaDevices.videoInputs()
        if not cameras:
            self.header_label.setText("No se detectó ninguna cámara")
            return

        # Elegí la primera cámara disponible
        self.camera = QCamera(cameras[0])
        self.capture_session.setCamera(self.camera)
        self.camera.start()

    def stop_camera(self):
        if self.camera is None:
            return
        self.camera.stop()
        self.camera = None
