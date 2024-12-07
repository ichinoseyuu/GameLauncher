import sys, os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *


widgets = None
class MainWindow(QMainWindow):
    #region 初始化
    def __init__(self):
        QMainWindow.__init__(self)
        UserData.init() # 初始化用户数据
        UserData.loadJson() # 加载用户数据
        self.btnData = ButtonManager()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 生成界面
        global widgets
        widgets = self.ui

        self.setWindowFlags(Qt.FramelessWindowHint) # 表示窗口没有边框
        self.setAttribute(Qt.WA_TranslucentBackground) # 表示窗口具有透明效果
        widgets.FolderGridLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft) # 设置布局对齐方式

        self.old_pos = None
        self.isEditMode = False # 当前是否在删除模式
        self.colLimit = 5 # 每行最多放5个按钮
        self.isChooseGameFile = False # 是否已经选择游戏文件
        self.currentGame = UserData.settings.value('current_game') # 当前选择的游戏
        if self.currentGame == 'none':
            self.isChooseGameFile = False
        else:
            self.isChooseGameFile = True
            self.loadComboBox() # 加载下拉菜单
            self.loadPic(UserData.games[self.currentGame]['path'], widgets.CurrentGamePic) # 加载游戏图片
            self.loadBtns() # 加载按钮
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
        widgets.ButtonRemoveGame.clicked.connect(self.delGame)
        #主页下拉菜单
        widgets.GameComboBox.currentIndexChanged.connect(self.swithGame)

        #开始页按钮
        widgets.ButtonPlay.clicked.connect(self.playGame)
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
        print(self.currentGame)
        #endregion


# region homePage相关函数

    # 打开游戏选择对话框
    def chooseGameFile(self):
        fileDialog = CFileDialog('游戏','',CFileDialog.DialogMode.File, self)
        reply, name, path = fileDialog.exec()
        if reply == 1:
            self.isChooseGameFile = True
            self.currentGame = name
            widgets.GameComboBox.addItem(f'{name}')
            widgets.GameComboBox.setCurrentText(name)
            UserData.settings.setValue('current_game',name)
            UserData.addGame(name, path)
            self.loadPic(UserData.games[self.currentGame]['path'], widgets.CurrentGamePic) # 加载游戏图片
            self.tip = CDynamicTip(f'成功添加游戏 {name}', CDynamicTip.PosMode.Center, self)

    # 下一页
    def nextPage(self):
        if self.isChooseGameFile:
            widgets.StackedWidget.setCurrentIndex(1)
        else:
            self.tip = CDynamicTip('请先选择游戏文件', CDynamicTip.PosMode.Center, self)


    def loadComboBox(self):
        for game in UserData.games.keys():
            widgets.GameComboBox.addItem(f'{game}')
        widgets.GameComboBox.setCurrentText(self.currentGame)

    # 切换游戏
    def swithGame(self):
        currntGame = widgets.GameComboBox.currentText()
        self.currentGame = currntGame
        self.btnData.removeAllBtns()
        if UserData.isNewGame(currntGame): return
        self.loadPic(UserData.games[self.currentGame]['path'], widgets.CurrentGamePic) # 加载游戏图片
        self.loadBtns()
        self.tip = CDynamicTip(f'切换到游戏 {currntGame}', CDynamicTip.PosMode.Center, self)


    def delGame(self):
        if self.currentGame =='none':
            self.tip = CDynamicTip('你还未添加游戏，无法删除', CDynamicTip.PosMode.Center, self)
            return
        # 删除游戏
        UserData.games.pop(self.currentGame)
        widgets.GameComboBox.removeItem(widgets.GameComboBox.currentIndex())
        
        # 判断下一个游戏
        currntGame = widgets.GameComboBox.currentText()
        # 如果已经删除所有项目，则将currentGame设为'none'
        if widgets.GameComboBox.currentText() == '':
            self.isChooseGameFile = False
            self.currentGame = 'none'
            UserData.settings.setValue('current_game', 'none')
            widgets.CurrentGamePic.clear()
            self.btnData.removeAllBtns()
            return
        # 如果还剩有其他游戏，则切换到其他游戏
        self.currentGame = currntGame
        UserData.settings.setValue('current_game', currntGame)
        self.btnData.removeAllBtns()
        if UserData.isNewGame(currntGame): return
        self.loadPic(UserData.games[self.currentGame]['path'], widgets.CurrentGamePic) # 加载游戏图片
        self.loadBtns()

# endregion


#region startPage相关函数

    # 开始游戏
    def playGame(self):
        if self.isChooseGameFile:
            path = os.startfile(UserData.games[self.currentGame]['path'])
            QProcess.startDetached(f'{path}')
            self.tip = CDynamicTip(f'打开游戏 {self.currentGame}', CDynamicTip.PosMode.Center, self)
        else:
            self.tip = CDynamicTip('请先选择游戏文件', CDynamicTip.PosMode.Center, self)

# endregion


