
from PyQt5 import QtCore, QtGui, QtWidgets
from sayfa3 import Ui_ihackyou3



class Ui_ihackyou2( QtWidgets.QMainWindow ):
    def __init__(self): #*****
        super().__init__() #*****

        #self.ana_sayfa = ana_sayfa

        self.setupUi() #*****    


    def sayfalargec(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ihackyou3()
        self.ui.show()
        self.close()



    def setupUi(self):
        self.setObjectName("ihackyou")
        self.resize(341, 195)
        self.setWindowTitle(" I LOVE YOU")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(100, 40, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setMouseTracking(False)
        self.text1.setObjectName("text1")
        self.backgr = QtWidgets.QLabel(self.centralwidget)
        self.backgr.setGeometry(QtCore.QRect(-4, 140, 361, 71))
        self.backgr.setStyleSheet("background-color:rgb(216, 216, 216)")
        self.backgr.setText("")
        self.backgr.setObjectName("backgr")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(234, 150, 91, 31))
        self.ok.setStyleSheet("border: 1px solid #3A3939;")
        self.ok.setObjectName("ok")
        self.warningicon = QtWidgets.QLabel(self.centralwidget)
        self.warningicon.setGeometry(QtCore.QRect(20, 40, 61, 61))
        self.warningicon.setText("")
        self.warningicon.setPixmap(QtGui.QPixmap("./image/war.png"))
        self.warningicon.setScaledContents(True)
        self.warningicon.setObjectName("warningicon")
        self.setCentralWidget(self.centralwidget)


        self.ok.clicked.connect(self.sayfalargec)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.text1.setText(_translate("ihackyou", "Neyse, senin için bir sorum var ?"))
        self.ok.setText(_translate("ihackyou", "Tamam"))
