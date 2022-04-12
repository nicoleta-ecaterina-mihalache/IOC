from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
import sys

import Dialog
import Proiect
import Proiect_AppSecond


class ExampleApp(QtWidgets.QMainWindow, Proiect.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.myDialog = None
        self.setupUi(self)

    def executeDialog(self):
        self.hide()
        self.myDialog = ExampleApp2()
        self.myDialog.show()
        self.close()

    def helpF(self):
        self.hide()
        self.myDialog = ExampleDialog()
        self.myDialog.show()
        self.close()


class ExampleApp2(QtWidgets.QMainWindow, Proiect_AppSecond.Ui_SecondApp):
    def __init__(self, parent=None):
        super(ExampleApp2, self).__init__(parent)
        self.myDialog = None
        self.myWindow = None
        self.setupUi(self)

    def backWindow(self):
        self.hide()
        self.myWindow = ExampleApp()
        self.myWindow.show()
        self.close()

    def helpF(self):
        self.hide()
        self.myDialog = ExampleDialog()
        self.myDialog.show()
        self.close()

    def exitWindow(self):
        sys.exit(0)

class ExampleDialog(QtWidgets.QDialog, Dialog.Ui_DialogW):
    def __init__(self, parent=None):
        super(ExampleDialog, self).__init__(parent)
        self.myDialog = None
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()