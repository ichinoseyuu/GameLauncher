from PySide6.QtWidgets import QPushButton, QToolTip, QMenu
from PySide6.QtCore import Qt, QSize, QProcess
from PySide6.QtGui import QIcon,QMouseEvent
from .Dialog import CFileDialog
from .DataManager import StyleManager, UserData
from .DynamicTip import CDynamicTip
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
        super().mousePressEvent(event)


    def contextMenuEvent(self, event):
        # 重写右键菜单事件
        contextMenu = QMenu(self)
        contextMenu.addAction("编辑", self.edit)
        contextMenu.addAction("在资源管理器中显示", lambda: self.showInExplorer(self.path))
        contextMenu.setStyleSheet(StyleManager.btnStyle)
        contextMenu.exec(event.globalPos())


    def edit(self):
        # 打开编辑对话框
        dir = os.path.dirname(UserData.games[self.parent.currentGame]['path'])
        dialog = CFileDialog('', dir, CFileDialog.DialogMode.Folder ,self.parent)
        dialog.Title.setText('编辑文件夹')
        dialog.PathLineEdit.setPlaceholderText('请选择要更改的路径')
        dialog.NameLineEdit.setPlaceholderText('请输入要更改的名称')
        reply, name, path = dialog.exec()
        if reply == 1:
            self.setText(name)
            self.path = path
            self.parent.tip = CDynamicTip(f'成功修改文件夹', CDynamicTip.PosMode.Center, self.parent)


    def enterEvent(self, event):
        # 鼠标进入按钮时显示自定义信息
        QToolTip.showText(event.globalPos(), self.path, self)
        # 让父类方法继续处理事件
        #self.setStyleSheet(StyleManager.btnStyle)
        super().enterEvent(event)


    def leaveEvent(self, event):
        # 鼠标离开按钮时隐藏标签
        QToolTip.hideText()
        #self.setStyleSheet(StyleManager.btnStyle)
        super().leaveEvent(event)


    def mouseMoveEvent(self, event):
        # 鼠标在按钮上移动时，标签随着鼠标移动
        #QToolTip.showText(event.globalPos(), self.path, self)
        super().mouseMoveEvent(event)


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
