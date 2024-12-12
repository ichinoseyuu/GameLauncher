from PySide6.QtGui import QColor

class ColorGroup:
    folder_btn_normal_color = QColor(255, 240, 254)
    folder_btn_hover_color = QColor(241, 230, 243)
    folder_btn_pressed_color = QColor(231, 220, 233)
    folder_btn_text_color = QColor(0, 0, 0)
    folder_btn_border = 'none'

class StyleSheet:
    def get_folder_btn_styleSheet(color: QColor):
        # 每次调用时根据当前的颜色重新生成样式表
        return f"""
            CFolderButton {{
                background-color: {color.name()};
                font-family: "微软雅黑";
                font-size: 10pt;
                color: dimgray;
                border-radius: 4px;
                text-align: left;
                padding-left: 10px;
            }}
            CFolderButton:checked {{
                background-color: {color.name()};
                font-family: "微软雅黑";
                font-size: 10pt;
                color: dimgray;
                border-radius: 4px;
                border: 2px solid rgb(217, 204, 255);
                text-align: left;
                padding-left: 10px;
            }}
            CFolderButton::icon {{
                padding-right: 10px;/* 控制图标与文字之间的间距 */
                color: #AAAAAA;
            }}
        """
    def get_menu_styleSheet():
        return '''
        QMenu {
        font: 10pt;
        color: dimgray;
        border-radius: 2px;
        background-color: whitesmoke;
        border: 1px solid lightgray;
        }
        QMenu::item {
            height: auto;
            width: auto;
        }
        QMenu::item:selected {
            background-color: lightgray;
        }
        QMenu::item:disabled {
            color: #AAAAAA;
        }
        '''
class ObjReference:
    obj = {}
