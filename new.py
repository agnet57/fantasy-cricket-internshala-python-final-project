# -*- coding: utf-8 -*-

# Form1 implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(1164, 724)
        self.widget = QtWidgets.QWidget(Form1)
        self.widget.setGeometry(QtCore.QRect(310, 220, 541, 301))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QLabel(self.widget)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.add = QtWidgets.QPushButton(self.widget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 1, 0, 1, 2)
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 2, 0, 1, 2)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("warning")

        self.retranslateUi(Form1)
        self.add.clicked.connect(self.addclick)
        self.cancel.clicked.connect(self.cancelclick)
        QtCore.QMetaObject.connectSlotsByName(Form1)
    def addclick(self):
        try:  
            txt=self.lineEdit.text()
            myproject=sqlite3.connect("team.db")
            mycur=myproject.cursor() 
            mycur.execute("CREATE TABLE IF NOT EXISTS '"+txt+"' (points INTEGER NOT NULL , player TEXT(50));")
            self.msgBox.setText("team added successfully")
            self.msgBox.exec()
            self.msgBox.setText("type the same name in team name box to save your team")
            self.msgBox.exec()
        except:
            self.msgBox.setText("try again!")
            self.msgBox.exec()
    def cancelclick(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form1 = QtWidgets.QWidget()
        ui = Ui_Form1()
        ui.setupUi(Form1)
        Form1.show()
    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "NEW"))
        self.add.setText(_translate("Form1", "ADD"))
        self.cancel.setText(_translate("Form1", "CANCEL"))
        self.text.setText(_translate("Form1", "TEAM NAME"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())
