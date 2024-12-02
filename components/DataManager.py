import enum
from typing import Callable
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class ButtonManager:
    class Keys(enum.StrEnum):
        NameKey = 'name'
        ObjKey = 'obj'
        PathKey = 'path'
    def __init__(self):
        self.buttons = {}
        
    def getAllBtns(self):
        #.values()只获取键值，不获取键，返回一个list
        #.items()获取键值对，返回一个dict
        key = self.Keys.ObjKey
        return [value[key] for value in self.buttons.values()]
    
    def getSelectedBtnsAndCood(self) -> dict:
        #region 获取选中的按钮和坐标
        key = self.Keys.ObjKey
        data = {}
        for cood, item in self.buttons.items():
            if key in item and item[key].isChecked():
                data.update({cood: item[key]})
        return data
        #endregion
    
    def getSelectedBtns(self) -> dict:
        #region 获取选中的按钮
        key = self.Keys.ObjKey
        btns = []
        for value in self.buttons.values():
            if key in value and value[key].isChecked():
                btns.append(value[key])
        return btns
        #endregion
    
    def delSelectedBtns(self, btns: list, obj):
        #region 删除选中的按钮
        key = self.Keys.ObjKey
        for btn in btns:
            # 查找并删除对应的按钮
            for cood, value in list(self.buttons.items()):  # 使用 list() 来避免修改字典时出错
                if key in value and value[key] == btn:
                    value[key].deleteLater()# 删除按钮的GUI对象
                    obj.updateBtns(cood[0], cood[1])  # 更新按钮布局
                    obj.ui.FolderGridLayout.update()
                    del self.buttons[cood]    # 删除字典中的该键值对       
        newButtons = {}
        # 遍历字典的剩余元素，重新编号键
        for i, (cood, item) in enumerate(self.buttons.items()):
            # 重新生成键，按顺序重新编号为 (i // colCount, i % colCount) 的形式
            newKey = (i // obj.colLimit, i % obj.colLimit)
            newButtons[newKey] = item
        self.buttons = newButtons
        #endregion

        
    def toggleCheckable(self, btns: list):
        #region 改变按钮是否看选择的状态 
        if not btns: return
        for btn in btns:
            btn.setCheckable(not btn.isCheckable())
        #endregion

    def toggleChecked(self, btns: dict):
        #region 改变按钮是否点击的状态
        for btn in btns:
            btn.setChecked(not btn.isChecked())
        #endregion
        
    def printBtns(self):
        for key, value in self.buttons.items():
            print(key,'name:', value['name'])
        

class StyleManager:
    def __init__(self):
        self.btnStyle = self.loadStyleData('./qss/other/button.qss')

    def loadStyleData(self, filePath: str):
        with open(filePath, 'r', encoding='utf-8') as file:
            return file.read()
        
    