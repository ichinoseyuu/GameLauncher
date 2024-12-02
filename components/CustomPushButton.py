from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *
import os

class CustomButton(QPushButton):
    def __init__(self, text: str, path: str, parent=None):
        QPushButton.__init__(self)
        self.parent = parent
        self.setText(text)
        self.path = path
        self.setMinimumSize(184, 50)
        self.setMaximumSize(184, 50)
        self.icon = QIcon()
        self.icon.addFile(u":/btn/main_widget/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setIcon(self.icon)
        self.setIconSize(QSize(24, 24))
        self.setLayoutDirection(Qt.LeftToRight)
        self.setStyleSheet(StyleManager.btnStyle)
        if not self.parent.isEditMode:
            self.setCheckable(False)
        else:
            self.setCheckable(True)


    def mousePressEvent(self, event):
        # 重写鼠标按下事件
        if not self.isCheckable():
            self.showInExplorer(self.path)
        else:
            self.changeStyle()
        print(f'checkable:{self.isCheckable()}')
        super().mousePressEvent(event)  # 保持原有功能
        
    def showInExplorer(self, folderPath: str):
        # region 在资源管理器中显示
        Path = os.path.normpath(folderPath) #标准化路径格式
        if os.path.exists(Path):
            QProcess.startDetached("explorer", [Path])
        # endregion
        
    def changeStyle(self): 
        # region 切换按钮显示状态
        # 按钮被点击则会自动切换状态
        if self.isChecked():
            # 如果按钮已经被选中，更新显示
            self.setStyleSheet(StyleManager.btnStyle)
            print(f'selcet{self.text()}')
        else:
            # 如果按钮没有被选中，更新显示
            self.setStyleSheet(StyleManager.btnStyle)
            print(f'unselcet{self.text()}')
        # endregion
        
    def enterEvent(self, event):
        # 重写鼠标进入事件
        self.setStyleSheet(StyleManager.btnStyle)
        super().enterEvent(event)

    def leaveEvent(self, event):
        # 重写鼠标离开事件
        self.setStyleSheet(StyleManager.btnStyle)
        super().leaveEvent(event)

if __name__ == '__main__':
    app = QApplication([])

    # 创建自定义按钮
    button = CustomButton("Click Me", "icon.png")
    button.show()

    app.exec_()
