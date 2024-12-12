import enum, json, os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *
class UserData():
    # HKEY_CURRENT_USER\Software\ichinoseyuu\GameLauncher
    settings = QSettings("ichinoseyuu", "GameLauncher")
    dataFile = './data/data.json'
    games = {}

    def init():
        #region 初始化
        UserData.settings.setValue('version', '1.0.0')
        if UserData.settings.value('theme') is None:
            UserData.settings.setValue('theme', 'light')
        if (UserData.settings.value('current_game') == None) | (UserData.settings.value('current_game') == ''):
            UserData.settings.setValue('current_game', 'none')
        dataDir = os.path.dirname(UserData.dataFile)
        # 确保 Data 文件夹存在
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        #endregion


    def saveJson():   
        #region 保存json文件
        dataDir = os.path.dirname(UserData.dataFile)
        # 确保 Data 文件夹存在
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        with open(UserData.dataFile, 'w') as jsonFile:
            json.dump(UserData.games, jsonFile, indent=4)
        #endregion


    def loadJson():
        #region 加载json文件
        # 检查 Data 文件是否存在，如果不存在则跳过
        if not os.path.exists(UserData.dataFile): return
        with open(UserData.dataFile, 'r') as jsonFile:
            UserData.games = json.load(jsonFile)
        #endregion


    def addGame(game: str, path: str):
        """_summary_ 添加游戏

        Args:
            game (str): _description_ 游戏名称
            path (str): _description_ 游戏路径
        """
        #region 添加游戏
        index = len(UserData.games)
        UserData.games.update({
            game:{
                'index': index,
                'path': path,
                'folders': {}
            }
        })
        #endregion


    def isNewGame(game: str):
        """_summary_ 判断是否是新游戏

        Args:
            game (str): _description_ 游戏名称

        Returns:
            _type_: _description_ 如果游戏不存在,返回True,否则返回False
        """        
        return game not in UserData.games


