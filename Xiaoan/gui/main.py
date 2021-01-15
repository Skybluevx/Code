import sys
from PyQt5 import QtWidgets
from Ui_main_window import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = MyWindow()
    mywin.show()
    sys.exit(app.exec_())
