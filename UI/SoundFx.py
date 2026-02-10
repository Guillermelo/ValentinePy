# UI/SoundFx.py
import os
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

class SoundFx:
    def __init__(self):
        self.click = QSoundEffect()
        self.click.setSource(QUrl.fromLocalFile(
            os.path.join(ASSETS_DIR, "CLICK.wav")
        ))
        self.click.setVolume(0.4)

        self.deadWord = QSoundEffect()
        self.deadWord.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "Deadword.wav")))
        self.deadWord.setVolume(0.4)

        self.clock_tick = QSoundEffect()
        self.clock_tick.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "clock_tick.wav")))
        self.clock_tick.setVolume(0.2)

        self.clock_big_tick = QSoundEffect()
        self.clock_big_tick.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "big_tick.wav")))
        self.clock_big_tick.setVolume(0.9)

        self.killed_word = QSoundEffect()
        self.killed_word.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "killed_word.wav")))
        self.killed_word.setVolume(0.5)

        self.game_over = QSoundEffect()
        self.game_over.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "game_over.wav")))
        self.game_over.setVolume(0.9)

        self.type = QSoundEffect()
        self.type.setSource(QUrl.fromLocalFile(os.path.join(ASSETS_DIR, "typing.wav")))
        self.type.setVolume(0.7)



    def play_clock_tick(self):
        self.clock_tick.play()

    def play_clock_big_tick(self):
        self.clock_big_tick.play()

    def play_dead_word(self):
        self.deadWord.play()

    def play_click(self):
        self.click.play()

    def play_killed_word(self):
        self.killed_word.play()

    def play_game_over(self):
        self.game_over.play()

    def play_type(self):
        self.type.play()