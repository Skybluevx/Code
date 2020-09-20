# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QCheckBox
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
        self.bt_2.clicked.connect(self.question)
        self.bt_3.clicked.connect(self.waring)

    def waring(self):
        cb = QCheckBox("所有文档都按此操作")
        msgbox = QMessageBox()
        msgbox.setWindowTitle("警告")
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("这是一个警告消息对话框")
        msgbox.setInformativeText("出现更改愿意保存吗？")
        save = msgbox.addButton("保存", QMessageBox.AcceptRole)
        nosave = msgbox.addButton("取消", QMessageBox.RejectRole)
        cancel = msgbox.addButton("不保存", QMessageBox.DestructiveRole)
        msgbox.setDefaultButton(save)
        msgbox.setCheckBox(cb)
        cb.stateChanged.connect(self.check)
        reply = msgbox.exec()

        if reply == QMessageBox.Retry:
            self.la.setText("你选择了Retry！")
        elif reply == QMessageBox.Abort:
            self.la.setText("你选择了Abort！")
        else:
            self.la.setText("你选择了Ignore!")

    def about(self):
        msgbox = QMessageBox(QMessageBox.NoIcon, "关于", "别想了，早点洗洗睡吧！")
        msgbox.setIconPixmap(QPixmap("./123.png"))
        msgbox.exec()

    def aboutqt(self):
        QMessageBox.aboutQt(self, "关于Qt")

    def check(self):
        if self.sender().isChecked():
            self.la.setText("你又打勾了哦")
        else:
            self.la.setText("怎么又不打了")

    def question(self):
        reply = QMessageBox.question(self, "询问", "这是一个询问消息对话框， 默认是No",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.la.setText("你选择了Yes！")
        elif reply == QMessageBox.No:
            self.la.setText("你选择了No！")
        else:
            self.la.setText("你选择了Cancel！")

    def info(self):
        reply = QMessageBox.information(
            self, "提示", "这是一个消息提示对话框！", QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.la.setText("你选择了ok！")
        else:
            self.la.setText("你选择了Close！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
