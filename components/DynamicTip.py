import enum
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint,QTimer,QRect,QSize
from PySide6.QtGui import QMouseEvent,QCursor
from .Ui_DynamicTip import Ui_DynamicTip
from .Functions import GenericFunc

class CDynamicTip(QWidget, Ui_DynamicTip):
    class PosMode(enum.Enum):
        Center = 0
        Left = 1
        Right = 2
    def __init__(self, tip: str, posMode: PosMode = PosMode.Center,parent=None):
        super(CDynamicTip, self).__init__()
        self.parent = parent
        self.positionMode = posMode
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #设置提示文字
        self.TipLabel.setText(tip)

        # 自动调整窗口大小
        self.adjustSize()

        # 计算窗口位置
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self.parent.geometry()))

        # 设置动画
        self.moveAnimIn = QPropertyAnimation(self, b"pos")
        self.moveAnimIn.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.moveAnimIn.setDuration(1000)

        self.moveAnimOut = QPropertyAnimation(self, b"pos")
        self.moveAnimOut.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.moveAnimOut.setDuration(500)

        self.fadeAnim = QPropertyAnimation(self, b"windowOpacity")
        self.fadeAnim.setDuration(500)
        self.fadeAnim.setStartValue(1)
        self.fadeAnim.setEndValue(0)

        # 设置定时器，3秒后关闭窗口
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fadeOut)
        self.timer.start(1500)

        self.show()
        self.animIn()


    def animIn(self):
        if self.positionMode == CDynamicTip.PosMode.Center:
            self.moveAnimIn.setStartValue(QPoint(self.x(), self.y() + 150))# 起始位置
            self.moveAnimIn.setEndValue(self.pos())  # 结束位置，往上移动50像素
            self.moveAnimIn.start()
        elif self.positionMode == CDynamicTip.PosMode.Right:
            x = self.parent.geometry().right()-self.width()
            self.moveAnimIn.setStartValue(QPoint(x,self.y() + 150))  # 起始位置
            self.moveAnimIn.setEndValue(QPoint(x, self.y()))  # 结束位置，往上移动50像素
            self.moveAnimIn.start()
        elif self.positionMode == CDynamicTip.PosMode.Left:
            x = self.parent.geometry().left()
            self.moveAnimIn.setStartValue(QPoint(x,self.y() + 150))  # 起始位置
            self.moveAnimIn.setEndValue(QPoint(x, self.y()))  # 结束位置，往上移动50像素
            self.moveAnimIn.start()

    def fadeOut(self):
        self.fadeAnim.start()
        self.fadeAnim.finished.connect(self.deleteLater)

    def fadeOutPress(self):
        if self.positionMode == CDynamicTip.PosMode.Center:
            self.fadeAnim.start()
            self.fadeAnim.finished.connect(self.deleteLater)

        elif self.positionMode == CDynamicTip.PosMode.Right:
            self.moveAnimOut.setStartValue(self.pos())  # 起始位置
            self.moveAnimOut.setEndValue(QPoint(self.x()+50, self.y()))
            self.fadeAnim.finished.connect(self.deleteLater)
            self.fadeAnim.start()
            self.moveAnimOut.start()

        elif self.positionMode == CDynamicTip.PosMode.Left:
            self.moveAnimOut.setDuration(1000)
            self.moveAnimOut.setStartValue(self.pos())  # 起始位置
            self.moveAnimOut.setEndValue(QPoint(self.x()+50, self.y()))
            self.fadeAnim.finished.connect(self.deleteLater)
            self.fadeAnim.start()
            self.moveAnimOut.start()


    def mousePressEvent(self, event):
        if self.positionMode == CDynamicTip.PosMode.Center:
            self.fadeOutPress()
        elif self.positionMode == CDynamicTip.PosMode.Right:
            self.fadeOutPress()
        elif self.positionMode == CDynamicTip.PosMode.Left:
            self.fadeOutPress()
        return super().mousePressEvent(event)




class CToolTip(QWidget, Ui_DynamicTip):
    def __init__(self):
        super().__init__()
        self.parent = None
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._init_Anim()

    def _init_Anim(self):
        self.anim_fade_in = QPropertyAnimation(self, b"windowOpacity")
        self.anim_fade_in.setDuration(200)
        self.anim_fade_in.setStartValue(0)
        self.anim_fade_in.setEndValue(1)

        self.anim_fade_out = QPropertyAnimation(self, b"windowOpacity")
        self.anim_fade_out.setDuration(200)
        self.anim_fade_out.setStartValue(1)
        self.anim_fade_out.setEndValue(0)

        self.anim_resize = QPropertyAnimation(self, b"size")
        self.anim_resize.setDuration(200)

        self.tracker_timer = QTimer()  # 跟踪鼠标的计时器
        self.tracker_timer.setInterval(int(1000/60))
        self.tracker_timer.timeout.connect(self.refreshPos)
        self.tracker_timer.start()


    def setTip(self, parent, tip: str):
        self.parent = parent
        self.TipLabel.setText(tip)


    def showTip(self):
        self.adjust_size()
        self.anim_fade_in.start()
        self.show()


    def hideTip(self):
        self.anim_fade_out.finished.connect(self.close)
        self.anim_fade_out.start()


    def adjust_size(self):
        """根据控件内容调整大小"""
        # 获取推荐的大小
        recommended_size = self.sizeHint()
        # 获取最小尺寸
        min_width = self.minimumWidth()
        min_height = self.minimumHeight()
        # 设置新尺寸，确保不小于最小尺寸
        new_width = max(recommended_size.width() + 36, min_width)
        new_height = max(recommended_size.height(), min_height)
        # 调整大小
        
        self.anim_resize.setStartValue(QSize(self.width(), self.height()))
        self.anim_resize.setEndValue(QSize(new_width, new_height))
        self.anim_resize.start()

    def refreshPos(self):
        pos = QCursor.pos()
        x, y = pos.x(), pos.y()
        self.move(x-19, y-self.geometry().height())

    def sizeHint(self):
        """返回推荐的尺寸"""
        # 使用标签的尺寸作为基础
        return self.TipBoard.sizeHint()