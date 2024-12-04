import sys
import os
import enum
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *


widgets = None
class MainWindow(QMainWindow):
    #region 初始化
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
        widgets.ButtonNext.clicked.connect(self.nextPage)
        widgets.ButtonChangeGame.clicked.connect(self.swithGame)
        #主页下拉菜单
        widgets.GameComboBox.currentIndexChanged.connect(self.swithGame)

        #开始页按钮
        widgets.ButtonAddFolder.clicked.connect(self.openFolderDialog)
        widgets.ButtonDelFolder.clicked.connect(self.removeSelectedButtons)
        widgets.ButtonEditFolder.clicked.connect(self.toggleMode)
        widgets.ButtonSelectAll.clicked.connect(self.selectAllBtns)
        widgets.ButtonSelectAll.setVisible(False)


        # 关于页按钮
        widgets.ButtonGitHub.clicked.connect(self.goToMyGithub)
        widgets.ButtonCheckUpdate.clicked.connect(self.checkUpdate)
        widgets.ButtonRemoveUerdata.clicked.connect(self.removeUserdata)


        # 添加淡入效果 (通过调整窗口的透明度)
        widgets.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        widgets.fadeAnim.setDuration(200)
        widgets.fadeAnim.setStartValue(0)
        widgets.fadeAnim.setEndValue(1)
        widgets.fadeAnim.start()
        #endregion


# region homePage相关函数

    # 打开游戏选择对话框
    def chooseGameFile(self):
        fileDialog = CFileDialog('游戏',CFileDialog.DialogMode.File, self)
        reply, name, path = fileDialog.exec()
        if reply:
            self.isChooseGameFile = True
            widgets.GameComboBox.addItem(f'{name}')

    # 下一页
    def nextPage(self):
        if self.isChooseGameFile:
            widgets.StackedWidget.setCurrentIndex(1)
        else:
            print('please choose game file first')


    # 切换游戏
    def swithGame(self):
        if widgets.GameComboBox.currentIndex() == 0:
            self.isChooseGameFile = False
        else:
            self.isChooseGameFile = True
        pass

# endregion



