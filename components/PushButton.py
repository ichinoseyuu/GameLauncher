from PySide6.QtWidgets import QPushButton, QToolTip
from PySide6.QtCore import Qt, QSize, QProcess
from PySide6.QtGui import QIcon,QMouseEvent
from components import *
import os

class CButton(QPushButton):
    def __init__(self, text: str, path: str, parent=None):
        QPushButton.__init__(self)
        self.parent = parent
        self.setText(text)
        self.path = path
        self.setMinimumSize(180, 50)
        self.setMaximumSize(180, 50)
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
        
        if event.button() == Qt.LeftButton:
            if self.isCheckable():
                self.changeStyle()
        elif event.button() == Qt.RightButton:
            pass
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
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        if self.parent.isEditMode: return
        if event.button() == Qt.LeftButton:
            # 在资源管理器中显示文件
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
            print(f'unselcet:{self.text()}')
        else:
            # 如果按钮没有被选中，更新显示
            self.setStyleSheet(StyleManager.btnStyle)
            print(f'selcet:{self.text()}')
        # endregion
