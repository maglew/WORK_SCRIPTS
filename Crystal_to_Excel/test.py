from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic, QtWidgets
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("gui.ui", self)

        # find the widgets in the xml file

        #self.textedit = self.findChild(QTextEdit, "textEdit")
        #self.button = self.findChild(QPushButton, "pushButton")
        #self.button.clicked.connect(self.clickedBtn)

        self.show()

    #def clickedBtn(self):
       # self.textEdit.setPlainText("Please subscribe the channnel and like the videos")


#app = QApplication(sys.argv)
#window = UI()
#app.exec_()

app = QtWidgets.QApplication([])
window = UI()
sys.exit(app.exec())

'''
#from PyQt5 import QtWidgets, uic
#import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("gui.ui")  # расположение вашего файла .ui

win.show()
sys.exit(app.exec())'''
