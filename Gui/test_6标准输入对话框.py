# coding=utf-8
# PyQt5的对话框系列
# 标准输入对话框

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("对话框系列")

        self.lab_1 = QLabel("姓名：", self)
        self.lab_1.move(20, 20)

        self.lab_2 = QLabel("年龄：", self)
        self.lab_2.move(20, 80)

        self.lab_3 = QLabel("性别：", self)
        self.lab_3.move(20, 140)

        self.lab_4 = QLabel("身高(cm)：", self)
        self.lab_4.move(20, 200)

        self.lab_5 = QLabel("基本信息：", self)
        self.lab_5.move(20, 260)

        self.lab_1_1 = QLabel("学点编程", self)
        self.lab_1_1.move(80, 20)

        self.lab_2_1 = QLabel("18", self)
        self.lab_2_1.move(80, 80)

        self.lab_3_1 = QLabel("男", self)
        self.lab_3_1.move(80, 140)

        self.lab_4_1 = QLabel("175", self)
        self.lab_4_1.move(120, 200)

        self.tb = QTextBrowser(self)
        self.tb.move(20, 320)

        self.bt1 = QPushButton("修改姓名", self)
        self.bt1.move(200, 20)

        self.bt2 = QPushButton('修改年龄', self)
        self.bt2.move(200, 80)

        self.bt3 = QPushButton('修改性别', self)
        self.bt3.move(200, 140)

        self.bt4 = QPushButton('修改身高', self)
        self.bt4.move(200, 200)

        self.bt5 = QPushButton('修改信息', self)
        self.bt5.move(200, 260)

        self.bt1.clicked.connect(self.showDialog)
        self.bt2.clicked.connect(self.showDialog)
        self.bt3.clicked.connect(self.showDialog)
        self.bt4.clicked.connect(self.showDialog)
        self.bt5.clicked.connect(self.showDialog)

        self.show()

    def showDialog(self):
        sender = self.sender()
        sex = ["男", "女"]
        if sender == self.bt1:
            text, ok = QInputDialog.getText(self, "修改姓名", "请输入姓名：")
            if ok:
                self.lab_1_1.setText(text)
        elif sender == self.bt2:
            text, ok = QInputDialog.getInt(self, "修改年龄", "请输入年龄：", min=1)
            if ok:
                self.lab_2_1.setText(str(text))
        elif sender == self.bt3:
            text, ok = QInputDialog.getItem(self, "修改性别", "请选择性别：", sex)
            if ok:
                self.lab_3_1.setText(text)
        elif sender == self.bt4:
            text, ok = QInputDialog.getDouble(self, "修改身高", "请输入身高：", min=1.0)
            if ok:
                self.lab_4_1.setText(str(text))
        elif sender == self.bt5:
            text, ok = QInputDialog.getMultiLineText(self, "修改信息", "请输入个人信息：")
            if ok:
                self.tb.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
