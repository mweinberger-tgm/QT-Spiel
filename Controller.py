import View
import Model
import sys
from PySide.QtCore import *
from PySide.QtGui import *

__author__ = 'Michael Weinberger'
__date__ = 20151220
__version__ = 1.0


class Controller(QWidget):

    """
        Erstellt das Spiel, verbindet die einzelnen Komponenten miteinander
    """
    def __init__(self, parent=None):

        super().__init__(parent)

        self.lastval = 0

        self.Dialog = View.Ui_Dialog()
        self.Dialog.setupUi(self)
        self.Buttons = [
            self.Dialog.pushButton_1,
            self.Dialog.pushButton_2,
            self.Dialog.pushButton_3,
            self.Dialog.pushButton_4,
            self.Dialog.pushButton_5,
            self.Dialog.pushButton_6,
            self.Dialog.pushButton_7,
            self.Dialog.pushButton_8,
            self.Dialog.pushButton_9,
            self.Dialog.pushButton_10,
            self.Dialog.pushButton_11,
            self.Dialog.pushButton_12,
            self.Dialog.pushButton_13,
            self.Dialog.pushButton_14,
            self.Dialog.pushButton_15
        ]

        counter = 1
        for button in self.Buttons:
            button.setText(str(counter))
            button.setEnabled(True)
            counter += 1

        self.Model = Model.Model()

        self.Dialog.neu.clicked.connect(self.new)
        self.Dialog.close.clicked.connect(self.kill)

        self.new()

        self.Dialog.label_10.setText(str(self.Model.games))
        self.Dialog.label_6.setText(str(self.Model.pending))
        self.Dialog.label_7.setText(str(self.Model.true))
        self.Dialog.label_8.setText(str(self.Model.false))
        self.Dialog.label_9.setText(str(self.Model.total))

        #Unschön, ja :) Aber rennt
        self.Dialog.pushButton_1.clicked.connect(lambda: self.action(self.Dialog.pushButton_1))
        self.Dialog.pushButton_2.clicked.connect(lambda: self.action(self.Dialog.pushButton_2))
        self.Dialog.pushButton_3.clicked.connect(lambda: self.action(self.Dialog.pushButton_3))
        self.Dialog.pushButton_4.clicked.connect(lambda: self.action(self.Dialog.pushButton_4))
        self.Dialog.pushButton_5.clicked.connect(lambda: self.action(self.Dialog.pushButton_5))
        self.Dialog.pushButton_6.clicked.connect(lambda: self.action(self.Dialog.pushButton_6))
        self.Dialog.pushButton_7.clicked.connect(lambda: self.action(self.Dialog.pushButton_7))
        self.Dialog.pushButton_8.clicked.connect(lambda: self.action(self.Dialog.pushButton_8))
        self.Dialog.pushButton_9.clicked.connect(lambda: self.action(self.Dialog.pushButton_9))
        self.Dialog.pushButton_10.clicked.connect(lambda: self.action(self.Dialog.pushButton_10))
        self.Dialog.pushButton_11.clicked.connect(lambda: self.action(self.Dialog.pushButton_11))
        self.Dialog.pushButton_12.clicked.connect(lambda: self.action(self.Dialog.pushButton_12))
        self.Dialog.pushButton_13.clicked.connect(lambda: self.action(self.Dialog.pushButton_13))
        self.Dialog.pushButton_14.clicked.connect(lambda: self.action(self.Dialog.pushButton_14))
        self.Dialog.pushButton_15.clicked.connect(lambda: self.action(self.Dialog.pushButton_15))

    """
        Beendet das Programm sauber
    """
    def kill(self):
        QCoreApplication.instance().quit()

    """
        Setzt die Werte zurück
    """
    def new(self):

        self.Model.newgame()

    """
        Definiert was passiert, wenn ein Button gedrückt ist.

        Bei 0 verbleibenden Zahlen wird eine Gratulation ausgesprochen und das
        Spiel neu gestartet
    """
    def action(self, button):

        if int(button.text()) == self.lastval+1:

            self.Model.success()
            self.lastval += 1

            self.Dialog.label_6.setText(str(self.Model.pending))
            self.Dialog.label_7.setText(str(self.Model.true))
            self.Dialog.label_9.setText(str(self.Model.total))

        else:

            self.Model.fail()
            self.Dialog.label_9.setText(str(self.Model.total))
            self.Dialog.label_8.setText(str(self.Model.false))

        if self.Model.pending == 0:
            QMessageBox.about(self, "WOW! SUPER! GRATULIERE!", "Du kannst bis 15 zählen ... :)")
            self.lastval = 0
            self.new()

"""
    Starten des Programms
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = Controller()
    main_window.show()
    sys.exit(app.exec_())
