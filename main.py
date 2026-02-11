import time
from UI.LoveLetter import LoveLetterPage
from PySide6.QtWidgets import QApplication
from UI.menu import Menu
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    /* =========================
       GAME HUD THEME (navy / moss / dark red)
       ========================= */

    /* Base */
    QWidget {
        background-color: #070b14;      /* almost-black navy */
        color: #e7eefc;
        font-family: "Cascadia Mono", "Consolas", "Segoe UI", monospace;
        font-size: 15px;
    }

    /* Subtle scanlines (optional feel): apply by setting objectName="screen" to root pages */
    QWidget#screen {
        background-color: qlineargradient(
            x1:0, y1:0, x2:0, y2:1,
            stop:0 #070b14,
            stop:1 #05070e
        );
    }

    /* Panels (inventory-window feel) */
    QWidget#panel {
        background-color: #0b1324;
        border: 1px solid #243558;
        border-radius: 14px;
    }

    QWidget#panel2 {
        background-color: #08101f;
        border: 1px solid #1b2946;
        border-radius: 14px;
    }

    /* Titles */
    QLabel#title {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: 1px;
        color: #f2f7ff;
    }

    QLabel#subtitle {
        font-size: 13px;
        color: #aebbd4;
    }

    /* HUD labels (use property role="hud") */
    QLabel[role="hud"] {
        background-color: rgba(20, 20, 30, 180);
        border: 1px solid #243558;
        border-radius: 10px;
        padding: 8px 10px;
        color: #e7eefc;
    }

    /* =========================
       Buttons (arcade)
       ========================= */
    QPushButton {
        background-color: #0e1a33;
        border: 1px solid #2c4574;
        border-radius: 12px;
        padding: 10px 14px;
        font-weight: 800;
        color: #e7eefc;
    }

    /* Hover glow */
    QPushButton:hover {
        background-color: #132349;
        border: 1px solid #4f78c2;
    }

    /* Pressed "push-in" */
    QPushButton:pressed {
        background-color: #0a142a;
        border: 1px solid #1f3560;
        padding-top: 12px;
        padding-bottom: 8px;
    }

    /* Primary (navy glow) */
    QPushButton#primary {
        background-color: rgba(20, 20, 30, 180);
        border: 1px solid #5a8de0;
    }
    QPushButton#primary:hover {
        background-color: #173260;
        border: 1px solid #85b2ff;
    }

    /* Moss (confirm / action) */
    QPushButton#moss {
        background-color: #0f201b;
        border: 1px solid #2d6a54;
    }
    QPushButton#moss:hover {
        background-color: #122a22;
        border: 1px solid #3b8b6f;
    }

    /* Danger (dark red) */
    QPushButton#danger {
        background-color: #240d12;
        border: 1px solid #7b1f2c;
    }
    QPushButton#danger:hover {
        background-color: #311016;
        border: 1px solid #b02a3c;
    }

    /* =========================
       Inputs (terminal-ish)
       ========================= */
    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QComboBox {
        background-color: #08101f;
        border: 1px solid #243558;
        border-radius: 10px;
        padding: 8px 10px;
        color: #e7eefc;
        selection-background-color: #1b345a;
        selection-color: #ffffff;
    }

    QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QComboBox:focus {
        border: 1px solid #85b2ff;
    }

    /* =========================
       Tooltips / Popups
       ========================= */
    QToolTip {
        background-color: #0b1324;
        color: #e7eefc;
        border: 1px solid #2d6a54; /* moss outline */
        padding: 6px 8px;
        border-radius: 8px;
    }

    QMessageBox {
        background-color: #0b1324;
    }
    """)

    window = Menu()
    window.show()
    app.exec()

