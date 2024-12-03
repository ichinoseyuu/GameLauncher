from PySide6.QtWidgets import QToolTip
from PySide6.QtCore import Qt

class CToolTip(QToolTip):
    @staticmethod
    def showText(pos, text, widget=None):
        # 你可以在这里自定义工具提示的显示方式
        # 例如，修改工具提示的背景颜色、边框、字体等

        # 设置一个自定义的样式
        custom_style = """
            QToolTip {
                background-color: #333;
                color: white;
                border: 1px solid #444;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
        """
        # 使用样式表来修改工具提示的外观
        QToolTip.setStyleSheet(custom_style)

        # 调用父类的 showText 方法来显示工具提示
        QToolTip.showText(pos, text, widget)