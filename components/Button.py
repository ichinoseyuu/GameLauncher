from PySide6.QtWidgets import QPushButton, QToolTip, QMenu
from PySide6.QtCore import Qt, QSize, QProcess, QEvent,QPropertyAnimation,Property
from PySide6.QtGui import QIcon,QMouseEvent, QCursor,QColor,QPalette
from .GlobalReference import StyleSheet,ColorGroup,ObjReference
import os

class CButton(QPushButton):
    def __init__(self, name: str, parent=None):
        QPushButton.__init__(self)
        self.objectName = name

    def enterEvent(self, event):
        # 鼠标进入按钮时显示自定义信息
        self.parent.tooltip.setTip(self, self.toolTip)
        self.parent.tooltip.showTip()
        # 让父类方法继续处理事件
        super().enterEvent(event)


    def leaveEvent(self, event):
        # 鼠标离开按钮时隐藏标签
        self.parent.tooltip.hideTip()
        super().leaveEvent(event)
        
    def setToolTip(self, arg__1):
        pass




class CFolderButton(QPushButton):
    def __init__(self, text: str, path: str, parent=None):
        QPushButton.__init__(self)
        self.parent = parent
        self.setText(text)
        self.path = path
        self.cood = (0,0)

        self.setMinimumSize(180, 50)
        self.setMaximumSize(180, 50)
        self.icon = QIcon()
        self.icon.addFile(u":/btn/main_widget/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setIcon(self.icon)
        self.setIconSize(QSize(24, 24))
        self.setLayoutDirection(Qt.LeftToRight)

        self.color = ColorGroup.folder_btn_normal_color
        self.setStyleSheet(StyleSheet.get_folder_btn_styleSheet(self.color))

        if not self.parent.isEditMode:
            self.setCheckable(False)
        else:
            self.setCheckable(True)

        # 创建动画对象，用于平滑地改变背景颜色
        self.anim = QPropertyAnimation(self, b"background_color")
        self.anim.setDuration(250)  # 动画持续时间


    @Property(QColor)
    def background_color(self):
        return self.color
    @background_color.setter
    def background_color(self, color):
        self.setStyleSheet(StyleSheet.get_folder_btn_styleSheet(color))


    # @Property(QColor)
    # def border(self):
    #     return self.color
    # @border.setter
    # def background_color(self, color):
    #     self.setStyleSheet(StyleSheet.get_folder_btn_styleSheet(color))

    def contextMenuEvent(self, event):
        # 重写右键菜单事件
        contextMenu = QMenu(self)
        contextMenu.addAction("编辑",lambda: self.parent.edit(self))
        contextMenu.addAction("在资源管理器中显示", lambda: self.showInExplorer(self.path))
        contextMenu.setStyleSheet(StyleSheet.get_menu_styleSheet())
        contextMenu.exec(event.globalPos())

    def enterEvent(self, event):
        # 鼠标进入按钮时显示自定义信息
        ObjReference.obj['tooltip'].setTip(self,self.path)
        ObjReference.obj['tooltip'].showTip()
        # 触发动画改变背景颜色
        self.anim.stop()
        self.anim.setStartValue(self.color)
        self.anim.setEndValue(ColorGroup.folder_btn_hover_color)
        self.anim.start()
        super().enterEvent(event)



    def leaveEvent(self, event):
        # 鼠标离开按钮时隐藏标签
        ObjReference.obj['tooltip'].hideTip()
        # 触发动画改变背景颜色
        self.anim.stop()
        self.anim.setStartValue(ColorGroup.folder_btn_hover_color)
        self.anim.setEndValue(self.color)
        self.anim.start()
        super().leaveEvent(event)


    def mousePressEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(ColorGroup.folder_btn_hover_color)
        self.anim.setEndValue(ColorGroup.folder_btn_pressed_color)
        self.anim.start()
        if event.button() == Qt.LeftButton:
            if not self.parent.isEditMode:
                self.showInExplorer(self.path)
                return
            elif self.isCheckable() & self.parent.isEditMode:
                self.changeStyle()
        super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(ColorGroup.folder_btn_pressed_color)
        self.anim.setEndValue(ColorGroup.folder_btn_hover_color)
        self.anim.start()
        super().mouseReleaseEvent(event)


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
            self.setStyleSheet(StyleSheet.get_folder_btn_styleSheet(self.color))
            print(f'unselcet:{self.text()}')
        else:
            # 如果按钮没有被选中，更新显示
            self.setStyleSheet(StyleSheet.get_folder_btn_styleSheet(self.color))
            print(f'selcet:{self.text()}')
        # endregion

