
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from new import Ui_Form1
from open import Ui_Form2
from evaluate import Ui_Form
m=0
def f(s,t):
    global m
    if t==1:
        m=m+s
        return m
    if t==0:
        m=m-s
        return m
class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1037, 909)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(70, 20, 631, 51))
        self.welcome.setObjectName("welcome")
        self.SELCTION = QtWidgets.QLabel(self.centralwidget)
        self.SELCTION.setGeometry(QtCore.QRect(60, 90, 101, 51))
        self.SELCTION.setFrameShape(QtWidgets.QFrame.Box)
        self.SELCTION.setTextFormat(QtCore.Qt.PlainText)
        self.SELCTION.setObjectName("SELCTION")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 150, 871, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.allrounderlabel = QtWidgets.QLabel(self.layoutWidget)
        self.allrounderlabel.setObjectName("allrounderlabel")
        self.gridLayout.addWidget(self.allrounderlabel, 0, 5, 1, 1)
        self.bowler = QtWidgets.QLabel(self.layoutWidget)
        self.bowler.setObjectName("bowler")
        self.gridLayout.addWidget(self.bowler, 0, 2, 1, 1)
        self.wicketkeeper = QtWidgets.QLabel(self.layoutWidget)
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.gridLayout.addWidget(self.wicketkeeper, 0, 7, 1, 1)
        self.bowlerlabel = QtWidgets.QLabel(self.layoutWidget)
        self.bowlerlabel.setObjectName("bowlerlabel")
        self.gridLayout.addWidget(self.bowlerlabel, 0, 3, 1, 1)
        self.allrounder = QtWidgets.QLabel(self.layoutWidget)
        self.allrounder.setObjectName("allrounder")
        self.gridLayout.addWidget(self.allrounder, 0, 4, 1, 1)
        self.batsmanlable = QtWidgets.QLabel(self.layoutWidget)
        self.batsmanlable.setObjectName("batsmanlable")
        self.gridLayout.addWidget(self.batsmanlable, 0, 1, 1, 1)
        self.batsman = QtWidgets.QLabel(self.layoutWidget)
        self.batsman.setObjectName("batsman")
        self.gridLayout.addWidget(self.batsman, 0, 0, 1, 1)
        self.pavailable = QtWidgets.QLabel(self.layoutWidget)
        self.pavailable.setObjectName("pavailable")
        self.gridLayout.addWidget(self.pavailable, 3, 0, 1, 1)
        self.wicketkplabel = QtWidgets.QLabel(self.layoutWidget)
        self.wicketkplabel.setObjectName("wicketkplabel")
        self.gridLayout.addWidget(self.wicketkplabel, 0, 8, 1, 1)
        self.pused = QtWidgets.QLabel(self.layoutWidget)
        self.pused.setObjectName("pused")
        self.gridLayout.addWidget(self.pused, 3, 6, 1, 1)
        self.pavailablelabel = QtWidgets.QLabel(self.layoutWidget)
        self.pavailablelabel.setObjectName("pavailablelabel")
        self.gridLayout.addWidget(self.pavailablelabel, 3, 1, 1, 1)
        self.pusedlabel = QtWidgets.QLabel(self.layoutWidget)
        self.pusedlabel.setObjectName("pusedlabel")
        self.gridLayout.addWidget(self.pusedlabel, 3, 7, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 310, 881, 56))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bat = QtWidgets.QRadioButton(self.layoutWidget1)
        self.bat.setObjectName("bat")
        self.gridLayout_2.addWidget(self.bat, 0, 0, 1, 1)
        self.wicketkeeper_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.wicketkeeper_2.setObjectName("wicketkeeper_2")
        self.gridLayout_2.addWidget(self.wicketkeeper_2, 0, 3, 1, 1)
        self.allrounder_2 = QtWidgets.QRadioButton(self.layoutWidget1)
        self.allrounder_2.setObjectName("allrounder_2")
        self.gridLayout_2.addWidget(self.allrounder_2, 0, 5, 1, 1)
        self.bowl = QtWidgets.QRadioButton(self.layoutWidget1)
        self.bowl.setObjectName("bowl")
        self.gridLayout_2.addWidget(self.bowl, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 7, 1, 1)
        self.teamname = QtWidgets.QLabel(self.layoutWidget1)
        self.teamname.setObjectName("teamname")
        self.gridLayout_2.addWidget(self.teamname, 0, 6, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 370, 881, 471))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.list2 = QtWidgets.QListWidget(self.layoutWidget2)
        self.list2.setObjectName("list2")
        self.gridLayout_3.addWidget(self.list2, 1, 2, 1, 1)
        self.list1 = QtWidgets.QListWidget(self.layoutWidget2)
        self.list1.setObjectName("list1")
        self.gridLayout_3.addWidget(self.list1, 1, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.layoutWidget2)
        self.exit.setObjectName("exit")
        self.gridLayout_3.addWidget(self.exit, 2, 1, 1, 1)
        self.labeltodislpay = QtWidgets.QLabel(self.layoutWidget2)
        self.labeltodislpay.setText("please enter the team name in save team")
        self.labeltodislpay.setObjectName("labeltodislpay")
        self.gridLayout_3.addWidget(self.labeltodislpay, 0, 2, 1, 1)
        self.teamnamelabel = QtWidgets.QLabel(self.layoutWidget2)
        self.teamnamelabel.setObjectName("teamnamelabel")
        self.gridLayout_3.addWidget(self.teamnamelabel, 0, 1, 1, 1)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 22))
        self.menubar.setObjectName("menubar")
        self.menumanage_teams = QtWidgets.QMenu(self.menubar)
        self.menumanage_teams.setObjectName("menumanage_teams")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        #new team
        self.actionnew_team = QtWidgets.QAction(main)
        self.actionnew_team.setObjectName("actionnew_team")
        #save team
        self.actionsave_team = QtWidgets.QAction(main)
        self.actionsave_team.setObjectName("actionsave_team")
        #evaluate team
        self.actionevaluate = QtWidgets.QAction(main)
        self.actionevaluate.setObjectName("actionevaluate")
        #open team
        self.actionopen = QtWidgets.QAction(main)
        self.actionopen.setObjectName("actionopen")
        #menu manage new
        self.menumanage_teams.addAction(self.actionnew_team)
        self.actionnew_team.setShortcut("ctrl+N")
        self.actionnew_team.triggered.connect(self.file_new)
        #menu mnage open
        self.menumanage_teams.addAction(self.actionopen)
        self.actionopen.setShortcut("ctrl+o")
        self.actionopen.triggered.connect(self.file_open)
        #menu save team
        self.menumanage_teams.addAction(self.actionsave_team)
        self.actionsave_team.setShortcut("ctrl+s")
        self.actionsave_team.triggered.connect(self.file_save)
        #menu evaluate
        self.actionevaluate.setShortcut("ctrl+e")
        self.actionevaluate.triggered.connect(self.file_evaluate)
        self.menumanage_teams.addAction(self.actionevaluate)

        self.menubar.addAction(self.menumanage_teams.menuAction())

        self.retranslateUi(main)
        self.exit.clicked.connect(self.exitclick)
        self.bat.clicked.connect(self.batclick)
        self.bowl.clicked.connect(self.bowlclick)
        self.wicketkeeper_2.clicked.connect(self.wicketkeeper_2click)
        self.allrounder_2.clicked.connect(self.allrounder_2click)
        self.list1.itemDoubleClicked['QListWidgetItem*'].connect(self.list1clearSelection)
        self.list2.itemDoubleClicked['QListWidgetItem*'].connect(self.list2selectAll)
        self.list1.itemClicked['QListWidgetItem*'].connect(self.list1Selection) 
        item = QtWidgets.QListWidgetItem()
        #project.
        self.myproject=sqlite3.connect("project.db")
        self.mycur=self.myproject.cursor()
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("warning!")
        txt=self.lineEdit_7.text()
        print(len(txt))
        if len(txt)==0:
            self.msgBox.setText("welcome")
            self.msgBox.exec()
            self.msgBox.setText("add new team using new option in menu")
            self.msgBox.exec()
        self.l=[]
        self.p=[]
        QtCore.QMetaObject.connectSlotsByName(main)
    def file_open(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form2()#INHERITED
        self.ui.setupUi(self.window)
        self.window.show()
    def file_evaluate(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def file_new(self):
        self.list2.clear()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form1()
        self.ui.setupUi(self.window)
        self.window.show()
    def batclick(self):
        self.list1.clear()
        for i in range(1,11):
            sql="SELECT player FROM cricket WHERE category='batsman' and slno='"+str(i)+"';"
            self.mycur.execute(sql)
            ply=self.mycur.fetchone()
            a=' '.join(map(str,ply))
            self.list1.addItem(a)
    def list1clearSelection(self, item):
        y=self.list2.count()
        if y<11:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item.text())
        if y>10:
                self.msgBox.setText("caannot add more players")
                self.msgBox.exec()    
        if self.bat.isChecked()==True:    
            x=self.list1.count()
            _translate = QtCore.QCoreApplication.translate
            self.batsmanlable.setText(_translate("main",str(x)))
            if x<6:
                self.msgBox.setText("caannot add more than 5 players")
                self.msgBox.exec()  
        if self.bowl.isChecked()==True:
            b=self.list1.count()
            _translate = QtCore.QCoreApplication.translate
            self.bowlerlabel.setText(_translate("main",str(10-b)))
            if b<7:
                self.msgBox.setText("caannot add more than 4 players")
                self.msgBox.exec()

        if self.wicketkeeper_2.isChecked()==True:
            c=self.list1.count()
            _translate = QtCore.QCoreApplication.translate
            self.wicketkplabel.setText(_translate("main",str(3-c)))
            if c<8:
                self.msgBox.setText("caannot add more than 1 players")
                self.msgBox.exec()
        if self.allrounder_2.isChecked()==True:
            d=self.list1.count()
            _translate = QtCore.QCoreApplication.translate
            self.allrounderlabel.setText(_translate("main",str(5-d)))
            if d<4:
                self.msgBox.setText("caannot add more than 2 players")
                self.msgBox.exec()
    
    def list1Selection(self,item):
        t=1
        print(item.text())
        txt=item.text()
        self.p.append(txt)
        print(len(item.text()))
        sql1="SELECT points FROM cricket WHERE player='"+str(txt)+"';"
        self.mycur.execute(sql1)
        poi=self.mycur.fetchone()
        a=int(''.join(map(str,poi)))
        self.l.append(a)
        _translate = QtCore.QCoreApplication.translate
        z=f(a,t)
        print(z)
        if z>4001:
           self.msgBox.setText("you have used all ur points")
           self.msgBox.exec()
        self.pusedlabel.setText(_translate("main",str(a)))
        _translate = QtCore.QCoreApplication.translate
        self.pavailablelabel.setText(_translate("main",str(4000-z)))
    def file_save(self):
        try:
            x=self.lineEdit_7.text()
            self.labeltodislpay.setText(x)
            k=len(x)
            if k==0:
                self.msgBox.setText("please enter the team name")
                self.msgBox.exec()
            print(x)
            print(self.p)
            print(self.l)
            i=''.join(map(str,self.p))  
            print(i)
            l=''.join(map(str,self.l))
            print(l)
            myproject=sqlite3.connect("team.db")
            mycur=myproject.cursor()
            sql1="INSERT INTO teams (team) VALUES ('"+x+"');"
            mycur.execute(sql1)
            myproject.commit()
            print("done")
            for i in range(0,11):
                sql="INSERT INTO '"+x+"'(points,player) VALUES ('"+str(self.l[i-1])+"','"+str(self.p[i-1])+"');"
                mycur.execute(sql)
                myproject.commit()
                print("added successfully")
            self.msgBox.setText("team saved")
            self.msgBox.exec() 
                
        except:
            self.msgBox.setText("team saved")
            self.msgBox.exec()    
    def list2selectAll(self,item):
        t=0
        self.list2.takeItem(self.list2.row(item))
        self.list1.addItem(item.text())
        u=self.list2.count()
        print(item.text())
        txt=item.text()
        sql1="SELECT points FROM cricket WHERE player='"+str(txt)+"';"
        self.mycur.execute(sql1)
        poi=self.mycur.fetchone()
        a=int(''.join(map(str,poi)))
        _translate = QtCore.QCoreApplication.translate
        z=f(a,t)
        print(z)
        q=4000-z
        print(q)
        o=q+a*u
        _translate = QtCore.QCoreApplication.translate
        self.pavailablelabel.setText(_translate("main",str(q)))
    def bowlclick(self,item):
        self.list1.clear()
        for i in range(11,21):
            sql="SELECT player FROM cricket WHERE category='bowler' and slno='"+str(i)+"';"
            self.mycur.execute(sql)
            ply=self.mycur.fetchone()
            b=' '.join(map(str,ply))
            self.list1.addItem(b)
    def wicketkeeper_2click(self,item):
        self.list1.clear()
        for i in range(26,29):
            sql="SELECT player FROM cricket WHERE category='wicket keeper' and slno='"+str(i)+"';"
            self.mycur.execute(sql)
            ply=self.mycur.fetchone()
            b=' '.join(map(str,ply))
            self.list1.addItem(b)
    def allrounder_2click(self,item):
        self.list1.clear()
        for i in range(21,26):
            sql="SELECT player FROM cricket WHERE category='allrounder' and slno='"+str(i)+"';"
            self.mycur.execute(sql)
            ply=self.mycur.fetchone()
            b=' '.join(map(str,ply))
            self.list1.addItem(b)
    def exitclick(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        main = QtWidgets.QMainWindow()
        ui = Ui_main()
        ui.setupUi(main)
        main.show()
        sys.exit(app.exec_())

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.welcome.setText(_translate("main", "<html><head/><body><div><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;font-family:times new roman;background-color:blue;color:white\">WELCOME TO FANTASY CRICKET</span></p></div></body></html>"))
        self.SELCTION.setText(_translate("main", "SELECTIONS"))
        self.allrounderlabel.setText(_translate("main", "0"))
        self.bowler.setText(_translate("main", "BOWLER"))
        self.wicketkeeper.setText(_translate("main", "WICKETKP"))
        self.bowlerlabel.setText(_translate("main", "0"))
        self.allrounder.setText(_translate("main", "ALLROUNDER"))
        self.batsmanlable.setText(_translate("main", "0"))
        self.batsman.setText(_translate("main", "BATSMAN"))
        self.pavailable.setText(_translate("main", "POINTS AVAILABLE"))
        self.wicketkplabel.setText(_translate("main", "0"))
        self.pused.setText(_translate("main", "POINTS USED"))
        self.pavailablelabel.setText(_translate("main", "0"))
        self.pusedlabel.setText(_translate("main", "0"))
        self.bat.setText(_translate("main", "BAT"))
        self.wicketkeeper_2.setText(_translate("main", "WICKET KEEPER"))
        self.allrounder_2.setText(_translate("main", "ALL ROUNDER"))
        self.bowl.setText(_translate("main", "BOWL"))
        self.teamname.setText(_translate("main", "SAVE TEAM NAME"))
        self.exit.setText(_translate("main", "EXIT"))
        self.teamnamelabel.setText(_translate("main", "TEAM NAME"))
        self.menumanage_teams.setTitle(_translate("main", "MANAGE TEAMS"))
        self.actionnew_team.setText(_translate("main", "NEW TEAM"))
        self.actionsave_team.setText(_translate("main", "SAVE TEAM"))
        self.actionevaluate.setText(_translate("main", "EVALUATE"))
        self.actionopen.setText(_translate("main", "OPEN"))
        for i in range(0,10):
            item=self.list1.item(i)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
