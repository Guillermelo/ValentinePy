from PySide6.QtCore import QSize, Qt, QPoint, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QStackedWidget
from PySide6.QtGui import QPixmap, QMovie
import os
from UI.SoundFx import SoundFx

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")

class LoveStoryPage(QWidget):
    def __init__(self, go_next_page):
        super().__init__()
        self.go_next_page = go_next_page
        self.sfx = SoundFx()
        self.current_image = 0
        self.current_dialog_index = 0

        self.images = [
            os.path.join(ASSETS_DIR, "1_seven_eleven.png"),
            os.path.join(ASSETS_DIR, "2_HK_BUS.png"),
            os.path.join(ASSETS_DIR, "3_SG_merlion.png"),
            os.path.join(ASSETS_DIR, "sunset_love_letter.png"),
            os.path.join(ASSETS_DIR, "5_TWN_chiangkaishek.png"),
            os.path.join(ASSETS_DIR, "6_AIRPORT.png"),
            os.path.join(ASSETS_DIR, "finale.png")
        ]

        self.dialog_map = [
            [" Holaa Usuario de la Aplicacion For Lisa"," Soy un robot que guillermo instalo 🤖", " para poder contar esta bonita historia de amor", " pasion ", " y locura."," Esta Historia comienza asi..."," Todo comenzo un dia",""],
            [" dos chicuelos se gustaban", "mucho mucho", " (el se gustaba un poco tooo much...)"," he was willing to do crazy stuff ngl ", ""],
            [" viajaron juntos pq se dieron cuenta de que habia algo", " y lo sentian muy fuerte en el corazon"," MUCHAS COSAS SENTIAN" ,""],
            [" Una tarde mirando el mar en Tamsui"," Cayendo en cuenta que se amaban", " mucho mucho"," caminaron por las calles taiwanesas",""],
            [" y cuando todos los secretos fueron revelados...", " mirandose frente a frente", " decidieron estar juntoss", " apesar de cualquier dificultad",""],
            [" sabiendo que eventualmente se van a ver de nuevo", " una", " y otra", " y mil veces mas",""],
            [" Por el mundo entero", " con todo", " te amo ", " te gusto tu regalo?", " mas vale..."," Fin de la Historia", " ..." ," Seguis ahi?"," ya podes parar", " No estoy entrenado para dar otros servicios", " a partir de aca ya no vas a encontrar nada"
             ," O SI????", " es broma no vas a encontrar nada", " ...", " esta aplicacion se autodestruira en"," 3"," 2"," 1", " BOOOOOOOOM 💥", " ...", " Cha..."," no te espanto eso", " bueno menos mal no huiste", " por que me olvide de mostrarte este mensaje de Guille: ",
             " te amo un monton amor", " y quiero amarte siempre", " pasemosla bien en Portugal", "y dame muchos besos", " bueno ahora si termino"," O NO??"," QUE QUERES QUE HAGA QUE??", " QUERES QUE TE CUENTE LA HISTORIA OTRA VEZ?", "Alguien se tiene que encargar de mi mantenimiento 😭" ," bueno ahi voy...", " ehem ehem..." ]
        ]

        self.scene = QLabel(self)
        self.scene.setGeometry(30, 30, 630, 630)
        self.scene.setPixmap(QPixmap(self.images[0]))
        self.scene.setScaledContents(True)

        self.text_label = QLabel(self)
        self.text_label.setGeometry(50, 600, 600, 40)
        self.text_label.setWordWrap(True)
        self.text_label.setStyleSheet("""
        QLabel {
            background-color: rgba(20, 20, 30, 180);
            color: #F2F4FF;
            padding: 10px 16px;
            border-radius: 12px;
            font-size: 16px;
        }
        """)

        self.next_scene_button = QPushButton("Next", self)
        self.next_scene_button.setGeometry(450, 650, 70, 35)
        self.next_scene_button.clicked.connect(self.change_scene)

        self.home_button = QPushButton("Home", self)
        self.home_button.setGeometry(300, 650, 70, 35)
        self.home_button.clicked.connect(self.sfx.play_click)
        self.home_button.clicked.connect(self.home_button_was_clicked)

        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self._typewriter_tick)

        self.is_typing = False
        self.full_text_to_type = ""
        self.type_index = 0
        self.type_speed_ms = 20
        self.pause_punct_ms = 120

    def home_button_was_clicked(self):
        QTimer.singleShot(1, lambda: self.go_next_page(1))

    def play_dialog_animated(self, text):
        self.typing_timer.stop()
        self.is_typing = True
        self.full_text_to_type = text
        self.type_index = 0
        self.text_label.setText("")
        self.typing_timer.start(self.type_speed_ms)

    def finish_typing_instant(self):
        if not self.is_typing:
            return
        self.typing_timer.stop()
        self.is_typing = False
        self.text_label.setText(self.full_text_to_type)

    def _typewriter_tick(self):
        if self.type_index > len(self.full_text_to_type):
            self.typing_timer.stop()
            self.is_typing = False
            return

        current = self.full_text_to_type[:self.type_index]
        self.text_label.setText(current)


        if self.type_index > 0:
            last_char = self.full_text_to_type[self.type_index - 1]
            if last_char in [".", ",", "!", "?", ";", ":"]:
                self.typing_timer.setInterval(self.pause_punct_ms)
            else:
                self.typing_timer.setInterval(self.type_speed_ms)

        self.type_index += 1

        # Opcional: sonidito por letra (si tenés uno muy suave)
        # Ojo: si suena muy rápido puede molestar. Mejor solo cada 2-3 chars.
        if self.type_index % 3 == 0:
            self.sfx.play_type()

    # ---------------- SCENE / DIALOG FLOW ----------------
    def change_scene(self):
        if self.is_typing:
            self.finish_typing_instant()
            return

        dialogs = self.dialog_map[self.current_image]

        text = dialogs[self.current_dialog_index]
        self.play_dialog_animated(text)


        if self.current_dialog_index == len(dialogs) - 1:

            self.current_image = (self.current_image + 1) % len(self.images)
            self.scene.setPixmap(QPixmap(self.images[self.current_image]))
            self.current_dialog_index = 0
        else:
            self.current_dialog_index += 1

    def on_enter(self):
        self.current_image = 0
        self.current_dialog_index = 0
        self.scene.setPixmap(QPixmap(self.images[0]))


        # self.play_dialog_animated(self.dialog_map[0][0])

    def on_leave(self):
        self.typing_timer.stop()
        self.is_typing = False
        print("on_leave")
