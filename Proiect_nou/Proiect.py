import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import JsonColors
from playsound import playsound
from threading import Thread
import speech_text
import speech_recognition as sr
import pyttsx3


class Ui_MainWindow(object):
    def __init__(self):
        self.actionExit = None
        self.actionHelp = None
        self.menu_File = None
        self.comboBoxServicii = None
        self.labelConexiuni = None
        self.labelServicii = None
        self.comboBoxConexiuni = None
        self.toolBar = None
        self.menu_Exit = None
        self.menuBar = None
        self.menu_Help = None
        self.line_statieEnd = None
        self.line_statieStart = None
        self.label_data = None
        self.date_dataPlecare = None
        self.pushButton = None
        self.label_statiesosire = None
        self.label_statieplecare = None
        self.groupBox = None
        self.centralwidget = None
        self.statusbar = None

    def setupUi(self, MainWindow):
        data = JsonColors.read_colors()
        fundal = "background-color: " + data["fundal"]
        butonCauta = "background-color: " + data["butonCauta"]
        fundalBox = "background-color: " + data["fundalBox"]
        lineEdit = "background-color: " + data["lineEdit"]
        statusBar = "background-color: " + data["statusBar"]

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(657, 575)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(fundal)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 611, 361))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet(fundalBox)

        self.label_statieplecare = QtWidgets.QLabel(self.groupBox)
        self.label_statieplecare.setGeometry(QtCore.QRect(90, 40, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setUnderline(False)
        self.label_statieplecare.setFont(font)
        self.label_statieplecare.setObjectName("label_statieplecare")

        self.label_statiesosire = QtWidgets.QLabel(self.groupBox)
        self.label_statiesosire.setGeometry(QtCore.QRect(120, 120, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_statiesosire.setFont(font)
        self.label_statiesosire.setObjectName("label_statiesosire")

        self.label_data = QtWidgets.QLabel(self.groupBox)
        self.label_data.setGeometry(QtCore.QRect(100, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_data.setFont(font)
        self.label_data.setObjectName("label_data")

        self.line_statieStart = QtWidgets.QLineEdit(self.groupBox)
        self.line_statieStart.setGeometry(QtCore.QRect(50, 80, 211, 20))
        self.line_statieStart.setObjectName("line_statieStart")
        self.line_statieStart.setStyleSheet(lineEdit)

        self.line_statieEnd = QtWidgets.QLineEdit(self.groupBox)
        self.line_statieEnd.setGeometry(QtCore.QRect(50, 160, 211, 20))
        self.line_statieEnd.setObjectName("line_statieEnd")
        self.line_statieEnd.setStyleSheet(lineEdit)

        self.date_dataPlecare = QtWidgets.QDateEdit(self.groupBox)
        self.date_dataPlecare.setGeometry(QtCore.QRect(50, 250, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.date_dataPlecare.setFont(font)
        self.date_dataPlecare.setAlignment(QtCore.Qt.AlignCenter)
        self.date_dataPlecare.setCurrentSection(QtWidgets.QDateTimeEdit.MonthSection)
        self.date_dataPlecare.setCalendarPopup(True)
        self.date_dataPlecare.setObjectName("date_dataPlecare")
        self.date_dataPlecare.setStyleSheet(lineEdit)

        self.labelServicii = QtWidgets.QLabel(self.groupBox)
        self.labelServicii.setGeometry(QtCore.QRect(420, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelServicii.setFont(font)
        self.labelServicii.setObjectName("labelServicii")

        self.labelConexiuni = QtWidgets.QLabel(self.groupBox)
        self.labelConexiuni.setGeometry(QtCore.QRect(410, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.labelConexiuni.setFont(font)
        self.labelConexiuni.setObjectName("labelConexiuni")

        self.comboBoxServicii = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxServicii.setGeometry(QtCore.QRect(350, 110, 211, 22))
        self.comboBoxServicii.setObjectName("comboBoxServicii")
        self.comboBoxServicii.setStyleSheet(lineEdit)

        self.comboBoxConexiuni = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxConexiuni.setGeometry(QtCore.QRect(350, 210, 211, 22))
        self.comboBoxConexiuni.setObjectName("comboBoxConexiuni")
        self.comboBoxConexiuni.setStyleSheet(lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 420, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(butonCauta)
        self.pushButton.clicked.connect(self.threadFunction)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setStyleSheet(statusBar)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.setStyleSheet(statusBar)

        self.actionHelpN = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelpN.setIcon(icon1)
        self.actionHelpN.setObjectName("actionHelpN")
        #self.actionHelpN.triggered.connect(self.threadFunction)
        #self.actionHelpN.triggered.connect(MainWindow.helpF)
        self.actionHelpN.triggered.connect(speech_text.threadFunctionSpeech)

        self.actionExitW = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/cross-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExitW.setIcon(icon2)
        self.actionExitW.setObjectName("actionExitW")
        self.actionExitW.triggered.connect(self.threadFunction)
        self.actionExitW.triggered.connect(self.exitButtonClick)

        self.toolBar.addAction(self.actionHelpN)
        self.toolBar.addAction(self.actionExitW)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.executeDialog)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exitButtonClick(self):
        sys.exit(0)

    def threadFunction(self):
        thread = Thread(target=self.playSound)
        thread.start()

    def playSound(self):
        playsound('sounds/hero_simple-celebration-01.wav', block=False)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proiect"))
        self.label_statieplecare.setText(_translate("MainWindow", "Stația de plecare"))
        self.label_statiesosire.setText(_translate("MainWindow", "Până la"))
        self.label_data.setText(_translate("MainWindow", "Data plecării"))
        self.date_dataPlecare.setDisplayFormat(_translate("MainWindow", "M/d/yyyy"))
        self.labelServicii.setText(_translate("MainWindow", "Servicii"))
        self.labelConexiuni.setText(_translate("MainWindow", "Conexiuni"))
        self.pushButton.setText(_translate("MainWindow", "Caută"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionHelpN.setText(_translate("SecondApp", "HelpN"))
        self.actionExitW.setText(_translate("SecondApp", "ExitW"))
