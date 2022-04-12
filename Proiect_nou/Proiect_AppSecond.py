import sys
from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound

import JsonColors
import speech_text


class Ui_SecondApp(object):
    def __init__(self):
        self.menu_Exit = None
        self.menu_Help = None
        self.toolBar = None
        self.menuBack = None
        self.statusbar = None
        self.pushButton_Cumpara = None
        self.listView = None
        self.centralwidget = None

    def setupUi(self, SecondApp):
        data = JsonColors.read_colors()
        fundal = "background-color: " + data["fundal"]
        statusBar = "background-color: " + data["statusBar"]
        buttonManu = "background-color: " + data["lineEdit"]
        butonCumpara = "background-color: " + data["butonCauta"]

        SecondApp.setObjectName("SecondApp")
        SecondApp.setFixedSize(657, 575)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        SecondApp.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SecondApp)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(fundal)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 20, 611, 321))
        self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet(buttonManu)

        self.pushButton_Cumpara = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cumpara.setGeometry(QtCore.QRect(200, 390, 241, 81))
        self.pushButton_Cumpara.setObjectName("pushButton_Cumpara")
        SecondApp.setCentralWidget(self.centralwidget)
        self.pushButton_Cumpara.setStyleSheet(butonCumpara)
        self.pushButton_Cumpara.clicked.connect(self.threadFunction)

        self.statusbar = QtWidgets.QStatusBar(SecondApp)
        self.statusbar.setObjectName("statusbar")
        SecondApp.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet(statusBar)

        self.toolBar = QtWidgets.QToolBar(SecondApp)
        self.toolBar.setObjectName("toolBar")
        SecondApp.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.setStyleSheet(statusBar)

        self.actionBackW = QtWidgets.QAction(SecondApp)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackW.setIcon(icon)
        self.actionBackW.setObjectName("actionBackW")
        self.actionBackW.triggered.connect(self.threadFunction)
        self.actionBackW.triggered.connect(SecondApp.backWindow)

        self.actionHelpN = QtWidgets.QAction(SecondApp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelpN.setIcon(icon1)
        self.actionHelpN.setObjectName("actionHelpN")
        self.actionHelpN.triggered.connect(speech_text.threadFunctionSpeech)
        #self.actionHelpN.triggered.connect(self.threadFunction)
        #self.actionHelpN.triggered.connect(SecondApp.helpF)

        self.actionExitW = QtWidgets.QAction(SecondApp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/cross-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExitW.setIcon(icon2)
        self.actionExitW.setObjectName("actionExitW")
        self.actionExitW.triggered.connect(self.threadFunction)
        self.actionExitW.triggered.connect(SecondApp.exitWindow)

        self.toolBar.addAction(self.actionBackW)
        self.toolBar.addAction(self.actionHelpN)
        self.toolBar.addAction(self.actionExitW)

        self.retranslateUi(SecondApp)
        QtCore.QMetaObject.connectSlotsByName(SecondApp)

    def exitButtonClick(self):
        sys.exit(0)

    def threadFunction(self):
        thread = Thread(target=self.playSound)
        thread.start()

    def playSound(self):
        playsound('sounds/hero_simple-celebration-01.wav', block=False)

    def retranslateUi(self, SecondApp):
        _translate = QtCore.QCoreApplication.translate
        SecondApp.setWindowTitle(_translate("SecondApp", "Proiect"))
        self.pushButton_Cumpara.setText(_translate("SecondApp", "Cumpără"))
        self.toolBar.setWindowTitle(_translate("SecondApp", "toolBar"))
        self.actionBackW.setText(_translate("SecondApp", "BackW"))
        self.actionHelpN.setText(_translate("SecondApp", "HelpN"))
        self.actionExitW.setText(_translate("SecondApp", "ExitW"))

