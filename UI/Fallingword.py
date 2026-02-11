from PySide6.QtCore import QSize, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtGui import QFont

import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class FallingWord:
    def __init__(self, parent, text, size, x=None, y=30, speed=2):
        self.x = random.randint(100, 600) if x is None else x
        self.y = y
        self.speed = speed / 100
        self.text = text
        self.size = size
        self.alive = True

        self.label = QLabel(text, parent)
        self.label.move(int(self.x), int(self.y))

        game_size = size

        self.label.setStyleSheet(f"""
            QLabel {{
                color: #F2F7FF;
                background: transparent;
                font-family: "Cascadia Mono", Consolas, monospace;
                font-size: {game_size}px;
                font-weight: 900;
                letter-spacing: 1px;
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

    def pick_spawn_x(self, text, size, y=30, tries=40, min_gap=12):
        # márgenes (ajustá a tu pantalla)
        left = 20
        right = 680 - 20

        # estimación inicial de ancho; si querés ultra exacto, podemos usar QFontMetrics
        approx_w = max(60, int(len(text) * size * 0.55))
        max_x = max(left, right - approx_w)

        alive = [fw for fw in self.falling_words if fw.alive]

        for _ in range(tries):
            x = random.randint(left, max_x)

            # caja candidata (aprox)
            cand_l = x
            cand_t = y
            cand_r = x + approx_w
            cand_b = y + size

            ok = True
            for fw in alive:
                r = fw.label.geometry()  # real
                l2, t2, r2, b2 = r.left(), r.top(), r.right(), r.bottom()

                overlap = not (
                        cand_r + min_gap < l2 or
                        cand_l - min_gap > r2 or
                        cand_b + min_gap < t2 or
                        cand_t - min_gap > b2
                )
                if overlap:
                    ok = False
                    break

            if ok:
                return x

        return random.randint(left, max_x)
