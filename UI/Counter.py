from PySide6.QtCore import QSize, Qt,QPoint, QPropertyAnimation, QEasingCurve, QTimer
from zoneinfo import ZoneInfo
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from datetime import datetime

from UI.SoundFx import SoundFx

TZ_TAIPEI = ZoneInfo("Asia/Taipei")

class CounterPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.sfx = SoundFx()

        self.together_since = datetime(2025, 12, 8, 1, 30, 0, tzinfo=TZ_TAIPEI)
        self.know_each_other_since = datetime(2025, 8, 16, 22, 00, 0, tzinfo=TZ_TAIPEI)

        self.counter_name_label = QLabel("Together Since:",self)
        self.counter_name_label.setGeometry(100, 200, 500, 60)
        self.counter_name_label.setAlignment(Qt.AlignCenter)
        self.counter_name_label.setStyleSheet("font-size: 20px;")

        self.counter_label = QLabel(self)
        self.counter_label.setGeometry(100, 250, 500, 60)
        self.counter_label.setAlignment(Qt.AlignCenter)
        self.counter_label.setStyleSheet("font-size: 20px;")

        self.counter2_name_label = QLabel("Know each other Since:", self)
        self.counter2_name_label.setGeometry(100, 300, 500, 60)
        self.counter2_name_label.setAlignment(Qt.AlignCenter)
        self.counter2_name_label.setStyleSheet("font-size: 20px;")

        self.counter_label2 = QLabel(self)
        self.counter_label2.setGeometry(100, 350, 500, 60)
        self.counter_label2.setAlignment(Qt.AlignCenter)
        self.counter_label2.setStyleSheet("font-size: 20px;")

        # home_button_was_clicked button handler
        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(300, 600, 100, 50)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

        # style

        self.counter_name_label.setProperty("role", "hud")
        self.counter_label.setProperty("role", "hud")
        self.counter2_name_label.setProperty("role", "hud")
        self.counter_label2.setProperty("role", "hud")

        self.counter_name_label.setObjectName("title")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)


    def update_counter(self):
        now = datetime.now(TZ_TAIPEI)
        delta = now - self.together_since
        total_seconds = int(delta.total_seconds())
        days = total_seconds // 86400
        hours = (total_seconds % 86400) // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        self.counter_label.setText(
            f"{days} DAYS {hours:02d} HOURS {minutes:02d} MINUTES {seconds:02d} SECONDS"
        )
        delta2 = now - self.know_each_other_since
        total_seconds2 = int(delta2.total_seconds())
        days2 = total_seconds2 // 86400
        hours2 = (total_seconds2 % 86400) // 3600
        minutes2 = (total_seconds2 % 3600) // 60
        seconds2 = total_seconds2 % 60
        if seconds2 == 0:
            self.sfx.play_clock_big_tick()
        else:
            self.sfx.play_clock_tick()

        self.counter_label2.setText(
            f"{days2} DAYS {hours2:02d} HOURS {minutes2:02d} MINUTES {seconds2:02d} SECONDS"
        )

    def home_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(1))

    def on_enter(self):
        self.timer.start(1000)  # 1 segundo
        self.update_counter()

    def on_leave(self):
        self.timer.stop()
