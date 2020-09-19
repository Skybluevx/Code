# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 100, 700)
        self.setWindowTitle("消息对话框")

        self.la = QLabel("这里会显示我们选择的按钮信息", self)
        self.la.move(20, 20)

        self.bt_1 = QPushButton("提示", self)
        self.bt_1.move(20, 70)
        self.bt_2 = QPushButton("询问", self)
        self.bt_2.move(120, 70)
        self.bt_3 = QPushButton("警告", self)
        self.bt_3.move(220, 70)
        self.bt_4 = QPushButton("错误", self)
        self.bt_4.move(20, 140)
        self.bt_5 = QPushButton("关于", self)
        self.bt_5.move(120, 140)
        self.bt_6 = QPushButton("关于Qt", self)
        self.bt_6.move(220, 140)

        self.bt_1.clicked.connect(self.info)
        self.bt_2.clicked.connect()

    def question(self):
        pass

    def info(self):
        reply = QMessageBox.information(
            self, "提示", "这是一个消息提示对话框！", QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.la.setText("你选择了ok！")
        else:
            self.la.setText("你选择了Close！")
