# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python\Code\Gui\test_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 81, 21))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 120, 141, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.ti)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setToolTip(_translate("Form", "点击这里猜数字"))
        self.pushButton.setText(_translate("Form", "我猜"))
        self.lineEdit.setText(_translate("Form", "在这里输入数字"))
