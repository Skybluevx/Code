import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_test import Ui_Dialog


class MyWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = MyWindow()
    windows.show()
    sys.exit(app.exec_())
