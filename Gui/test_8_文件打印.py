import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QDialog
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.printer = QPrinter()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle("打印文件窗口")

        self.tx = QTextEdit(self)

        self.bt_1 = QPushButton("打开文件", self)
        self.bt_2 = QPushButton("打开多个文件", self)
        self.bt_3 = QPushButton("保存文件", self)
        self.bt_4 = QPushButton("页面设置", self)
        self.bt_5 = QPushButton("打印文档", self)
        self.bt_1.move(350, 20)
        self.bt_2.move(350, 70)
        self.bt_3.move(350, 220)
        self.bt_4.move(350, 270)
        self.bt_5.move(350, 320)

        self.bt_1.clicked.connect(self.openfile)
        self.bt_2.clicked.connect(self.openfiles)
        self.bt_3.clicked.connect(self.savefile)
        self.bt_4.clicked.connect(self.pagesettings)
        self.bt_5.clicked.connect(self.printdialog)

        self.show()

    def printdialog(self):
        printdialag = QPrintDialog(self.printer, self)
        if QDialog.Accepted == printdialag.exec_():
            self.tx.print(self.printer)

    def pagesettings(self):
        printsetdialog = QPageSetupDialog(self.printer, self)
        printsetdialog.exec_()

    def savefile(self):
        file_name = QFileDialog.getSaveFileName(self, "保存文件", "./", "Text file (*.txt)")
        if file_name[0]:
            with open(file_name, "w", encoding="utf-8", errors="ignore") as f:
                f.write(self.tx.toPlainText())

    def openfiles(self):
        fnames = QFileDialog.getOpenFileName(
            self, "打开文件", "./", ("Images (*.png *.jpg *.xpm)"))
        if fnames[0]:
            for fname in fnames[0]:
                with open(fname[0], "r", encoding="gb18030", errors="ignore") as f:
                    self.tx.setText(f.read())

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
