from PySide6.QtCore import QSize, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QPushButton, QWidget, QLabel,QLineEdit
from PySide6.QtGui import QPixmap, QColor
from UI.Fallingword import FallingWord
import random
from UI.SoundFx import SoundFx
import os

STATE = False
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

# , y imagenes

class GamePage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.words = ["hola", "adios", "sol", "luna", "corazon"]
        self.falling_words = []
        self.alive_time = 0
        self.spawn_rate = 4000 # 4 seconds
        self.killed_words = 0
        self.life = 3
        self.sfx = SoundFx()

        self.background_image = QLabel(self)
        self.background_image.setGeometry(10, 10, 680, 680)
        img_path = os.path.join(ASSETS_DIR, "game_background.png")
        pixmap = QPixmap(img_path)
        self.background_image.setPixmap(pixmap)
        self.background_image.setScaledContents(True)




        # home_button_was_clicked button handler
        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(10, 10, 100, 50)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

        self.start_pause = QPushButton("Start", self)
        self.start_pause.setGeometry(570,10, 100, 50)
        self.start_pause.clicked.connect(self.start_pause_button_was_clicked)

        self.killed_words_label = QLabel(f"Killed words: {self.killed_words}", self)
        self.killed_words_label.setGeometry(120, 23, 250, 40)
        self.killed_words_label.setAlignment(Qt.AlignCenter)
        self.killed_words_label.setStyleSheet("""
                                    QLabel {
                                        background: rgba(20, 20, 30, 180);
                                        color: #F2F4FF;
                                        padding: 10px 16px;
                                        border-radius: 12px;
                                        font-size: 16px;
                                    }
                                """)

        self.life_label= QLabel(f"Lifes: {self.life}", self)
        self.life_label.setGeometry(380, 23, 150, 40)
        self.life_label.setAlignment(Qt.AlignCenter)
        self.life_label.setStyleSheet("""
                                    QLabel {
                                        background-color: rgba(20, 20, 30, 180);
                                        color: #F2F4FF;
                                        padding: 10px 16px;
                                        border-radius: 12px;    
                                        font-size: 16px;
                                    }
                                """)



        # keyboard
        self.keyboard = QLineEdit(self)
        self.keyboard.setGeometry(50, 600, 600, 40)
        self.keyboard.returnPressed.connect(self.on_enter_pressed)

        # GAME OVER
        self.game_over_label = QLabel("Game Over", self)
        self.game_over_label.setGeometry(200, 300, 200, 100)

        self.game_over_label.setStyleSheet("""
                    QLabel {
                        background: transparent;
                        color: white;
                        font-size: 60px;
                    }
                """)
        glow = QGraphicsDropShadowEffect(self.game_over_label)
        glow.setBlurRadius(100)
        glow.setOffset(0, 0)
        glow.setColor(Qt.GlobalColor.darkRed)

        shadow = QGraphicsDropShadowEffect(self.game_over_label)
        shadow.setBlurRadius(10)
        shadow.setOffset(1, 1)
        shadow.setColor(QColor(0, 0, 0))
        self.game_over_label.setGraphicsEffect(shadow)
        self.game_over_label.setGraphicsEffect(glow)
        self.game_over_label.adjustSize()
        self.game_over_label.hide()


        # timer update module
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1)  # 1/10 segundo

        # style
        self.start_pause.setObjectName("primary")
        self.killed_words_label.setObjectName("moss")
        self.home_button.setObjectName("danger")
        self.life_label.setObjectName("moss")

        self.update_clock()

    def home_button_was_clicked(self):
        global STATE
        if STATE:
            STATE = False
        QTimer.singleShot(1, lambda: self.go_next_page(1))

    def start_pause_button_was_clicked(self):
        global STATE
        if STATE:
            STATE = False
        else:
            STATE = True

    def on_enter_pressed(self):
        text = self.keyboard.text()
        print("User typed:", text)
        self.keyboard.clear()
        for fw in self.falling_words:
            if fw.alive and fw.text == text:
                fw.kill()
                self.killed_words+=1
                self.killed_words_label.setText(f"killed_words_label: {self.killed_words}")
                if self.spawn_rate > 300:
                    self.spawn_rate-=50
                self.sfx.play_killed_word()
                break

        pass

    def update_clock(self):
        global STATE
        self.alive_time += 1
        self.start_pause.setText("Start" if STATE == False else "Pause")
        if not STATE:
            return

        if self.alive_time % self.spawn_rate == 0:
            random_words = random.sample(self.words, 3)
            print (random_words)
            # self.alive_words = random_words
            speed = random.randint(3, 6) + (self.killed_words)
            for text in random_words:
                fw = FallingWord(self, text, speed=speed,size=random.randint(30, 60))
                self.falling_words.append(fw)


        bottom = 560
        for fw in self.falling_words:
            fw.update()
            if fw.y >= bottom:
                fw.kill()
                self.sfx.play_dead_word()
                self.life -=1
                self.life_label.setText(f"Lifes: {self.life}")
                if  self.life <= 0:
                    self.game_over()

        self.falling_words = [fw for fw in self.falling_words if fw.alive]

    def on_enter(self):
        global STATE
        STATE = False
        self.life = 3
        self.life_label.setText(f"Lifes: {self.life}")
        self.falling_words = []
        self.alive_time = 0
        self.spawn_rate = 4000  # 4 seconds
        self.killed_words = 0
        self.killed_words_label.setText(f"killed_words_label: {self.killed_words}")
        self.game_over_label.hide()

    def on_leave(self):
        for fw in self.falling_words:
            if fw.alive:
                fw.kill()
        global STATE
        STATE = False

    def game_over(self):
        global STATE
        STATE = False
        for fw in self.falling_words:
            if fw.alive:
                fw.kill()
        self.game_over_label.show()
        self.sfx.play_game_over()

