# coding = utf-8
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QInputDialog, QTextBrowser, QLineEdit
from test_10_PasswdDialog import PasswdDialog
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(380, 180)
        self.setWindowTitle("主界面")

        self.lb1 = QLabel("密码在此显示...")
        self.lb1.move(20, 20)

        self.bt1 = QPushButton("输入密码（普通型）", self)
        self.bt1.move(20, 60)

        self.bt2 = QPushButton("输入密码（普通增强型）", self)
        self.bt2.move(20, 100)

        self.bt3 = QPushButton("输入密码（热别加强型）", self)
        self.bt3.move(20, 140)

        self.show()

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)

    def showDialog(self):
        sender = self.sender()
        if sender == self.bt1:
            text, ok = QInputDialog.getText(
                self, "密码输入框", "请输入密码", QLineEdit.Password)
            if ok:
                self.lb1.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getText(
                self, "密码输入框", "请输入密码", QLineEdit.PasswordEchoOnEdit)
            if ok:
                self.lb1.setText(text)
        else:
            pwd = PasswdDialog()
            r = pwd.exec_()
            if r:
                self.lb1.setText(pwd.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