#region startPage相关函数

    # 打开文件夹选择对话框
    def openFolderDialog(self):
        folderDialog = CFileDialog('文件夹',CFileDialog.DialogMode.Folder, self)
        reply, name, path = folderDialog.exec()
        if reply:
            self.addFolderBtn(name, path)


    # 添加按钮
    def addFolderBtn(self, name: str, path: str):
        # 计算新按钮应该放置的位置
        row = self.ui.FolderGridLayout.count() // self.colLimit
        col = self.ui.FolderGridLayout.count() % self.colLimit
        newBtn = CButton(name, path, self)
        item ={(row, col):{'name':name, 'obj':newBtn, 'path':path}}
        self.btnData.buttons.update(item)
        widgets.FolderGridLayout.addWidget(newBtn, row, col)


    # 切换模式
    def toggleMode(self):
        self.isEditMode = not self.isEditMode
        btns = self.btnData.getAllBtns()
        if self.isEditMode:
            # 将所有存在的按钮改为checkable状态
            widgets.ButtonSelectAll.setVisible(True)
            widgets.ButtonSelectAll.setChecked(True)
            self.btnData.toggleCheckable(btns)
            print('is edit mode')
        else:
            widgets.ButtonSelectAll.setVisible(False)
            widgets.ButtonSelectAll.setChecked(False)
            self.btnData.toggleCheckable(btns)
            print('not edit mode')


    # 全选按钮
    def selectAllBtns(self):
        if not self.isEditMode: return
        btns = self.btnData.getAllBtns()
        if widgets.ButtonSelectAll.isChecked():
            self.btnData.setCheckedAll(btns, False)
        else:
            self.btnData.setCheckedAll(btns, True)


    # 删除选中的按钮
    def removeSelectedButtons(self):
        if self.isEditMode:
            coods,btns = self.btnData.getSelectedCoodAndBtn()
            self.btnData.delSelectedBtns(btns,self.colLimit)
            self.updateBtns(coods)


    # 更新按钮(删除多个)
    def updateBtns(self, coods: list):
        while coods:
            self.updateBtnForDelOne(coods[0][0], coods[0][1])
            coods = self.updateCoods(coods)
        # region
        # self.updateBtnForDelOne(coods[0][0], coods[0][1])
        # coods = self.updateCoods(coods)
        # if len(coods) != 0:
        #     return self.updateBtns(coods)
        # endregion


    # 更新需要删除的坐标
    def updateCoods(self, coods: list):
        """_summary_ 更新需要删除的坐标

        Args:
            coods (list): _description_ 需要删除的坐标

        Returns:
            _type_: _description_ 返回新的需要删除的坐标
        """        
        for i in range(len(coods)):
            cood = coods[i]
            # 如果需要删除的坐标为 (Row, 0)，则将位置更新到上一行
            if cood[1] == 0: coods[i] = (cood[0] - 1, self.colLimit - 1)
            # 如果需要删除的坐标为 (Row, Col)，则将位置更新到上一列
            else: coods[i] = (cood[0], cood[1] - 1)
        coods.pop(0)
        return coods


    #从指定位置更新按钮，不考虑下一个位置的布局中是否有控件
    def updateBtnForDelOne(self, row: int, col: int):
        """_summary_ 根据删除一个按钮更新按钮

        Args:
            row (int): _description_ 当前按钮的行
            col (int): _description_ 当前按钮的列

        Returns:
            _type_: _description_ 递归|是否完成更新
        """        
        # 如果传入的位置在最后一列
        if col == self.colLimit - 1:
            if not self.moveBtnToPreviousRow(row, col):
                return self.updateBtnForDelOne(row + 1, 0)
        # 传入位置不在最后一列
        if not self.moveBtnToPreviousCol(row, col):
            return self.updateBtnForDelOne(row, col + 1)




    # 根据坐标移动按钮
    def moveBtnWithCood(self, cood: tuple[int, int], targetCood: tuple[int, int]):
        """_summary_ 根据坐标移动按钮

        Args:
            cood (tuple[int, int]): _description_ 当前按钮的坐标
            targetCood (tuple[int, int]): _description_ 目标按钮的坐标
        """
        # 获取指定位置的控件
        item = widgets.FolderGridLayout.itemAtPosition(targetCood[0], targetCood[1])
        if item is None:
            return
        # 将控件移动到第一个空位
        widgets.FolderGridLayout.addWidget(item.widget(), cood[0], cood[1])


    # 根据索引移动按钮
    def moveBtnWithIndex(self, cood: tuple[int, int], targetCood: tuple[int, int]):
        """_summary_ 根据索引移动按钮

        Args:
            cood (tuple[int, int]): _description_ 当前按钮的坐标
            targetCood (tuple[int, int]): _description_ 目标按钮的坐标
        """        
        # 获取指定位置的控件
        item = widgets.FolderGridLayout.itemAtPosition(targetCood[0], targetCood[1])
        if item is None:
            return
        # 将控件移动到第一个空位
        widgets.FolderGridLayout.addWidget(item.widget(), cood[0], cood[1])


    # 将按钮移动到上一行
    def moveBtnToPreviousRow(self, row: int, col: int):
        """_summary_  将按钮移动到上一行

        Args:
            row (int): _description_ 行
            col (int): _description_ 列

        Returns:
            _type_: _description_ 如果下一行没有布局则返回 true,已经执行完所有移动,
            或者下一行布局中没有控件则返回 true,则执行完一个按钮被删除的更新
        """
        item = widgets.FolderGridLayout.itemAtPosition(row + 1, 0)
        #如果下一行没有布局则返回 true，已经执行完所有移动
        if item is None: return True
        #如果下一行布局中没有控件则返回 true，则执行完一个按钮被删除的更新
        if item.widget() is None: return True
        widgets.FolderGridLayout.addWidget(item.widget(), row, col)


    # 将按钮向左移动
    def moveBtnToPreviousCol(self, row: int, col: int):
        """_summary_ 将按钮向左移动

        Args:
            row (int): _description_ 行
            col (int): _description_ 列

        Returns:
            _type_: _description_ 如果下一列没有布局则返回 true,已经执行完所有移动，
            或者下一列布局中没有控件则返回 true,则执行完一个按钮被删除的更新
        """                
        item = widgets.FolderGridLayout.itemAtPosition(row, col + 1)
        #如果下一列没有布局则返回 true，已经执行完所有移动
        if item is None: return True
        #如果下一列布局中没有控件则返回 true，则执行完一个按钮被删除的更新
        if item.widget() is None: return True
        widgets.FolderGridLayout.addWidget(item.widget(), row, col)


    # 获取第一个空位的坐标
    def getFirstEmptyRowAndCol(self):
        """_summary_ 获取第一个空位的坐标

        Returns:
            _type_: _description_ 第一个空位的坐标
        """        
        for i in range(widgets.FolderGridLayout.count()):
            item = widgets.FolderGridLayout.itemAtPosition(i // self.colLimit, i % self.colLimit)
            if item is None: return i // self.colLimit, i % self.colLimit
            if item.widget() is None: return i // self.colLimit, i % self.colLimit
        return -1

    # 获取第一个空位的索引
    def getFirstEmptyIndex(self):
        """_summary_ 获取第一个空位的索引

        Returns:
            _type_: _description_ 第一个空位的索引
        """       
        for i in range(widgets.FolderGridLayout.count()):
            item = widgets.FolderGridLayout.itemAt(i)
            if item is None: return i
            if item.widget() is None: return i
        return -1

# endregion

# region aboutpage 相关函数

    # 打开github
    def goToMyGithub(self):
        GenericFunc.openWeb('https://github.com/ichinoseyuu')

    # 清除所有数据
    def removeUserdata(self):
        pass

    # 检查更新
    def checkUpdate(self):
        pass


# endregion
    def mousePressEvent(self, event):
        GenericFunc.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        GenericFunc.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        GenericFunc.mouseReleaseEvent(self, event)

    def paintEvent(self, event):
        GenericFunc.paintShadow(self)


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

    #region
    # 旧的退出方法
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