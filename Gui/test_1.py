"""
    PyQt5制作GUI界面取得了突破性进展，目前已经额可以将按钮啥的链接到自己的函数了。
    
"""
from PyQt5 import QtWidgets, QtCore
from Ui_test_1 import Ui_Form
import sys


class MyWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def ti(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, "waring", "This is a Button event")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = MyWindow()
    my.show()
    sys.exit(app.exec_())
