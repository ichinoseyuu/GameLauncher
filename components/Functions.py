import math, webbrowser
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from main import *

class GenericFunc():
    
    def loadFile(filePath: str):
        with open(filePath, 'r', encoding='utf-8') as file:
            return file.read()


    def openWeb(webUrl: str):
        webbrowser.open(webUrl)


    def calculateGlobalCenterPos(geometry,parentGeometry) :
        #region 计算全局中心位置
        x = parentGeometry.left()+ parentGeometry.width()/2-geometry.width()/2
        y = parentGeometry.top()+parentGeometry.height()/2-geometry.height()/2
        return QRect(x, y, geometry.width(), geometry.height())
        #endregion

    def calculateLocalCenterPos(geometry,parentGeometry) :
        #region 计算父窗口中心位置
        x = parentGeometry.width()/2-geometry.width()/2
        y = parentGeometry.height()/2-geometry.height()/2
        return QRect(x, y, geometry.width(), geometry.height())


    def mousePressEvent(obj, event):
        #region 记录鼠标按下时的位置
        if event.buttons() == Qt.LeftButton:
            obj.old_pos = event.globalPosition().toPoint()
        #endregion


    def mouseMoveEvent(obj, event):
        #region 移动窗口
        if not hasattr(obj, 'old_pos'):  # 如果 obj 没有 old_pos 属性，初始化
            obj.old_pos = None
        if obj.old_pos is not None and event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - obj.old_pos  # 计算位置变化
            obj.move(obj.x() + delta.x(), obj.y() + delta.y())  # 移动窗口
            obj.old_pos = event.globalPosition().toPoint()  # 更新旧位置
        #endregion

    def mouseReleaseEvent(obj, event):
        #region 释放鼠标时重置旧位置
        if event.button() == Qt.LeftButton:
            obj.old_pos = None  # 释放鼠标时重置旧位置
        #endregion


    def paintShadow(obj):
        #region 绘制窗口阴影
        m = 9  # 初始偏移量
        # 创建绘制器
        painter = QPainter(obj)
        painter.setRenderHint(QPainter.Antialiasing, True)  # 设置抗锯齿
        # 设置初始颜色
        color = QColor(140, 140, 140, 30)
        # 循环绘制多个渐变阴影圆角矩形
        for i in range(m):
            # 设置透明度，随着i增大逐渐变透明
            alpha = 90 - math.sqrt(i) * 30
            color.setAlpha(max(alpha, 0))  # 确保透明度不会小于0
            painter.setPen(QPen(color, 1, Qt.SolidLine)) # 设置笔刷颜色和线宽
            # 绘制圆角矩形
            painter.drawRoundedRect(QRect(m - i, m - i, obj.width() - (m - i) * 2, obj.height() - (m - i) * 2), 0, 0)
        painter.end()
        #endregion

