# -*- coding: utf-8 -*-

# Form2 implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(1129, 678)
        self.layoutWidget = QtWidgets.QWidget(Form2)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 70, 849, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.player = QtWidgets.QLabel(self.layoutWidget)
        self.player.setObjectName("player")
        self.gridLayout.addWidget(self.player, 1, 0, 1, 1)
        self.points = QtWidgets.QLabel(self.layoutWidget)
        self.points.setObjectName("points")
        self.gridLayout.addWidget(self.points, 1, 5, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 4, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        k=sqlite3.connect("team.db")
        my=k.cursor()
        sql1="SELECT team FROM teams;"
        j=my.execute(sql1)
        o=my.fetchall()
        l=len(o)
        u=[]
        for i in range(0,l):
            u=''.join(map(str,o[i]))
            print(u)
            self.comboBox.addItem(u)
        self.selectteam = QtWidgets.QLabel(self.layoutWidget)
        self.selectteam.setObjectName("selectteam")
        self.gridLayout.addWidget(self.selectteam, 1, 1, 1, 1)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("warning!")

        self.retranslateUi(Form2)
        self.pushButton.clicked.connect(self.pushButtonclick)
        self.progressBar.valueChanged['int'].connect(self.progressBar.setMaximum)
        QtCore.QMetaObject.connectSlotsByName(Form2)
    def pushButtonclick(self):
        try:
            self.listWidget.clear()
            self.listWidget_2.clear()
            txt1=self.comboBox.currentText()
            myproject=sqlite3.connect("team.db")
            mycur=myproject.cursor()
            #player widget
            sql="SELECT player FROM '"+txt1+"';"
            mycur.execute(sql)
            for i in range(0,11):
                j=mycur.fetchone()
                l=' '.join(map(str,j))
                print(l)
                self.listWidget.addItem(str(l))
            #points widget    
            sql1="SELECT points FROM '"+txt1+"';"
            mycur.execute(sql1)
            for k in range(0,11):
                o=mycur.fetchone()
                print(o)
                u=int(' '.join(map(str,o)))
                print(u)      
                self.listWidget_2.addItem(str(u))
                self.progressBar.setValue(100)
        except:
            self.msgBox.setText("no such team exist")
            self.msgBox.exec()

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "OPEN"))
        self.label.setText(_translate("Form2", "TEAM NAME"))
        self.player.setText(_translate("Form2", "PLAYER"))
        self.points.setText(_translate("Form2", "POINT"))
        self.pushButton.setText(_translate("Form2", "OPEN"))
        self.selectteam.setText(_translate("Form2", "SELECT TEAM"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form2 = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form2)
    Form2.show()
    sys.exit(app.exec_())
