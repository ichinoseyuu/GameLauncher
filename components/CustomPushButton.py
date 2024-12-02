from PySide6.QtGui import QMouseEvent
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
        print(self.isCheckable())
        if self.isCheckable():
            self.changeStyle()
        if event.button() == Qt.LeftButton:
            print("left button clicked")

        elif event.button() == Qt.RightButton:
            print("Right button clicked")
        super().mousePressEvent(event)
            
            
    def enterEvent(self, event):
        # 鼠标进入按钮时显示自定义信息
        QToolTip.showText(event.globalPos(), self.path, self)
        # 让父类方法继续处理事件
        #self.setStyleSheet(StyleManager.btnStyle)
        super().enterEvent(event)
        pass

    def leaveEvent(self, event):
        # 鼠标离开按钮时隐藏标签
        QToolTip.hideText()
        #self.setStyleSheet(StyleManager.btnStyle)
        super().leaveEvent(event)
        pass
    
    def mouseMoveEvent(self, event):
        # 鼠标在按钮上移动时，标签随着鼠标移动
        #QToolTip.showText(event.globalPos(), self.path, self)
        super().mouseMoveEvent(event)
        pass
    
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.showInExplorer(self.path)
        return super().mouseDoubleClickEvent(event)


        
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
            print(f'selcet:{self.text()}')
        else:
            # 如果按钮没有被选中，更新显示
            self.setStyleSheet(StyleManager.btnStyle)
            print(f'unselcet:{self.text()}')
        # endregion
