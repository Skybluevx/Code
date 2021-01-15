# coding=utf-8
# 猜数字的小游戏

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.num = randint(1, 100)
        self.initUi()

    def initUi(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("猜数字")

        self.text = QLineEdit("点击这里输入数字", self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.bt1 = QPushButton("我猜", self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip("<b>点击这里猜数字</b>")
        self.bt1.clicked.connect(self.showMessage)

        self.show()

    def showMessage(self):
        print(self.num)

        guessnum = int(self.text.text())
        print(guessnum)

        if guessnum > self.num:
            QMessageBox.about(self, "看结果", "猜大了！！！")
            self.text.setFocus()
            self.text.selectAll()
        elif guessnum < self.num:
            QMessageBox.about(self, "看结果", "猜小了！！！")
            self.text.setFocus()
            self.text.selectAll()
        else:
            QMessageBox.about(self, "看结果", "恭喜！答对了，进入下一轮！")
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()
            self.text.selectAll()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, "确认", "确认退出吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
