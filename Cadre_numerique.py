import sys
import random
from PySide6 import *
from Cadre_numerique_class import *

# Ouverture de la fenêtre
print(QtCore.__version__)
# fen = Full_screen_window()
# fen.app.exec()

app = QtWidgets.QApplication([])

img = ImageViewer()
img.load_file("aa.jpg")
img._fit_to_window()
img.show()

sys.exit(app.exec())