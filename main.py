import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *

widgets = None
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 生成界面
        global widgets 
        widgets = self.ui
        
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        widgets.FolderGridLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft) # 设置布局对齐方式

        
        self.isDeleteMode = False # 当前是否在删除模式
        self.isMultiSelectMode = False # 当前是否在多选模式
        self.selectedButton = None # 当前选中的按钮
        self.colLimit = 5 # 每行最多放5个按钮
        self.index = 0 # 按钮索引
        self.isChooseGameFile = False # 是否已经选择游戏文件
        widgets.StackedWidget.setCurrentIndex(0) # 默认显示主页



        #标题栏按钮
        widgets.ButtonMin.clicked.connect(self.showMinimized) #最小化
        widgets.ButtonExit.clicked.connect(self.exitApplication) # 右上角退出 

        #左侧菜单栏按钮
        widgets.ButtonHome.clicked.connect(lambda: widgets.StackedWidget.setCurrentIndex(0))
        widgets.ButtonStart.clicked.connect(lambda: widgets.StackedWidget.setCurrentIndex(1))
        widgets.ButtonAbout.clicked.connect(lambda: widgets.StackedWidget.setCurrentIndex(2))

        #主页按钮
        widgets.ButtonPathSet.clicked.connect(self.chooseGameFile)

        #开始页按钮
        widgets.ButtonAddFolder.clicked.connect(self.openFolderDialog)
        widgets.ButtonDelFolder.clicked.connect(self.removeSelectedButton)
        widgets.ButtonEditFolder.clicked.connect(self.toggleMode)
        #self.ButtonSelectMore.clicked.connect(self.selectMore)

        # 添加淡入效果 (通过调整窗口的透明度)
        widgets.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        widgets.fadeAnim.setDuration(200)
        widgets.fadeAnim.setStartValue(0)
        widgets.fadeAnim.setEndValue(1)
        widgets.fadeAnim.start()


    def chooseGameFile(self):
        chooseFileDialog = FileDialog('游戏',self)
        reply, str = chooseFileDialog.exec()
        if reply:
            self.isChooseGameFile = True
            widgets.CurrentGameLabel.setText(f'当前游戏：{str}')


    def openFolderDialog(self):
        chooseFileDialog = FolderDialog('文件夹',self)                        
        reply, name, path = chooseFileDialog.exec()
        if reply:
            self.addFolder(name, path)   
 
    def addFolder(self, name, path):
        # 计算新按钮应该放置的位置
        row = self.ui.FolderGridLayout.count() // self.colLimit 
        col = self.ui.FolderGridLayout.count() % self.colLimit   
        # 创建新按钮
        newBtn = QPushButton(f"{name}")
        newBtn.setStyleSheet(
                'QPushButton {'
                '   background-color: rgb(235, 235, 235);'
	            '   font-family: "微软雅黑";'
	            '   font-size: 10pt;'
	            '   color: dimgray;'
                '   border-radius: 2px;'
                '}'
                'QPushButton:hover {'
                '   background-color: gainsboro;'
                '   border-radius: 2px;'
                '}'
                'QPushButton:pressed {'
                '   background-color: lightgray;'
                '   border-radius: 2px;'
                '}'
            )
        newBtn.setMinimumSize(184, 50)
        newBtn.setMaximumSize(184, 50)
        newBtn.clicked.connect(lambda: self.showInExplorer(path))
        #newButton.clicked.connect(lambda _, btn=newButton: self.changeButtonState(btn))
        newBtn.clicked.connect(lambda: self.changeButtonState(newBtn))
        # 将新按钮添加到网格布局
        self.ui.FolderGridLayout.addWidget(newBtn, row, col)
    
    def showInExplorer(self, path):
        if self.isDeleteMode: return
        filePath = os.path.normpath(path)
        if os.path.exists(filePath):
            QProcess.startDetached("explorer", [filePath])

    def toggleMode(self):
        self.isDeleteMode = not self.isDeleteMode
        if self.isDeleteMode:
            print("已进入删除模式")
        else:
            
            print("已退出删除模式")


    def changeButtonState(self, button):
        if self.isDeleteMode:
            # 如果已经选中了一个按钮，移除其边框
            if self.selectedButton:
                self.selectedButton.setStyleSheet(
                'QPushButton {'
                '   background-color: rgb(235, 235, 235);'
	            '   font-family: "微软雅黑";'
	            '   font-size: 10pt;'
	            '   color: dimgray;'
                '   border-radius: 2px;'
                '}'
                'QPushButton:hover {'
                '   background-color: gainsboro;'
                '   border-radius: 2px;'
                '}'
                'QPushButton:pressed {'
                '   background-color: lightgray;'
                '   border-radius: 2px;'
                '}'
            )

            # 设置新的选中按钮的边框
            self.selectedButton = button
            self.selectedButton.setStyleSheet(
                'QPushButton {'
                '   background-color: rgb(235, 235, 235);'
	            '   font-family: "微软雅黑";'
	            '   font-size: 10pt;'
	            '   color: dimgray;'
                '   border-radius: 2px;'
                '   border: 1px solid dimgray;'
                '}'
                'QPushButton:hover {'
                '   background-color: gainsboro;'
                '   border-radius: 2px;'
                '}'
                'QPushButton:pressed {'
                '   background-color: lightgray;'
                '   border-radius: 2px;'
                '}'
            )
            print(f"已选中按钮 {self.selectedButton.text()}")

        # 从指定位置开始，将后面的按钮重新排列
    def rearrangeButtons(self, row: int, col: int):
        # 传入位置为最后一列
        if col == widgets.FolderGridLayout.columnCount() - 1:
            # 获取下下一个位置的控件
            next_item = widgets.FolderGridLayout.itemAtPosition(row + 1, 0)
            # 下一个位置为空，结束
            if not next_item: return   
            widgets.FolderGridLayout.addWidget(next_item.widget(), row, col)
            return self.rearrangeButtons(row + 1, 0)
        # 传入位置不在最后一列
        next_item = widgets.FolderGridLayout.itemAtPosition(row, col + 1)
        # 下一个位置为空，结束
        if not next_item: return   
        widgets.FolderGridLayout.addWidget(next_item.widget(), row, col)
        return self.rearrangeButtons(row, col + 1)

    def removeSelectedButton(self):
        if self.selectedButton:
            # 获取被选中按钮的位置
            row, col = widgets.FolderGridLayout.getItemPosition(widgets.FolderGridLayout.indexOf(self.selectedButton))[:2]
            # 删除选中的按钮
            self.selectedButton.deleteLater()
            print(f"{self.selectedButton.text()} is deleted")
            # 重新排列其他按钮的位置
            self.rearrangeButtons(row, col)
            # 更新保存的按钮位置

            # 清除选中的按钮
            self.selectedButton = None  






    def mousePressEvent(self, event):
        UtilityFunctions.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        UtilityFunctions.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        UtilityFunctions.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        UtilityFunctions.paintShadow(self)

        #退出程序
    def exitApplication(self):
        message = Message('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            widgets.fadeAnim.setStartValue(1)
            widgets.fadeAnim.setEndValue(0)
            widgets.fadeAnim.finished.connect(lambda:QApplication.instance().quit())
            widgets.fadeAnim.start()

    #region 旧版退出程序
    # def closeEvent(self, event):
    #     message = CustomMessage('退出', '您确定要退出吗？')
    #     reply = message.exec()
    #     if reply == 1:
    #         self.fadeAnim.start()
    #         event.accept()       
    #     else:
    #         event.ignore()
    # endregion


            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())