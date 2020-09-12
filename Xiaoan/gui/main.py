import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from Ui_main_window import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toolButton.clicked.connect(self.toolButton.click)

    def toolButton(self):

        def click():
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "这是一个点击事件！！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    sys.exit(app.exec_())
