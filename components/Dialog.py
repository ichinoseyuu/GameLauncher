import os
import enum
from PySide6.QtWidgets import QDialog,QFileDialog
from PySide6.QtCore import Qt,QPropertyAnimation
from .Ui_FileDialog import Ui_Dialog
from .Functions import GenericFunc

class CFileDialog(QDialog, Ui_Dialog):
    class DialogMode(enum.IntEnum):
        File = 0
        Folder = 1
    def __init__(self, tip: str = '', dir: str = '', mode = DialogMode.File ,parent = None):
        super(CFileDialog, self).__init__()
        self.parent = parent
        self.mode = mode
        self.dir = dir
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self.parent.geometry()))

        self.ButtonExit.clicked.connect(self.cancel)
        self.ButtonCancel.clicked.connect(self.cancel)
        self.ButtonOk.clicked.connect(self.confirm)

        self.ButtonChooseFolder.clicked.connect(lambda: self.chooseFile(self.mode))

        # 设置输入框的输入提示
        self.Title.setText(f'添加{tip}')
        self.PathLineEdit.setPlaceholderText(f'未选择{tip}')
        self.NameLineEdit.setPlaceholderText('请输入名称')
        self.isSelected = False
        self.isConfirm = False

        # 添加淡入效果 (通过调整窗口的透明度)
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)
        self.fadeAnim.setStartValue(0)
        self.fadeAnim.setEndValue(1)
        self.fadeAnim.start()

    def chooseFile(self, mode = DialogMode.File):
        if mode == self.DialogMode.File:
            selectedFiles, _ = QFileDialog.getOpenFileNames(self, "选择程序", "", "程序 (*.exe)")
            if not selectedFiles: return 
            self.isSelected = True
            fileName = os.path.basename(selectedFiles[0])
            fileNameWithoutExt, _ =  os.path.splitext(fileName)
            self.PathLineEdit.setText(selectedFiles[0])
            self.NameLineEdit.setText(fileNameWithoutExt)

        elif mode == self.DialogMode.Folder:
            folderPath = QFileDialog.getExistingDirectory(self, "选择文件夹",self.dir)
            if not folderPath: return
            self.isSelected = True
            folderName = os.path.basename(folderPath)
            self.PathLineEdit.setText(folderPath)
            self.NameLineEdit.setText(folderName)


    def exec(self):
        super().exec()
        if self.isSelected & self.isConfirm:
            return 1, self.NameLineEdit.text(), self.PathLineEdit.text()
        else:
            return 0, '', ''



    def cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.isConfirm = False
        self.fadeAnim.finished.connect(self.reject)  # 动画完成后关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.start()  # 启动动画

    def confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.isConfirm = True
        self.fadeAnim.finished.connect(self.accept)  # 动画完成后关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.start()  # 启动动画


    def mousePressEvent(self, event):
        GenericFunc.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        GenericFunc.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        GenericFunc.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        super().paintEvent(event)
        GenericFunc.paintShadow(self)