# region folderPage相关函数

    # 打开文件夹选择对话框
    def openFolderDialog(self):
        if not self.isChooseGameFile: 
            self.tip = CDynamicTip('请先选择游戏文件', CDynamicTip.PosMode.Center, self)
            return
        dir = os.path.dirname(UserData.games[self.currentGame]['path'])
        folderDialog = CFileDialog('文件夹',dir,CFileDialog.DialogMode.Folder, self)
        reply, name, path = folderDialog.exec()
        if reply == 1:
            self.addFolderBtn(name, path)
            self.tip = CDynamicTip(f'成功添加文件夹 {name}', CDynamicTip.PosMode.Center, self)



    # 添加按钮
    def addFolderBtn(self, name: str, path: str):
        # 计算新按钮应该放置的位置
        row = self.ui.FolderGridLayout.count() // self.colLimit
        col = self.ui.FolderGridLayout.count() % self.colLimit
        newBtn = CButton(name, path, self)
        item ={(row, col):{'name': name, 'obj': newBtn, 'path': path}}
        self.btnData.buttons.update(item)
        widgets.FolderGridLayout.addWidget(newBtn, row, col)
        UserData.addFolder(self.currentGame, name, path, row, col)


    def loadBtns(self):
        for name, item in UserData.games[self.currentGame]['folders'].items():
            path = item['path']
            row = item['cood']['row']
            col = item['cood']['col']
            newBtn = CButton(name, path, self)
            item ={(row, col):{'name': name, 'obj': newBtn, 'path': path}}
            self.btnData.buttons.update(item)
            widgets.FolderGridLayout.addWidget(newBtn, row, col)


    def loadPic(self, filePath: str, obj: QLabel):
        iconProvider = QFileIconProvider()  # 创建 QFileIconProvider 对象
        fileInfo = QFileInfo(filePath)     # 获取文件路径信息
        icon = iconProvider.icon(fileInfo) # 获取图标
        # 将图标转换为 QPixmap 对象并缩放
        pixmap = icon.pixmap(42, 42).scaled(42, 42, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        obj.setPixmap(pixmap)  # 设置图标到标签中


    # 切换模式
    def toggleMode(self):
        self.isEditMode = not self.isEditMode
        btns = self.btnData.getAllBtns()
        if self.isEditMode:
            # 将所有存在的按钮改为checkable状态
            widgets.ButtonSelectAll.setVisible(True)
            widgets.ButtonSelectAll.setChecked(True)
            self.btnData.toggleCheckable(btns)
            self.tip = CDynamicTip('切换到编辑模式', CDynamicTip.PosMode.Center, self)
            print('is edit mode')
        else:
            widgets.ButtonSelectAll.setVisible(False)
            widgets.ButtonSelectAll.setChecked(False)
            self.btnData.toggleCheckable(btns)
            self.tip = CDynamicTip('已退出编辑模式', CDynamicTip.PosMode.Center, self)
            print('not edit mode')


    # 全选按钮
    def selectAllBtns(self):
        if not self.isEditMode: return
        btns = self.btnData.getAllBtns()
        if widgets.ButtonSelectAll.isChecked():
            self.btnData.setCheckedAll(btns, False)
            self.tip = CDynamicTip('取消全选', CDynamicTip.PosMode.Center, self)
        else:
            self.btnData.setCheckedAll(btns, True)
            self.tip = CDynamicTip('全选', CDynamicTip.PosMode.Center, self)


    # 删除选中的按钮
    def removeSelectedButtons(self):
        if self.isEditMode:
            coods,btns = self.btnData.getSelectedCoodAndBtn()
            self.btnData.delSelectedBtns(btns,self.colLimit)
            self.updateBtns(coods)
            self.tip = CDynamicTip('删除成功', CDynamicTip.PosMode.Center, self)


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
        self.tip = CDynamicTip('跳转到', CDynamicTip.PosMode.Center, self)

    # 清除所有数据
    def removeUserdata(self):
        message = CMessage('清除数据', '您确定要清除所有数据吗？\n清除完成后将会重启程序。', self)
        reply = message.exec()
        if reply == 1:
            UserData.games.clear()
            UserData.settings.setValue('current_game', 'none')
            UserData.settings.setValue('theme', 'light')
            self.btnData.buttons.clear()
            UserData.saveJson()
            widgets.fadeAnim.setStartValue(1)
            widgets.fadeAnim.setEndValue(0)
            widgets.fadeAnim.finished.connect(lambda:QApplication.instance().quit())
            widgets.fadeAnim.start()

    # 检查更新
    def checkUpdate(self):
        self.tip = CDynamicTip('努力中更新中...', CDynamicTip.PosMode.Center, self)
        pass


# endregion
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()



    def mouseMoveEvent(self, event):
        if self.old_pos is not None and event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos  # 计算位置变化
            self.move(self.x() + delta.x(), self.y() + delta.y())  # 移动窗口
            self.old_pos = event.globalPosition().toPoint()  # 更新旧位置


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None  # 释放鼠标时重置旧位置


    def paintEvent(self, event):
        super().paintEvent(event)
        GenericFunc.paintShadow(self)


    def exitApplication(self):
        #region 退出程序
        message = CMessage('退出', '您确定要退出吗？', self)
        reply = message.exec()
        if reply == 1:
            UserData.saveJson()
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