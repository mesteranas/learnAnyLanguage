import sys
from custome_errors import *
sys.excepthook = my_excepthook
import random
import gui
import guiTools
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.start=qt.QPushButton(_("starrt test"))
        self.start.setDefault(True)
        self.start.clicked.connect(self.ostart)
        layout.addWidget(self.start)
        self.wstoar=qt.QPushButton(_("words manager"))
        self.wstoar.setDefault(True)
        self.wstoar.clicked.connect(lambda:gui.WordsManager(self).exec())
        layout.addWidget(self.wstoar)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def ostart(self):
        count,OK=qt.QInputDialog.getInt(self,_("select questions count"),_("type count"),10,5,1000000,1)
        if OK:
            TU=0
            AU=0
            while AU<count:
                with open("data/words/words.lalw","r",encoding="utf-8") as file:
                    wa=random.choice(file.read().split("\n")).split('":"')
                w,OK=qt.QInputDialog.getText(self,_("type word"),wa[0])
                if OK:
                    if w.lower()==wa[1].lower():
                        TU+=1
                    AU+=1
                else:
                    break
            qt.QMessageBox.information(self,_("test result"),_("your mark is {} from {}".format(str(TU),str(AU))))
App=qt.QApplication([])
w=main()
w.show()
App.exec()