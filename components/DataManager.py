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
        if UserData.settings.value('current_game') is None:
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


    def saveFolder(game: str, folders: dict):
        """_summary_ 保存文件夹

        Args:
            game (str): _description_ 游戏名称
            folders (dict): _description_ 文件夹数据
        """
        #region 保存文件夹
        for cood, data in folders.items():
            UserData.games[game]['folders'].update({
                data['name']:{
                    'cood': {
                        'row': cood[0],
                        'col': cood[1]
                    },
                    'path': data['path']
                }
            })
        #endregion


    def addFolder(game: str,folderName: str, path: str, row: int, col: int):
        """_summary_ 添加文件夹

        Args:
            game (str): _description_ 游戏名称
            folderName (str): _description_ 文件夹名称
            path (str): _description_ 文件夹路径
            row (int): _description_ 行号
            col (int): _description_ 列号
        """
        #region 添加文件夹
        UserData.games[game]['folders'].update({
            folderName:{
                'cood': {
                    'row': row,
                    'col': col
                },
                'path': path
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


    def __init__(self):
        self.buttons = {}


    def getAllBtns(self):
        """_summary_ 获取所有按钮

        Returns:
            _type_: _description_ 返回一个list，包含所有按钮
        """
        #region 获取所有按钮
        #.values()只获取键值，不获取键，返回一个list
        #.items()获取键值对，返回一个dict
        key = self.Keys.ObjKey
        return [value[key] for value in self.buttons.values()]
        #endregion


    def getSelectedBtnsWithCood(self) -> dict:
        """_summary_ 获取选中的按钮和坐标

        Returns:
            dict: _description_ 返回一个字典，键是坐标，值是按钮
        """
        #region 获取选中的按钮和坐标
        key = self.Keys.ObjKey
        data = {}
        for cood, item in self.buttons.items():
            if key in item and item[key].isChecked():
                data.update({cood: item[key]})
        return data
        #endregion


    def getSelectedCoodAndBtn(self):
        """_summary_ 获取选中的按钮和坐标

        Returns:
            _type_: _description_ 返回一个元组，第一个元素是坐标，第二个元素是按钮
        """
        #region 获取选中的按钮和坐标
        key = self.Keys.ObjKey
        btns = []
        coods = []
        for cood, item in self.buttons.items():
            if key in item and item[key].isChecked():
                btns.append(item[key])
                coods.append(cood)
        return coods, btns
        #endregion


    def getSelectedBtns(self) -> list:
        """_summary_ 获取选中的按钮

        Returns:
            list: _description_ 选中的按钮
        """        
        #region 获取选中的按钮
        key = self.Keys.ObjKey
        btns = []
        for value in self.buttons.values():
            if key in value and value[key].isChecked():
                btns.append(value[key])
        return btns
        #endregion


    def delSelectedBtn(self, btn, colLimit):
        """_summary_ 删除一个按钮

        Args:
            btn (_type_): _description_ 需要删除的按钮
            colLimit (_type_): _description_ 每行按钮的数量
        """      
        #region 删除选中的按钮
        key = self.Keys.ObjKey
        # 查找并删除对应的按钮
        for cood, value in list(self.buttons.items()):  # 使用 list() 来避免修改字典时出错
            if key in value and value[key] == btn:
                value[key].deleteLater()# 删除按钮的GUI对象
                del self.buttons[cood]    # 删除字典中的该键值对       
        newButtons = {}
        # 遍历字典的剩余元素，重新编号键
        for i, (cood, item) in enumerate(self.buttons.items()):
            # 重新生成键，按顺序重新编号为 (i // colCount, i % colCount) 的形式
            newKey = (i // colLimit, i % colLimit)
            newButtons[newKey] = item
        self.buttons = newButtons
        #endregion


    def removeAllBtns(self):
        """_summary_ 去除所有按钮的显示
        """
        #region 去除所有按钮的显示
        key = self.Keys.ObjKey
        btns = [value[key] for value in self.buttons.values()]
        for btn in btns:
            btn.deleteLater()# 删除按钮的GUI对象
        self.buttons.clear()    # 清空字典
        #endregion


    def delSelectedBtns(self, btns: list, colLimit: int):
        """_summary_ 删除多个按钮

        Args:
            btns (list): _description_ 需要删除的按钮
            colLimit (int): _description_ 每行按钮的数量
        """     
        #region 删除选中的按钮
        key = self.Keys.ObjKey
        for btn in btns:
            # 查找并删除对应的按钮
            for cood, value in list(self.buttons.items()):  # 使用 list() 来避免修改字典时出错
                if key in value and value[key] == btn:
                    value[key].deleteLater()# 删除按钮的GUI对象
                    del self.buttons[cood]    # 删除字典中的该键值对       
        newButtons = {}
        # 遍历字典的剩余元素，重新编号键
        for i, (cood, item) in enumerate(self.buttons.items()):
            # 重新生成键，按顺序重新编号为 (i // colCount, i % colCount) 的形式
            newKey = (i // colLimit, i % colLimit)
            newButtons[newKey] = item
        self.buttons = newButtons
        #endregion



    def toggleCheckable(self, btns: list):
        """_summary_ 改变按钮是否看选择的状态

        Args:
            btns (list): _description_ 需要改变状态的按钮
        """
        #region 改变按钮是否看选择的状态 
        if not btns: return
        for btn in btns:
            btn.setCheckable(not btn.isCheckable())
        #endregion

    def setCheckedAll(self, btns: list, state: bool):
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


    def printBtns(self):
        # for key, value in self.buttons.items():
        #     print(key,'name:', value['name'], 'path:', value['path'])
        print(self.buttons)
    

class StyleManager:
    btnStyle = GenericFunc.loadFile('./qss/other/button.qss')