from PyQt5 import QtCore, QtGui, QtWidgets

import JsonColors


class Ui_DialogW(object):
    def setupUi(self, DialogW):
        data = JsonColors.read_colors()
        fundal = "background-color: " + data["fundal"]

        DialogW.setObjectName("DialogW")
        DialogW.resize(407, 122)
        self.labelHelp = QtWidgets.QLabel(DialogW)
        self.labelHelp.setGeometry(QtCore.QRect(60, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)

        self.labelHelp.setFont(font)
        self.labelHelp.setObjectName("labelHelp")
        self.labelHelp.setStyleSheet(fundal)

        self.retranslateUi(DialogW)
        QtCore.QMetaObject.connectSlotsByName(DialogW)

    def retranslateUi(self, DialogW):
        _translate = QtCore.QCoreApplication.translate
        DialogW.setWindowTitle(_translate("DialogW", "ProjectDialog"))
        self.labelHelp.setText(_translate("DialogW", "Aplicație de cumpărat bilete de tren CFR"))
