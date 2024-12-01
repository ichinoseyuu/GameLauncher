import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from .Ui_Message import Ui_Message
from .Ui_FileDialog import Ui_Dialog
from .Functions import UtilityFunctions

class FolderDialog(QDialog, Ui_Dialog):
    def __init__(self, tip: str = '', parent = None):
        super(FolderDialog, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(UtilityFunctions.calculatedGeometricPos(self.geometry(),self.parent.geometry()))

        self.ButtonExit.clicked.connect(self.cancel)
        self.ButtonCancel.clicked.connect(self.cancel)
        self.ButtonOk.clicked.connect(self.confirm)

        self.ButtonChooseFolder.clicked.connect(self.chooseFolder)

        # 设置输入框的输入提示
        self.Title.setText(f'添加{tip}')
        self.FolderPathLineEdit.setPlaceholderText(f'未选择{tip}')
        self.FolderNameLineEdit.setPlaceholderText('请输入名称')
        self.isChooseFolder = False

        # 添加淡入效果 (通过调整窗口的透明度)
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)
        self.fadeAnim.setStartValue(0)
        self.fadeAnim.setEndValue(1)
        self.fadeAnim.start()

    def chooseFolder(self):
        folderPath = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if not folderPath: return
        self.isChooseFolder = True
        folderName = os.path.basename(folderPath)
        self.FolderPathLineEdit.setText(folderPath)
        self.FolderNameLineEdit.setText(folderName)
        

    def exec(self):
        super().exec()  
        return self.isChooseFolder,self.FolderNameLineEdit.text(),self.FolderPathLineEdit.text()
    
    def cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.reject)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画

    def confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.accept)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画
        

    def mousePressEvent(self, event):
        UtilityFunctions.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        UtilityFunctions.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        UtilityFunctions.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        UtilityFunctions.paintShadow(self)



class FileDialog(QDialog, Ui_Dialog):
    def __init__(self, tip: str = '', parent = None):
        super(FileDialog, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(UtilityFunctions.calculatedGeometricPos(self.geometry(),self.parent.geometry()))

        self.ButtonExit.clicked.connect(self.cancel)
        self.ButtonCancel.clicked.connect(self.cancel)
        self.ButtonOk.clicked.connect(self.confirm)

        self.ButtonChooseFolder.clicked.connect(self.chooseFile)

        # 设置输入框的输入提示
        self.Title.setText(f'添加{tip}')
        self.FolderPathLineEdit.setPlaceholderText(f'未选择{tip}')
        self.FolderNameLineEdit.setPlaceholderText('请输入名称')
        self.isChooseFolder = False

        # 添加淡入效果 (通过调整窗口的透明度)
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)
        self.fadeAnim.setStartValue(0)
        self.fadeAnim.setEndValue(1)
        self.fadeAnim.start()

    def chooseFile(self):
        selectedFiles, _ = QFileDialog.getOpenFileNames(self, "选择程序", "", "程序 (*.exe)")
        if not selectedFiles: return 
        self.isChooseFolder = True
        fileName = os.path.basename(selectedFiles[0])
        self.FolderPathLineEdit.setText(selectedFiles[0])
        self.FolderNameLineEdit.setText(fileName)
        

    def exec(self):
        super().exec()  
        return self.isChooseFolder,self.FolderNameLineEdit.text()
    
    def cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.reject)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画

    def confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.accept)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画
        

    def mousePressEvent(self, event):
        UtilityFunctions.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        UtilityFunctions.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        UtilityFunctions.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        UtilityFunctions.paintShadow(self)


class Message(QDialog, Ui_Message) :
    def __init__(self, tip = '', message = '', parent=None):
        super(Message, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(UtilityFunctions.calculatedGeometricPos(self.geometry(),self.parent.geometry()))

        self.Title.setText(tip)
        self.MessageLabel.setText(message)

        self.ButtonExit.clicked.connect(self.cancel)
        self.ButtonCancel.clicked.connect(self.cancel)
        self.ButtonOk.clicked.connect(self.confirm)

        # 添加淡入效果 (通过调整窗口的透明度)
        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(200)
        self.fadeAnim.setStartValue(0)
        self.fadeAnim.setEndValue(1)
        self.fadeAnim.start()
    
    def exec(self):
        return super().exec()     
    
    def cancel(self):
        # 当点击退出按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.reject)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画

    def confirm(self):
        # 当点击确定按钮时，执行淡出动画并关闭窗口
        self.fadeAnim.setStartValue(1)  # 当前为不透明
        self.fadeAnim.setEndValue(0)  # 淡出到透明
        self.fadeAnim.finished.connect(self.accept)  # 动画完成后关闭窗口
        self.fadeAnim.start()  # 启动动画

    def mousePressEvent(self, event):
        UtilityFunctions.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        UtilityFunctions.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        UtilityFunctions.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        UtilityFunctions.paintShadow(self)
 

if __name__ == "__main__":
    pass