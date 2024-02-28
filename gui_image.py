import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout
 
 
class GuiImage(QWidget):
    def __init__(self):
        super().__init__()
 
        labelTexto = QLabel("Vou capturar o avatar!")
        labelImagem = QLabel("")
        labelImagem.setPixmap(QPixmap("Zukinho2.jpg"))
 
        layout = QHBoxLayout()
        layout.addWidget(labelTexto)
        layout.addWidget(labelImagem)
       
        self.setGeometry(100,100,500,600)
 
        self.setWindowTitle("Imagem em label")
 
        self.setLayout(layout)
 
app = QApplication(sys.argv)
tela = GuiImage()
tela.show()
app.exec_()