import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QTimer
class JarvisWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.radius = 50
        self.state = "sleeping"
        self.growing = True

        self.timer = QTimer()

        self.timer.timeout.connect(self.animate)

        self.timer.start(30)

        
        

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.showFullScreen()
    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        center_x = self.width() // 2
        center_y = self.height() // 2

        if self.state == "sleeping":

            color = QColor(30, 60, 120, 150)

        elif self.state == "listening":

            color = QColor(0, 200, 255, 220)

        elif self.state == "thinking":

            color = QColor(255, 170, 0, 220)

        elif self.state == "speaking":

            color = QColor(0, 255, 120, 220)

        else:

            color = QColor(0, 150, 255, 180)

        painter.setBrush(color)

        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
        center_x - self.radius,
        center_y - self.radius,
        self.radius * 2,
        self.radius * 2
    )
    

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:

            self.close()
    def set_state(self, state):

        self.state = state

        self.update()
    def animate(self):

        if self.growing:

            self.radius += 1

            if self.radius >= 70:

                self.growing = False

        else:

            self.radius -= 1

            if self.radius <= 50:

                self.growing = True

        self.update()
    def wake_up(self):

        self.show()

        self.set_state("listening")


    def go_to_sleep(self):

        self.hide()


