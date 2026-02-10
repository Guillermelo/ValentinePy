from PySide6.QtCore import QSize, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtGui import QFont

import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class FallingWord:
    def __init__(self, parent,text, size,y=0, speed = 2):
        self.x = random.randint(50, 550)
        self.y = random.randint(30, 110)
        self.speed = speed/100
        self.text = text
        self.size = size
        self.alive = True


        self.label = QLabel(text, parent)
        self.label.move(self.x, self.y)

        game_size = size  # probá 26-34



        # idk wtf is this
        self.label.setStyleSheet(f"""
            QLabel {{
                color: #F2F7FF;
                background: transparent;
                font-family: "Cascadia Mono", Consolas, monospace;
                font-size: {game_size}px;
                font-weight: 900;
                letter-spacing: 1px;

                text-shadow:
                    2px 2px 0px #000000,
                   -2px 2px 0px #000000,
                    2px -2px 0px #000000,
                   -2px -2px 0px #000000;
            }}
        """)
        glow = QGraphicsDropShadowEffect(self.label)
        glow.setBlurRadius(50)
        glow.setOffset(0, 0)
        glow.setColor(Qt.GlobalColor.darkRed)
        self.label.setGraphicsEffect(glow)

        self.label.adjustSize()
        self.label.show()

    def update(self):
        if not self.alive:
            return
        self.y += self.speed
        self.label.move(self.x, self.y)

    def kill(self):
        self.alive = False
        self.label.hide()
        self.label.deleteLater()