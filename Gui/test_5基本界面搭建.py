# coding=utf-8

# PyQt5：界面搭建

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        # 创建一个状态栏，显示状态信息
        self.statusBar().showMessage("准备就绪")

        # 设置窗口的位置以及大小
        self.setGeometry(300, 300, 1300, 700)
        # 设置窗口的标题
        self.setWindowTitle("工作空间")

        # 创建一个带有图标以及标签的动作
        exit_act = QAction(QIcon("./123.jpg"), "退出(&E)", self)
        # 设置这个动作的快捷方式
        exit_act.setShortcut("Ctrl+Q")
        # 设置这个动作的状态
        exit_act.setStatusTip("退出程序")
        # 将此动作的信号发送到quit()槽函数中用于退出程序
        exit_act.triggered.connect(qApp.quit)

        new_act = QAction(QIcon("./123.jpg"), "新建(&N)", self)
        new_act.setShortcut("Ctrl+N")

        # 创建新菜单
        save_menu = QMenu("保存方式(&S)", self)
        save_act = QAction(QIcon("./123.jpg"), "保存...", self)
        save_act.setShortcut("Ctrl+S")
        save_act.setStatusTip("保存文件")
        save_as_act = QAction(QIcon("./123.jpg"), "另存为...", self)
        save_as_act.setStatusTip("文件另存为")
        # 将两个操作添加至菜单中
        save_menu.addActions([save_act, save_as_act])

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 在菜单栏增加一个菜单并进行命名
        file_menu = menubar.addMenu("文件(&E)")
        # 为菜单添加一个操作
        file_menu.addAction(new_act)
        # 对菜单添加一个子菜单
        file_menu.addMenu(save_menu)
        # 添加一个分隔符
        file_menu.addSeparator()
        file_menu.addAction(exit_act)

        # 添加工具栏
        tool_bar = self.addToolBar("工具栏")
        # 将动作添加至工具栏中（工具栏显示的为图标，若是没有则显示为空白）
        tool_bar.addActions([new_act, exit_act])

        self.show()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        new_act = cmenu.addAction("新建")
        ope_act = cmenu.addAction("保存")
        quit_act = cmenu.addAction("退出")
        # 使用exec_()方法显示上下文菜单。 从事件对象获取鼠标指针的坐标。
        # mapToGlobal()方法将窗口小部件坐标转换为全局屏幕坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        # 如果从上下文菜单返回的操作等于退出操作，我们终止应用程序。
        if action == quit_act:
            qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
