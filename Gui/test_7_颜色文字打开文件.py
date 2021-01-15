# coding=utf-8
# PyQt5对话框系列
# 颜色、字体和打开文件对话框

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QFontDialog, QTextEdit, QFileDialog


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("打开文件对话框")

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 270)

        self.bt_1 = QPushButton("打开文件", self)
        self.bt_1.move(350, 20)
        self.bt_2 = QPushButton("选择字体", self)
        self.bt_2.move(350, 70)
        self.bt_3 = QPushButton("选择颜色", self)
        self.bt_3.move(350, 120)

        self.bt_1.clicked.connect(self.openfile)
        self.bt_2.clicked.connect(self.choicefont)
        self.bt_3.clicked.connect(self.choicecolor)

        self.show()

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.tx.setTextColor(col)

    def choicefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def openfile(self):
        # 弹出QFileDialog对话框。 getOpenFileName（）方法中的第一个字符串是标题。
        # 第二个字符串指定对话框工作目录。
        # 默认情况下，文件过滤器设置为所有文件（*），即不限制打开文件的类型。
        # 该函数返回值类型是元组。
        # 如果增加文件过滤，则需添加第三个字符串
        fname = QFileDialog.getOpenFileName(
            self, "打开文件", "./", ("Images (*.png *.jpg *.xpm)"))
        if fname[0]:
            with open(fname[0], "r", encoding="gb18030", errors="ignore") as f:
                self.tx.setText(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
