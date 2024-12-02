# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 318)
        Dialog.setMaximumSize(QSize(418, 318))
        self.StyleSheet = QWidget(Dialog)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setGeometry(QRect(0, 0, 418, 318))
        self.StyleSheet.setMinimumSize(QSize(418, 318))
        self.StyleSheet.setMaximumSize(QSize(418, 318))
        self.StyleSheet.setStyleSheet(u"#TitleWidget {\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"\n"
"#Title {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 11pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#TitleWidget QPushButton {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#TitleWidget QPushButton:hover {\n"
"    background-color: gainsboro;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#TitleWidget QPushButton:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/*=========================*/\n"
"\n"
"#DialogWidget {\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"#ButtonChooseFolder{\n"
"    background-color: rgb(235, 235, 235);\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: rgb(80, 80, 80);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonChooseFolder:hover {\n"
"    background-color: gainsboro;\n"
"    border-ra"
                        "dius: 2px;\n"
"}\n"
"\n"
"#ButtonChooseFolder:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#PathLineEdit {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    border: 1px solid gainsboro;\n"
"	border-radius: 2px;\n"
"    background-color: transparent;\n"
"    color: dimgray;\n"
"}\n"
"\n"
"#NameLineEdit {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 10pt;\n"
"    border: 1px solid gainsboro;\n"
"	border-radius: 2px;\n"
"    background-color: transparent;\n"
"    color: dimgray;\n"
"}\n"
"\n"
"/*=========================*/\n"
"#DefaultWidget {\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"#ButtonCancel{\n"
"    background-color: rgb(235, 235, 235);\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: rgb(80, 80, 80);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonCancel:hover {\n"
"    background-color: gainsboro;\n"
"    border-radi"
                        "us: 2px;\n"
"}\n"
"\n"
"#ButtonCancel:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonOk {\n"
"    background-color: rgb(208, 178, 224);\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonOk:hover {\n"
"    background-color: rgb(197, 172, 227);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonOk:pressed {\n"
"    background-color: rgb(181, 164, 232);\n"
"    border-radius: 2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.StyleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.TitleWidget = QWidget(self.StyleSheet)
        self.TitleWidget.setObjectName(u"TitleWidget")
        self.TitleWidget.setMinimumSize(QSize(400, 40))
        self.TitleWidget.setMaximumSize(QSize(400, 40))
        self.horizontalLayout = QHBoxLayout(self.TitleWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = QLabel(self.TitleWidget)
        self.Title.setObjectName(u"Title")
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.Title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ButtonExit = QPushButton(self.TitleWidget)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setMinimumSize(QSize(24, 24))
        self.ButtonExit.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/btn/title_bar/shutdown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonExit.setIcon(icon)

        self.horizontalLayout.addWidget(self.ButtonExit)


        self.verticalLayout.addWidget(self.TitleWidget)

        self.DialogWidget = QWidget(self.StyleSheet)
        self.DialogWidget.setObjectName(u"DialogWidget")
        self.DialogWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.NameLineEdit = QLineEdit(self.DialogWidget)
        self.NameLineEdit.setObjectName(u"NameLineEdit")
        self.NameLineEdit.setGeometry(QRect(9, 110, 381, 32))
        self.NameLineEdit.setMinimumSize(QSize(0, 32))
        self.NameLineEdit.setMaximumSize(QSize(16777215, 32))
        self.PathLineEdit = QLineEdit(self.DialogWidget)
        self.PathLineEdit.setObjectName(u"PathLineEdit")
        self.PathLineEdit.setGeometry(QRect(9, 50, 341, 32))
        self.PathLineEdit.setMinimumSize(QSize(0, 32))
        self.PathLineEdit.setMaximumSize(QSize(16777215, 32))
        self.PathLineEdit.setReadOnly(True)
        self.ButtonChooseFolder = QPushButton(self.DialogWidget)
        self.ButtonChooseFolder.setObjectName(u"ButtonChooseFolder")
        self.ButtonChooseFolder.setGeometry(QRect(360, 50, 32, 32))
        self.ButtonChooseFolder.setMinimumSize(QSize(32, 32))
        self.ButtonChooseFolder.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/btn/main_widget/file.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonChooseFolder.setIcon(icon1)
        self.ButtonChooseFolder.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.DialogWidget)

        self.DefaultWidget = QWidget(self.StyleSheet)
        self.DefaultWidget.setObjectName(u"DefaultWidget")
        self.DefaultWidget.setMinimumSize(QSize(400, 50))
        self.DefaultWidget.setMaximumSize(QSize(400, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.DefaultWidget)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.ButtonOk = QPushButton(self.DefaultWidget)
        self.ButtonOk.setObjectName(u"ButtonOk")
        self.ButtonOk.setMinimumSize(QSize(60, 32))
        self.ButtonOk.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.ButtonOk)

        self.ButtonCancel = QPushButton(self.DefaultWidget)
        self.ButtonCancel.setObjectName(u"ButtonCancel")
        self.ButtonCancel.setMinimumSize(QSize(60, 32))
        self.ButtonCancel.setMaximumSize(QSize(60, 32))

        self.horizontalLayout_2.addWidget(self.ButtonCancel)


        self.verticalLayout.addWidget(self.DefaultWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.Title.setText(QCoreApplication.translate("Dialog", u"\u6807\u9898", None))
#if QT_CONFIG(tooltip)
        self.ButtonExit.setToolTip(QCoreApplication.translate("Dialog", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.NameLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u540d\u79f0", None))
        self.PathLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u9009\u62e9\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.ButtonChooseFolder.setToolTip(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonChooseFolder.setText("")
        self.ButtonOk.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.ButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        pass
    # retranslateUi

