import sys
import os
import enum
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *


widgets = None
class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.btnData = ButtonManager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 生成界面
        global widgets 
        widgets = self.ui
        
        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        widgets.FolderGridLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft) # 设置布局对齐方式
        widgets.FolderGridLayout.setColumnMinimumWidth(0, 184)
        widgets.FolderGridLayout.setColumnMinimumWidth(1, 184)
        widgets.FolderGridLayout.setColumnMinimumWidth(2, 184)
        widgets.FolderGridLayout.setColumnMinimumWidth(3, 184)
        widgets.FolderGridLayout.setColumnMinimumWidth(4, 184)
        widgets.FolderGridLayout.setRowMinimumHeight(0, 50)
        widgets.FolderGridLayout.setRowMinimumHeight(1, 50)
        widgets.FolderGridLayout.setRowMinimumHeight(2, 50)
        widgets.FolderGridLayout.setRowMinimumHeight(3, 50)
        widgets.FolderGridLayout.setRowMinimumHeight(4, 50)


        self.isEditMode = False # 当前是否在删除模式
        self.colLimit = 5 # 每行最多放5个按钮
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
        widgets.ButtonDelFolder.clicked.connect(self.removeSelectedButtons)
        widgets.ButtonEditFolder.clicked.connect(self.toggleMode)
        #self.ButtonSelectMore.clicked.connect(self.selectMore)

        # 添加淡入效果 (通过调整窗口的透明度)
        widgets.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        widgets.fadeAnim.setDuration(200)
        widgets.fadeAnim.setStartValue(0)
        widgets.fadeAnim.setEndValue(1)
        widgets.fadeAnim.start()


    def chooseGameFile(self):
        # region 选择游戏文件
        fileDialog = CFileDialog('游戏',CFileDialog.DialogMode.File, self)
        reply, name, path = fileDialog.exec()
        if reply:
            self.isChooseGameFile = True
            widgets.CurrentGameLabel.setText(f'当前游戏：{name}')
        # endregion


    def openFolderDialog(self):
        # region 打开文件夹选择对话框
        folderDialog = CFileDialog('文件夹',CFileDialog.DialogMode.Folder, self)                        
        reply, name, path = folderDialog.exec()
        if reply:
            #self.addFolder(name, path)
            self.testadd()
        # endregion

    
    def addFolder(self, name: str, path: str):
        # region 添加按钮
        # 计算新按钮应该放置的位置
        row = self.ui.FolderGridLayout.count() // self.colLimit 
        col = self.ui.FolderGridLayout.count() % self.colLimit   
        # 创建新按钮
        newBtn = CButton(name, path, self)
        item ={(row, col):{'name':name, 'obj':newBtn, 'path':path}}
        self.btnData.buttons.update(item)
        widgets.FolderGridLayout.addWidget(newBtn, row, col)
        # endregion
        
    def toggleMode(self):
        # region 切换模式
        self.isEditMode = not self.isEditMode
        btns = self.btnData.getAllBtns()
        if self.isEditMode:
            # 将所有存在的按钮改为checkable状态
            self.btnData.toggleCheckable(btns)
            print('进入编辑模式')
        else:
            self.btnData.toggleCheckable(btns)
            print('退出编辑模式')
        self.btnData.printBtns()
        # endregion           
    

    def removeSelectedButtons(self):
        btns = self.btnData.getSelectedBtns()
        self.btnData.delSelectedBtns(btns,self)
        # region old_删除选中的按钮
        # coods , btns = self.btnData.getSelectedBtns()
        # if not btns: return
        # self.btnData.delSelectedBtns(btns, self.colLimit)
        # for cood in coods:
        #     self.rearrangeButtons(cood[0], cood[1])
        # self.btnData.printBtns()
        # print(coods)
        # endregion    
        # region  old_删除选中的按钮
        # btns = self.btnData.getSelectedBtns()
        # if not btns: return
        # points = []
        # for btn in btns:
        #     # 获取被选中按钮的位置
        #     row, col = widgets.FolderGridLayout.getItemPosition(widgets.FolderGridLayout.indexOf(btn))[:2]
        #     points.append((row, col))
        #     btn.setCheckable(not btn.isCheckable())
        # self.btnData.delSelectedBtns()
        # self.rearrangeButtons(row, col)
        # endregion
    
    def testadd(self):
        paths = ['./test','./components', './data', './qss', './resources', './.vscode', './ui', './__pycache__']
        names = ['test','components', 'data', 'qss', 'resources', '.vscode', 'ui', '__pycache__']
        for i in range(len(paths)):
            self.addFolder(names[i], paths[i])
    

    def updateBtns(self, row: int, col: int):
        # region 从指定位置开始将按钮重新排列
        if col == self.colLimit - 1:
            # 获取下下一个位置的控件
            next_item = widgets.FolderGridLayout.itemAtPosition(row + 1, 0)
            if next_item is None:
                
                return
            widgets.FolderGridLayout.addWidget(next_item.widget(), row, col)
            return self.updateBtns(row + 1, 0)
        # 传入位置不在最后一列
        next_item = widgets.FolderGridLayout.itemAtPosition(row, col + 1)
        if next_item is None:
            
            return
        widgets.FolderGridLayout.addWidget(next_item.widget(), row, col)
        return self.updateBtns(row, col + 1)
        # endregion
        
    def getFirstEmptyRowAndCol(self):
        # region 获取第一个空位
        for i in range(widgets.FolderGridLayout.count()):
            item = widgets.FolderGridLayout.itemAt(i)
        if item is None:
            return i // self.colLimit, i % self.colLimit
        # endregion
        
    def getFirstEmptyIndex(self):
        # region 获取第一个空位
        for i in range(widgets.FolderGridLayout.count()):
            item = widgets.FolderGridLayout.itemAt(i)
        if item is None:
            return i
        # endregion


    def mousePressEvent(self, event):
        UtilityFunctions.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        UtilityFunctions.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        UtilityFunctions.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        UtilityFunctions.paintShadow(self)


    def exitApplication(self):
        #region 退出程序
        message = CMessage('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            widgets.fadeAnim.setStartValue(1)
            widgets.fadeAnim.setEndValue(0)
            widgets.fadeAnim.finished.connect(lambda:QApplication.instance().quit())
            widgets.fadeAnim.start()
        #endregion

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