import enum
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint,QTimer
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

        # 计算窗口位置
        self.setGeometry(GenericFunc.calculateGlobalCenterPos(self.geometry(),self.parent.geometry()))

        #设置提示文字
        self.TipLabel.setText(tip)
        # 自动调整大小
        self.TipLabel.adjustSize()

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
