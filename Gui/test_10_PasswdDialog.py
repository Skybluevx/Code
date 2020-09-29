from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator


class PasswdDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 100)
        self.setWindowTitle("密码输入框")

        self.lb = QLabel("请输入密码：")

        self.edit = QLineEdit(self)
        self.edit.installEventFilter(self)

        self.bt1 = QPushButton("确定", self)
        self.bt2 = QPushButton("取消", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.bt1)
        hbox.addStretch(1)
        hbox.addWidget(self.bt2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.edit)
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.edit.setContextMenuPolicy(Qt.NoContextMenu)
        self.edit.setPlaceholderText("密码6-15位，只能有数字和字母，必须以字母开头")
        self.edit.setEchoMode(QLineEdit.Password)

        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.edit)
        self.edit.setValidator(validator)

        self.bt1.clicked.connect(self.Ok)
        self.bt2.clicked.connect(self.Cancel)

        object = QObject()

    def eventFilter(self, object, event):
        if object == self.edit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event)
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(QKeySequence.Paste):
                    return True

        return QDialog.eventFilter(self, object, event)  # 继续传递该事件到被观察者，由其本身调用相应事件

    def Cancel(self):
        self.done(0)  # 结束对话框返回0

    def Ok(self):
        self.text = self.edit.text()
        if len(self.text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.text) < 6:
            QMessageBox.warning(self, "警告", "消息长度小于六位")
        else:
            self.done(1)
