import math
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from main import *

class Func_Main():
    pass


class UtilityFunctions:

    @staticmethod
    def calculatedGeometricPos(geometry,parentGeometry) :
        x = parentGeometry.left()+ parentGeometry.width()/2-geometry.width()/2
        y = parentGeometry.top()+parentGeometry.height()/2-geometry.height()/2
        return QRect(x, y, geometry.width(), geometry.height())

    # 记录鼠标按下时的位置
    @staticmethod
    def mousePressEvent(obj, event):
        if event.buttons() == Qt.LeftButton:
            obj.old_pos = event.globalPosition().toPoint()   

    @staticmethod
    def mouseMoveEvent(obj, event):
        if obj.old_pos is not None and event.buttons() == Qt.LeftButton:
            delta = event.globalPosition().toPoint() - obj.old_pos  # 计算位置变化
            obj.move(obj.x() + delta.x(), obj.y() + delta.y())  # 移动窗口
            obj.old_pos = event.globalPosition().toPoint()  # 更新旧位置

    @staticmethod
    def mouseReleaseEvent(obj, event):
        if event.button() == Qt.LeftButton:
            obj.old_pos = None  # 释放鼠标时重置旧位置

    @staticmethod
    def paintShadow(obj):
        m = 9  # 初始偏移量
        # 创建绘制器
        painter = QPainter(obj)
        painter.setRenderHint(QPainter.Antialiasing, True)  # 设置抗锯齿
        # 设置初始颜色
        color = QColor(100, 100, 100, 30)
        # 循环绘制多个渐变阴影圆角矩形
        for i in range(m):
            # 设置透明度，随着i增大逐渐变透明
            alpha = 90 - math.sqrt(i) * 30
            color.setAlpha(max(alpha, 0))  # 确保透明度不会小于0
            painter.setPen(QPen(color, 1, Qt.SolidLine)) # 设置笔刷颜色和线宽
            # 绘制圆角矩形
            painter.drawRoundedRect(QRect(m - i, m - i, obj.width() - (m - i) * 2, obj.height() - (m - i) * 2), 0, 0)