class ButtonManager():
    class Keys(enum.StrEnum):
        NameKey = 'name'
        ObjKey = 'obj'
        PathKey = 'path'

    buttons = {}

    def getAllBtns():
        """_summary_ 获取所有按钮

        Returns:
            _type_: _description_ 返回一个list，包含所有按钮
        """
        #region 获取所有按钮
        #.values()只获取键值，不获取键，返回一个list
        #.items()获取键值对，返回一个dict
        key = ButtonManager.Keys.ObjKey
        return [value[key] for value in ButtonManager.buttons.values()]
        #endregion


    def getSelectedBtnsWithCood() -> dict:
        """_summary_ 获取选中的按钮和坐标

        Returns:
            dict: _description_ 返回一个字典，键是坐标，值是按钮
        """
        #region 获取选中的按钮和坐标
        key = ButtonManager.Keys.ObjKey
        data = {}
        for cood, item in ButtonManager.buttons.items():
            if key in item and item[key].isChecked():
                data.update({cood: item[key]})
        return data
        #endregion


    def getSelectedCoodAndBtn():
        """_summary_ 获取选中的按钮和坐标

        Returns:
            _type_: _description_ 返回一个元组，第一个元素是坐标，第二个元素是按钮
        """
        #region 获取选中的按钮和坐标
        key = ButtonManager.Keys.ObjKey
        btns = []
        coods = []
        for cood, item in ButtonManager.buttons.items():
            if key in item and item[key].isChecked():
                btns.append(item[key])
                coods.append(cood)
        return coods, btns
        #endregion


    def getSelectedBtns() -> list:
        """_summary_ 获取选中的按钮

        Returns:
            list: _description_ 选中的按钮
        """        
        #region 获取选中的按钮
        key = ButtonManager.Keys.ObjKey
        btns = []
        for value in ButtonManager.buttons.values():
            if key in value and value[key].isChecked():
                btns.append(value[key])
        return btns
        #endregion


    def delSelectedBtn(btn, colLimit):
        """_summary_ 删除一个按钮

        Args:
            btn (_type_): _description_ 需要删除的按钮
            colLimit (_type_): _description_ 每行按钮的数量
        """      
        #region 删除选中的按钮
        key = ButtonManager.Keys.ObjKey
        # 查找并删除对应的按钮
        for cood, value in list(ButtonManager.buttons.items()):  # 使用 list() 来避免修改字典时出错
            if key in value and value[key] == btn:
                value[key].deleteLater()# 删除按钮的GUI对象
                del ButtonManager.buttons[cood]    # 删除字典中的该键值对       
        newButtons = {}
        # 遍历字典的剩余元素，重新编号键
        for i, (cood, item) in enumerate(ButtonManager.buttons.items()):
            # 重新生成键，按顺序重新编号为 (i // colCount, i % colCount) 的形式
            newKey = (i // colLimit, i % colLimit)
            newButtons[newKey] = item
        ButtonManager.buttons = newButtons
        print(ButtonManager.buttons)
        #endregion


    def removeAllBtns():
        """_summary_ 去除所有按钮的显示
        """
        #region 去除所有按钮的显示
        key = ButtonManager.Keys.ObjKey
        btns = [value[key] for value in ButtonManager.buttons.values()]
        for btn in btns:
            btn.deleteLater()# 删除按钮的GUI对象
        ButtonManager.buttons.clear()    # 清空字典
        #endregion


    def delSelectedBtns(btns: list, colLimit: int):
        """_summary_ 删除多个按钮

        Args:
            btns (list): _description_ 需要删除的按钮
            colLimit (int): _description_ 每行按钮的数量
        """     
        #region 删除选中的按钮
        key = ButtonManager.Keys.ObjKey
        for btn in btns:
            # 查找并删除对应的按钮
            for cood, value in list(ButtonManager.buttons.items()):  # 使用 list() 来避免修改字典时出错
                if key in value and value[key] == btn:
                    value[key].deleteLater()# 删除按钮的GUI对象
                    del ButtonManager.buttons[cood]    # 删除字典中的该键值对       
        newButtons = {}
        # 遍历字典的剩余元素，重新编号键
        for i, (cood, item) in enumerate(ButtonManager.buttons.items()):
            # 重新生成键，按顺序重新编号为 (i // colCount, i % colCount) 的形式
            newKey = (i // colLimit, i % colLimit)
            newButtons[newKey] = item
        ButtonManager.buttons = newButtons
        print(ButtonManager.buttons)
        #endregion


    def toggleCheckable(btns: list):
        """_summary_ 改变按钮是否看选择的状态

        Args:
            btns (list): _description_ 需要改变状态的按钮
        """
        #region 改变按钮是否看选择的状态 
        if not btns: return
        for btn in btns:
            btn.setCheckable(not btn.isCheckable())
        #endregion


    def setCheckedAll(btns: list, state: bool):
        """_summary_ 改变按钮是否点击的状态

        Args:
            btns (list): _description_ 需要改变状态的按钮
            state (bool): _description_ 需要改变的状态
        """        
        #region 改变按钮是否点击的状态
        if not btns: return
        for btn in btns:
            btn.setChecked(state)
        #endregion

    def saveBtns(currentGame: str):
        """_summary_ 保存按钮信息

        Args:
            currentGame (str): _description_ 当前游戏名
        """
        #region 保存按钮信息
        if currentGame in UserData.games:
            newFolder = {}
            for key, value in ButtonManager.buttons.items():
                newFolder.update({
                    value['name']:{
                        'cood': {
                            'row':key[0],
                            'col':key[1]
                        },
                        'path': value['path'],
                    }
                })
            UserData.games[currentGame]['folders'] = newFolder
        # endregion

    def editBtn(btn, newName: str, newPath: str):
        if btn.cood in ButtonManager.buttons:
            ButtonManager.buttons[btn.cood]['name'] = newName
            ButtonManager.buttons[btn.cood]['path'] = newPath
            btn.setText(newName)
            btn.path = newPath

    def printBtns():
        # for key, value in self.buttons.items():
        #     print(key,'name:', value['name'], 'path:', value['path'])
        print(ButtonManager.buttons)