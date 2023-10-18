import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class WordsManager (qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("words manager"))
        self.words=[]
        self.word=qt.QListWidget()
        self.word.setAccessibleName(_("words"))
        self.add=qt.QPushButton(_("add"))
        self.add.clicked.connect(self.oadd)
        self.delete=qt.QPushButton(_("delete"))
        self.delete.clicked.connect(self.odelete)
        self.delete.setShortcut("delete")
        layout=qt.QVBoxLayout()
        layout.addWidget(self.word)
        layout.addWidget(self.add)
        layout.addWidget(self.delete)
        self.setLayout(layout)
        with open("data/words/words.lalw","r",encoding="utf-8") as f:
            f1=f.read().split("\n")
            self.words=f1
            self.word.addItems(f1)
    def oadd(self):
        t,OK=qt.QInputDialog.getText(self,_("main word"),_("type"))
        if OK:
            t1,OK=qt.QInputDialog.getText(self,_("translated word"),_("type"))
            if OK:
                w=t + '":"' + t1
                self.word.addItem(w)
                self.words.append(w)
        self.save()
    def odelete(self):
        c=self.word.currentItem().text()
        self.words.remove(c)
        self.word.clear()
        self.word.addItems(self.words)
        qt.QMessageBox.warning(self,_("done"),_("word deleted"))
        self.save()
    def save(self):
        with open("data/words/words.lalw","w",encoding="utf-8") as f:
            f.write("\n".join(self.words))