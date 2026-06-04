import sys
import threading

from PyQt6.QtWidgets import QApplication

from gui.jarvis_window import JarvisWindow
from gui.gui_manager import set_window

from wake_mode import start_wake_mode


app = QApplication(sys.argv)

window = JarvisWindow()

set_window(window)

window.show()


threading.Thread(
    target=start_wake_mode,
    daemon=True
).start()


sys.exit(app.exec())