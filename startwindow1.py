# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_main

class Ui_Form(object):
    def new_2click(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_main()#inherited
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()
    def exitclick(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1096, 722)
        self.fantsasylogo = QtWidgets.QLabel(Form)
        self.fantsasylogo.setGeometry(QtCore.QRect(160, 30, 701, 511))
        self.fantsasylogo.setText("")
        #SHOW THE IMAGE
        self.fantsasylogo.setPixmap(QtGui.QPixmap("fantasy-cricket-app.jpg"))
        self.fantsasylogo.setAlignment(QtCore.Qt.AlignCenter)
        self.fantsasylogo.setObjectName("fantsasylogo")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(250, 140, 481, 291))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.new_2 = QtWidgets.QPushButton(self.widget)
        self.new_2.setObjectName("new_2")
        self.gridLayout.addWidget(self.new_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setObjectName("exit")
        self.gridLayout.addWidget(self.exit, 2, 0, 1, 1)

        self.retranslateUi(Form)
        #CLICK BUTTONS
        self.new_2.clicked.connect(self.new_2click)
        self.exit.clicked.connect(self.exitclick)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "STARTWINDOW"))
        self.new_2.setText(_translate("Form", "START"))
        self.exit.setText(_translate("Form", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
