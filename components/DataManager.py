import enum, json, os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from components import *
class UserData():
    userData = {
        'games': {
            0: {
                'name': 'none',
                'path': 'none',
                'folders':{
                    (0,0): {
                        'name': 'none',
                        'path': 'none',
                    }
                }
            },
        },
        'settings': {
            'theme': 'light',
            'cuurent_game': 0,
        }
    }

    def checkDataPathIsExist():
        # 检查文件夹是否存在，如果不存在则创建
        dataDir = os.path.dirname(UserData.appDataFileName)
        # 确保 Data 文件夹存在
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)  # 创建文件夹

        # 检查 appData 文件是否存在，如果不存在则创建, 并初始化
        if not os.path.exists(UserData.appDataFileName):
            with open(UserData.appDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.appDocker, jsonFile, indent=4)

        # 检查 settingsData 文件是否存在，如果不存在则创建, 并初始化
        if not os.path.exists(UserData.settingsDataFileName):
            with open(UserData.settingsDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.settingsData, jsonFile, indent=4)

class ButtonManager():
    class Keys(enum.StrEnum):
        NameKey = 'name'
        ObjKey = 'obj'
        PathKey = 'path'
    def __init__(self):
        self.buttons = {}
        
    def getAllBtns(self):
        #.values()只获取键值，不获取键，返回一个list
        #.items()获取键值对，返回一个dict
        """_summary_ 获取所有按钮

        Returns:
            _type_: _description_ 返回一个list，包含所有按钮
        """        
        key = self.Keys.ObjKey
        return [value[key] for value in self.buttons.values()]
    
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
        for key, value in self.buttons.items():
            print(key,'name:', value['name'])
        

class StyleManager:
    btnStyle = GenericFunc.loadFile('./qss/other/button.qss')
    

    
    
        
    