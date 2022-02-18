 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import time
r=0
o=0
def s(d):
    global r
    r=r+d
    print(r)
    return r
def z(q):
    global o
    o=o+q
    print(o)
    return o
def win(k,l):
    if k>l:
        return 0
    if l>k: 
        return 1
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1130, 687)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(132, 90, 692, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.player = QtWidgets.QLabel(self.layoutWidget)
        self.player.setObjectName("player")
        self.gridLayout.addWidget(self.player, 5, 0, 1, 1)
        self.teamntered = QtWidgets.QLabel(self.layoutWidget)
        self.teamntered.setObjectName("teamntered")
        self.gridLayout.addWidget(self.teamntered, 5, 1, 1, 1)
        self.listplayer = QtWidgets.QListWidget(self.layoutWidget)
        self.listplayer.setObjectName("listplayer")
        self.gridLayout.addWidget(self.listplayer, 6, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 2, 2)
        self.ok2 = QtWidgets.QPushButton(self.layoutWidget)
        self.ok2.setObjectName("ok2")
        self.gridLayout.addWidget(self.ok2, 2, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 8, 2, 1)
        self.ok1 = QtWidgets.QPushButton(self.layoutWidget)
        self.ok1.setObjectName("ok1")
        self.gridLayout.addWidget(self.ok1, 2, 3, 2, 2)
        self.listpoints = QtWidgets.QListWidget(self.layoutWidget)
        self.listpoints.setObjectName("listpoints")
        self.gridLayout.addWidget(self.listpoints, 6, 7, 1, 2)
        self.win = QtWidgets.QPushButton(self.layoutWidget)
        self.win.setObjectName("win")
        self.gridLayout.addWidget(self.win, 7, 3, 1, 4)
        self.points = QtWidgets.QLabel(self.layoutWidget)
        self.points.setObjectName("points")
        self.gridLayout.addWidget(self.points, 5, 8, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 4, 7, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
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
            self.comboBox_2.addItem(u)
        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("pritam")
        self.i=0
        self.p=0
        

        self.retranslateUi(Form)
        self.win.clicked.connect(self.winclick)
        self.ok1.clicked.connect(self.ok1click)
        self.ok2.clicked.connect(self.ok2click)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def ok1click(self):
        try:
            self.listpoints.clear()
            self.listplayer.clear()
            self.msgBox.setText("use a different team")
            self.msgBox.exec()
            t=self.comboBox.currentText()
            print(t)
            myproject=sqlite3.connect("team.db")
            mycur=myproject.cursor()
            sql1="SELECT points FROM '"+t+"';"
            mycur.execute(sql1)
            for i in range(0,11):
                j=mycur.fetchone()
                print(type(j))
                print(j)
                v=''.join(map(str,j))
                print(v)
                self.listpoints.addItem(str(v))
            sql2="SELECT player FROM '"+t+"';"
            mycur.execute(sql2)
            for t in range(0,11):
                o=mycur.fetchone()
                print(o)
                h=''.join(map(str,o))
                self.listplayer.addItem(str(h))
            self.msgBox.setText("please press ok")
            self.msgBox.exec()
        except:
            self.msgBox.setText("no such team exist")
            self.msgBox.exec()
        m=self.comboBox.currentText()    
        sql2="SELECT sum(points) FROM '"+m+"';"
        myproject=sqlite3.connect("team.db")
        mycur=myproject.cursor()
        mycur.execute(sql2)
        u=mycur.fetchone()
        print(u)
        self.i=u
    def ok2click(self):
        try:
            self.listpoints.clear()
            self.listplayer.clear()
            o=self.comboBox_2.currentText()
            print(o)
            myproject=sqlite3.connect("team.db")
            mycur=myproject.cursor()
            sql1="SELECT points FROM '"+o+"';"
            mycur.execute(sql1)
            for i in range(0,11):
                j=mycur.fetchone()
                print(type(j))
                print(j)
                v=''.join(map(str,j))
                self.listpoints.addItem(str(v))
            sql2="SELECT player FROM '"+o+"';"
            mycur.execute(sql2)
            for t in range(0,11):
                z=mycur.fetchone()
                print(str(z))
                h=''.join(map(str,z))
                self.listplayer.addItem(str(h))
            self.msgBox.setText("please press ok")
            self.msgBox.exec()
        except:
            self.msgBox.setText("no such team exist")
            self.msgBox.exec()
        n=self.comboBox_2.currentText()    
        sql3="SELECT sum(points) FROM '"+n+"';"
        myproject=sqlite3.connect("team.db")
        mycur=myproject.cursor()
        mycur.execute(sql3)
        y=mycur.fetchone()
        print(y)
        self.p=y    
    def winclick(self):
        t=100
        count =0
        while count<t:
              count=count+1
              time.sleep(0)
              self.progressBar.setValue(count)
        self.msgBox.setText("and the winner is")
        self.msgBox.exec()
        m=self.comboBox.currentText()
        if self.i>self.p:
               self.msgBox.setText("win team1")
               self.msgBox.exec()
        if self.p>self.i:        
               self.msgBox.setText("win team2")
               self.msgBox.exec()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.player.setText(_translate("Form", "PLAYERS"))
        self.label.setText(_translate("Form", "ENTER TEAM2"))
        self.label_3.setText(_translate("Form", "ENTER TEAM1"))
        self.ok1.setText(_translate("Form", "OK"))
        self.teamntered.setText(_translate("Form", "TEAM"))
        self.points.setText(_translate("Form", "POINTS"))
        self.ok2.setText(_translate("Form", "   OK"))
        self.win.setText(_translate("Form", "press to see the winner"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
