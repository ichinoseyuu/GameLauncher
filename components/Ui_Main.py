# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1042, 738)
        MainWindow.setMinimumSize(QSize(1042, 738))
        self.StyleSheet = QWidget(MainWindow)
        self.StyleSheet.setObjectName(u"StyleSheet")
        self.StyleSheet.setMinimumSize(QSize(1042, 738))
        self.StyleSheet.setStyleSheet(u"#TitleWidget {\n"
"    border-bottom: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(250, 245, 245);\n"
"}\n"
"\n"
"#Title {\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font: 12pt;\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#Icon{\n"
"	image: url(:/images/icon/icon.png);\n"
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
"\n"
"/*=============================*/\n"
"\n"
"#LeftWidget {\n"
"    border-right: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#LeftWidget QPushButton {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#LeftWidget QPushButton:hover {\n"
"    background-color: gainsboro;\n"
"    border-"
                        "radius: 2px;\n"
"}\n"
"\n"
"#LeftWidget QPushButton:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/*=============================*/\n"
"\n"
"#HomePage {\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#PathSetWidget{\n"
"    background-color: rgb(250, 245, 250);\n"
"}\n"
"\n"
"#HomeLabel{\n"
"	image: url(:/images/back_ground/home_bg.png);\n"
"}\n"
"\n"
"#PathSetLabel{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 12pt;\n"
"	font-weight: bold;\n"
"	color: rgb(60, 60, 60);\n"
"}\n"
"#PathSetWidget QPushButton {\n"
"    background-color: rgb(235, 235, 235);\n"
"	color: rgb(80, 80, 80);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#PathSetWidget QPushButton:hover {\n"
"    background-color: gainsboro;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#PathSetWidget QPushButton:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#PathSetTopWidget{\n"
"    background-color: rgb(250, 245, 250);\n"
"	border-bottom: "
                        "1px solid rgb(235, 235, 235);\n"
"}\n"
"\n"
"#CurrentGameLabel{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: dimgray;\n"
"    border: 1px solid gainsboro;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"/*=============================*/\n"
"#StartPage {\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"#StartPageScrollArea {\n"
"    border: none;\n"
"}\n"
"#StartPageScrollWidget{\n"
"    background: rgb(255, 246, 248);\n"
"}\n"
"#StartPageScrollArea QScrollBar:vertical {\n"
"	width: 6px;\n"
"	margin: 0px 0px 0px 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"#StartPageScrollArea QScrollBar::handle:vertical {\n"
"    background: silver;\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"	width: 6px;\n"
"}\n"
"\n"
"#StartPageScrollArea QScrollBar::add-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"#StartPageScrollArea QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    heig"
                        "ht: 0px;\n"
"}\n"
"\n"
"#StartPageScrollArea QScrollBar::up-arrow:vertical,\n"
"#StartPageScrollArea QScrollBar::down-arrow:vertical { \n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"#FunctionWidget {\n"
"    background: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#FunctionTitleLabel{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 12pt;\n"
"	font-weight: bold;\n"
"	color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#FunctionWidget QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 2px;\n"
"}\n"
"#FunctionWidget QPushButton#ButtonEditFolder:checked {\n"
"    background-color: rgb(230,230,230);\n"
"	border-radius: 2px;\n"
"	border: 1px solid dimgray;\n"
"}\n"
"\n"
"#FunctionWidget QPushButton:hover {\n"
"    background-color: gainsboro;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#FunctionWidget QPushButton:pressed {\n"
"    background-color: lightgray;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#FolderWidget{\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#Botto"
                        "mWidget{\n"
"    background-color: rgb(250, 245, 250);\n"
"}\n"
"\n"
"#ButtonPlay {\n"
"    background-color: rgb(255, 99, 134);\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonPlay:hover {\n"
"    background-color: rgb(240, 90, 125);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#ButtonPlay:pressed {\n"
"    background-color: rgb(230, 80, 110);\n"
"    border-radius: 2px;\n"
"}\n"
"/*=============================*/\n"
"#AboutPage { \n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#AboutPageTitle{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 12pt;\n"
"	font-weight: bold;\n"
"	color: rgb(60, 60, 60);\n"
"}\n"
"\n"
"#AboutPageScrollArea {\n"
"    border: none;\n"
"}\n"
"#AboutPageScrollWidget{\n"
"    background: rgb(255, 246, 248);\n"
"}\n"
"#AboutPageScrollArea QScrollBar:vertical {\n"
"	width: 6px;\n"
"	margin: 0px 0px 0px 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"#A"
                        "boutPageScrollArea QScrollBar::handle:vertical {\n"
"    background: silver;\n"
"    min-height: 20px;\n"
"    border-radius: 2px;\n"
"	width: 6px;\n"
"}\n"
"\n"
"#AboutPageScrollArea QScrollBar::add-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"#AboutPageScrollArea QScrollBar::sub-line:vertical {\n"
"    background: transparent;\n"
"    border: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"#AboutPageScrollArea QScrollBar::up-arrow:vertical,\n"
"#AboutPageScrollArea QScrollBar::down-arrow:vertical { \n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"#SoftwareInfoWidget{\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#SoftwareInfoTitle{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"#SoftwarePic{\n"
"	image: url(:/images/icon/icon.png);\n"
"}\n"
"\n"
"#SoftwareName{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
""
                        "	color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"#SoftwareVersion{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 9pt;\n"
"	color: dimgray;\n"
"}\n"
"\n"
"#DeveloperPic{\n"
"\n"
"}\n"
"\n"
"#DeveloperName{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 10pt;\n"
"	color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"#DeveloperInfo{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 9pt;\n"
"	color: dimgray;\n"
"}\n"
"\n"
"#VersionInfoWidget{\n"
"    background-color: rgb(255, 246, 248);\n"
"}\n"
"\n"
"#VersionInfoTitle{\n"
"	font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: transparent;\n"
"	color: dimgray;\n"
"    border: none;\n"
"}\n"
"/*=============================*/\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.StyleSheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.TitleWidget = QWidget(self.StyleSheet)
        self.TitleWidget.setObjectName(u"TitleWidget")
        self.TitleWidget.setMinimumSize(QSize(0, 40))
        self.TitleWidget.setMaximumSize(QSize(16777215, 40))
        self.hboxLayout = QHBoxLayout(self.TitleWidget)
        self.hboxLayout.setSpacing(15)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(15, 0, 15, 0)
        self.Icon = QLabel(self.TitleWidget)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setMinimumSize(QSize(32, 32))
        self.Icon.setMaximumSize(QSize(32, 32))

        self.hboxLayout.addWidget(self.Icon)

        self.Title = QLabel(self.TitleWidget)
        self.Title.setObjectName(u"Title")

        self.hboxLayout.addWidget(self.Title)

        self.TitleSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.TitleSpacer)

        self.ButtonMin = QPushButton(self.TitleWidget)
        self.ButtonMin.setObjectName(u"ButtonMin")
        self.ButtonMin.setMinimumSize(QSize(24, 24))
        self.ButtonMin.setMaximumSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u":/btn/title_bar/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonMin.setIcon(icon)

        self.hboxLayout.addWidget(self.ButtonMin)

        self.ButtonExit = QPushButton(self.TitleWidget)
        self.ButtonExit.setObjectName(u"ButtonExit")
        self.ButtonExit.setMinimumSize(QSize(24, 24))
        self.ButtonExit.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/btn/title_bar/shutdown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonExit.setIcon(icon1)

        self.hboxLayout.addWidget(self.ButtonExit)


        self.verticalLayout.addWidget(self.TitleWidget)

        self.ContentWidget = QWidget(self.StyleSheet)
        self.ContentWidget.setObjectName(u"ContentWidget")
        self.horizontalLayout = QHBoxLayout(self.ContentWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftWidget = QWidget(self.ContentWidget)
        self.LeftWidget.setObjectName(u"LeftWidget")
        self.LeftWidget.setMinimumSize(QSize(60, 0))
        self.LeftWidget.setMaximumSize(QSize(60, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.LeftWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ButtonHome = QPushButton(self.LeftWidget)
        self.ButtonHome.setObjectName(u"ButtonHome")
        self.ButtonHome.setMinimumSize(QSize(42, 42))
        self.ButtonHome.setMaximumSize(QSize(42, 42))
        icon2 = QIcon()
        icon2.addFile(u":/btn/left_widget/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonHome.setIcon(icon2)
        self.ButtonHome.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.ButtonHome)

        self.ButtonStart = QPushButton(self.LeftWidget)
        self.ButtonStart.setObjectName(u"ButtonStart")
        self.ButtonStart.setMinimumSize(QSize(42, 42))
        self.ButtonStart.setMaximumSize(QSize(42, 42))
        icon3 = QIcon()
        icon3.addFile(u":/btn/left_widget/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonStart.setIcon(icon3)
        self.ButtonStart.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.ButtonStart)

        self.ButtonAbout = QPushButton(self.LeftWidget)
        self.ButtonAbout.setObjectName(u"ButtonAbout")
        self.ButtonAbout.setMinimumSize(QSize(42, 42))
        self.ButtonAbout.setMaximumSize(QSize(42, 42))
        icon4 = QIcon()
        icon4.addFile(u":/btn/left_widget/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonAbout.setIcon(icon4)
        self.ButtonAbout.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.ButtonAbout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ButtonTheme = QPushButton(self.LeftWidget)
        self.ButtonTheme.setObjectName(u"ButtonTheme")
        self.ButtonTheme.setMinimumSize(QSize(42, 42))
        self.ButtonTheme.setMaximumSize(QSize(42, 42))
        icon5 = QIcon()
        icon5.addFile(u":/btn/left_widget/dark_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/btn/left_widget/light_theme.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ButtonTheme.setIcon(icon5)
        self.ButtonTheme.setIconSize(QSize(24, 24))
        self.ButtonTheme.setCheckable(True)

        self.verticalLayout_2.addWidget(self.ButtonTheme)


        self.horizontalLayout.addWidget(self.LeftWidget)

        self.StackedWidget = QStackedWidget(self.ContentWidget)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.verticalLayout_3 = QVBoxLayout(self.HomePage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.HomeLabel = QLabel(self.HomePage)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setMinimumSize(QSize(964, 400))
        self.HomeLabel.setMaximumSize(QSize(16777215, 400))

        self.verticalLayout_3.addWidget(self.HomeLabel)

        self.PathSetWidget = QWidget(self.HomePage)
        self.PathSetWidget.setObjectName(u"PathSetWidget")
        self.ButtonPathSet = QPushButton(self.PathSetWidget)
        self.ButtonPathSet.setObjectName(u"ButtonPathSet")
        self.ButtonPathSet.setGeometry(QRect(840, 90, 32, 32))
        self.ButtonPathSet.setMinimumSize(QSize(32, 32))
        self.ButtonPathSet.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/btn/main_widget/increase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonPathSet.setIcon(icon6)
        self.ButtonPathSet.setIconSize(QSize(24, 24))
        self.PathSetTopWidget = QWidget(self.PathSetWidget)
        self.PathSetTopWidget.setObjectName(u"PathSetTopWidget")
        self.PathSetTopWidget.setGeometry(QRect(0, 0, 964, 60))
        self.PathSetTopWidget.setMinimumSize(QSize(964, 60))
        self.PathSetTopWidget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.PathSetTopWidget)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 0, 15, 0)
        self.PathSetLabel = QLabel(self.PathSetTopWidget)
        self.PathSetLabel.setObjectName(u"PathSetLabel")

        self.horizontalLayout_3.addWidget(self.PathSetLabel)

        self.ButtonNext = QPushButton(self.PathSetTopWidget)
        self.ButtonNext.setObjectName(u"ButtonNext")
        self.ButtonNext.setMinimumSize(QSize(32, 32))
        self.ButtonNext.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/btn/main_widget/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonNext.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.ButtonNext)

        self.ButtonChangeGame = QPushButton(self.PathSetWidget)
        self.ButtonChangeGame.setObjectName(u"ButtonChangeGame")
        self.ButtonChangeGame.setGeometry(QRect(890, 90, 32, 32))
        self.ButtonChangeGame.setMinimumSize(QSize(32, 32))
        self.ButtonChangeGame.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/btn/main_widget/switch.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonChangeGame.setIcon(icon8)
        self.ButtonChangeGame.setIconSize(QSize(24, 24))
        self.CurrentGameLabel = QLabel(self.PathSetWidget)
        self.CurrentGameLabel.setObjectName(u"CurrentGameLabel")
        self.CurrentGameLabel.setGeometry(QRect(40, 90, 781, 32))
        self.CurrentGameLabel.setMinimumSize(QSize(200, 32))
        self.CurrentGameLabel.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_3.addWidget(self.PathSetWidget)

        self.StackedWidget.addWidget(self.HomePage)
        self.StartPage = QWidget()
        self.StartPage.setObjectName(u"StartPage")
        self.verticalLayout_4 = QVBoxLayout(self.StartPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StartPageScrollArea = QScrollArea(self.StartPage)
        self.StartPageScrollArea.setObjectName(u"StartPageScrollArea")
        self.StartPageScrollArea.setMinimumSize(QSize(964, 0))
        self.StartPageScrollArea.setMaximumSize(QSize(964, 16777215))
        self.StartPageScrollArea.setWidgetResizable(True)
        self.StartPageScrollWidget = QWidget()
        self.StartPageScrollWidget.setObjectName(u"StartPageScrollWidget")
        self.StartPageScrollWidget.setGeometry(QRect(0, 0, 964, 630))
        self.StartPageScrollWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.StartPageScrollWidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(7, 7, 7, 7)
        self.FunctionWidget = QWidget(self.StartPageScrollWidget)
        self.FunctionWidget.setObjectName(u"FunctionWidget")
        self.FunctionWidget.setMinimumSize(QSize(944, 60))
        self.FunctionWidget.setMaximumSize(QSize(944, 60))
        self.gridLayout = QGridLayout(self.FunctionWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.FunctionTitleLabel = QLabel(self.FunctionWidget)
        self.FunctionTitleLabel.setObjectName(u"FunctionTitleLabel")

        self.gridLayout.addWidget(self.FunctionTitleLabel, 0, 0, 1, 1)

        self.ButtonEditFolder = QPushButton(self.FunctionWidget)
        self.ButtonEditFolder.setObjectName(u"ButtonEditFolder")
        self.ButtonEditFolder.setMinimumSize(QSize(32, 32))
        self.ButtonEditFolder.setMaximumSize(QSize(32, 32))
        icon9 = QIcon()
        icon9.addFile(u":/btn/main_widget/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/btn/main_widget/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ButtonEditFolder.setIcon(icon9)
        self.ButtonEditFolder.setIconSize(QSize(24, 24))
        self.ButtonEditFolder.setCheckable(True)

        self.gridLayout.addWidget(self.ButtonEditFolder, 0, 4, 1, 1)

        self.ButtonSelectMore = QPushButton(self.FunctionWidget)
        self.ButtonSelectMore.setObjectName(u"ButtonSelectMore")
        self.ButtonSelectMore.setMinimumSize(QSize(32, 32))
        self.ButtonSelectMore.setMaximumSize(QSize(32, 32))
        icon10 = QIcon()
        icon10.addFile(u":/btn/main_widget/select.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/btn/main_widget/unselect.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ButtonSelectMore.setIcon(icon10)
        self.ButtonSelectMore.setIconSize(QSize(24, 24))
        self.ButtonSelectMore.setCheckable(True)

        self.gridLayout.addWidget(self.ButtonSelectMore, 0, 2, 1, 1)

        self.ButtonAddFolder = QPushButton(self.FunctionWidget)
        self.ButtonAddFolder.setObjectName(u"ButtonAddFolder")
        self.ButtonAddFolder.setMinimumSize(QSize(32, 32))
        self.ButtonAddFolder.setMaximumSize(QSize(32, 32))
        self.ButtonAddFolder.setIcon(icon6)
        self.ButtonAddFolder.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.ButtonAddFolder, 0, 3, 1, 1)

        self.ButtonDelFolder = QPushButton(self.FunctionWidget)
        self.ButtonDelFolder.setObjectName(u"ButtonDelFolder")
        self.ButtonDelFolder.setMinimumSize(QSize(32, 32))
        self.ButtonDelFolder.setMaximumSize(QSize(32, 32))
        icon11 = QIcon()
        icon11.addFile(u":/btn/main_widget/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ButtonDelFolder.setIcon(icon11)
        self.ButtonDelFolder.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.ButtonDelFolder, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.FunctionWidget)

        self.FolderWidget = QWidget(self.StartPageScrollWidget)
        self.FolderWidget.setObjectName(u"FolderWidget")
        self.FolderWidget.setMinimumSize(QSize(944, 550))
        self.FolderWidget.setMaximumSize(QSize(944, 16777215))
        self.FolderGridLayout = QGridLayout(self.FolderWidget)
        self.FolderGridLayout.setObjectName(u"FolderGridLayout")
        self.FolderGridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.FolderWidget)

        self.StartPageScrollArea.setWidget(self.StartPageScrollWidget)

        self.verticalLayout_4.addWidget(self.StartPageScrollArea)

        self.BottomWidget = QWidget(self.StartPage)
        self.BottomWidget.setObjectName(u"BottomWidget")
        self.BottomWidget.setMinimumSize(QSize(0, 50))
        self.BottomWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.BottomWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ButtonPlay = QPushButton(self.BottomWidget)
        self.ButtonPlay.setObjectName(u"ButtonPlay")
        self.ButtonPlay.setMinimumSize(QSize(96, 38))
        self.ButtonPlay.setMaximumSize(QSize(96, 38))
        self.ButtonPlay.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.ButtonPlay)


        self.verticalLayout_4.addWidget(self.BottomWidget)

        self.StackedWidget.addWidget(self.StartPage)
        self.AboutPage = QWidget()
        self.AboutPage.setObjectName(u"AboutPage")
        self.verticalLayout_6 = QVBoxLayout(self.AboutPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.AboutPageTitle = QLabel(self.AboutPage)
        self.AboutPageTitle.setObjectName(u"AboutPageTitle")
        self.AboutPageTitle.setMinimumSize(QSize(0, 60))
        self.AboutPageTitle.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_6.addWidget(self.AboutPageTitle)

        self.AboutPageScrollArea = QScrollArea(self.AboutPage)
        self.AboutPageScrollArea.setObjectName(u"AboutPageScrollArea")
        self.AboutPageScrollArea.setMinimumSize(QSize(964, 400))
        self.AboutPageScrollArea.setWidgetResizable(True)
        self.AboutPageScrollWidget = QWidget()
        self.AboutPageScrollWidget.setObjectName(u"AboutPageScrollWidget")
        self.AboutPageScrollWidget.setGeometry(QRect(0, 0, 964, 400))
        self.verticalLayout_7 = QVBoxLayout(self.AboutPageScrollWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.SoftwareInfoWidget = QWidget(self.AboutPageScrollWidget)
        self.SoftwareInfoWidget.setObjectName(u"SoftwareInfoWidget")
        self.SoftwareInfoWidget.setMinimumSize(QSize(944, 200))
        self.SoftwareInfoWidget.setMaximumSize(QSize(944, 200))
        self.SoftwareInfoTitle = QLabel(self.SoftwareInfoWidget)
        self.SoftwareInfoTitle.setObjectName(u"SoftwareInfoTitle")
        self.SoftwareInfoTitle.setGeometry(QRect(10, 0, 171, 60))
        self.SoftwareInfoTitle.setMinimumSize(QSize(0, 60))
        self.SoftwareInfoTitle.setMaximumSize(QSize(16777215, 60))
        self.SoftwarePic = QLabel(self.SoftwareInfoWidget)
        self.SoftwarePic.setObjectName(u"SoftwarePic")
        self.SoftwarePic.setGeometry(QRect(20, 70, 64, 64))
        self.SoftwarePic.setMinimumSize(QSize(64, 64))
        self.SoftwarePic.setMaximumSize(QSize(64, 64))
        self.SoftwareName = QLabel(self.SoftwareInfoWidget)
        self.SoftwareName.setObjectName(u"SoftwareName")
        self.SoftwareName.setGeometry(QRect(90, 70, 125, 32))
        self.SoftwareName.setMinimumSize(QSize(125, 32))
        self.SoftwareName.setMaximumSize(QSize(125, 32))
        self.SoftwareVersion = QLabel(self.SoftwareInfoWidget)
        self.SoftwareVersion.setObjectName(u"SoftwareVersion")
        self.SoftwareVersion.setGeometry(QRect(90, 110, 125, 32))
        self.SoftwareVersion.setMinimumSize(QSize(125, 32))
        self.SoftwareVersion.setMaximumSize(QSize(125, 32))
        self.DeveloperPic = QLabel(self.SoftwareInfoWidget)
        self.DeveloperPic.setObjectName(u"DeveloperPic")
        self.DeveloperPic.setGeometry(QRect(270, 70, 64, 64))
        self.DeveloperPic.setMinimumSize(QSize(64, 64))
        self.DeveloperPic.setMaximumSize(QSize(64, 64))
        self.DeveloperName = QLabel(self.SoftwareInfoWidget)
        self.DeveloperName.setObjectName(u"DeveloperName")
        self.DeveloperName.setGeometry(QRect(360, 70, 125, 32))
        self.DeveloperName.setMinimumSize(QSize(125, 32))
        self.DeveloperName.setMaximumSize(QSize(125, 32))
        self.DeveloperInfo = QLabel(self.SoftwareInfoWidget)
        self.DeveloperInfo.setObjectName(u"DeveloperInfo")
        self.DeveloperInfo.setGeometry(QRect(360, 110, 571, 32))
        self.DeveloperInfo.setMinimumSize(QSize(125, 32))
        self.DeveloperInfo.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout_7.addWidget(self.SoftwareInfoWidget)

        self.VersionInfoWidget = QWidget(self.AboutPageScrollWidget)
        self.VersionInfoWidget.setObjectName(u"VersionInfoWidget")
        self.VersionInfoWidget.setMinimumSize(QSize(944, 0))
        self.VersionInfoWidget.setMaximumSize(QSize(944, 16777215))
        self.VersionInfoTitle = QLabel(self.VersionInfoWidget)
        self.VersionInfoTitle.setObjectName(u"VersionInfoTitle")
        self.VersionInfoTitle.setGeometry(QRect(10, 0, 171, 60))
        self.VersionInfoTitle.setMinimumSize(QSize(0, 60))
        self.VersionInfoTitle.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_7.addWidget(self.VersionInfoWidget)

        self.AboutPageScrollArea.setWidget(self.AboutPageScrollWidget)

        self.verticalLayout_6.addWidget(self.AboutPageScrollArea)

        self.StackedWidget.addWidget(self.AboutPage)

        self.horizontalLayout.addWidget(self.StackedWidget)


        self.verticalLayout.addWidget(self.ContentWidget)

        MainWindow.setCentralWidget(self.StyleSheet)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.Icon.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"GameLauncher", None))
#if QT_CONFIG(tooltip)
        self.ButtonMin.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonExit.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonHome.setToolTip(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonStart.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u9875", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonAbout.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonTheme.setToolTip(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3b\u9898", None))
#endif // QT_CONFIG(tooltip)
        self.HomeLabel.setText("")
#if QT_CONFIG(tooltip)
        self.ButtonPathSet.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonPathSet.setText("")
        self.PathSetLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u6e38\u620f\u8def\u5f84", None))
#if QT_CONFIG(tooltip)
        self.ButtonNext.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ButtonChangeGame.setToolTip(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u6e38\u620f", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonChangeGame.setText("")
        self.CurrentGameLabel.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6e38\u620f\uff1a", None))
        self.FunctionTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.ButtonEditFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165\u7f16\u8f91\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonEditFolder.setText("")
#if QT_CONFIG(tooltip)
        self.ButtonSelectMore.setToolTip(QCoreApplication.translate("MainWindow", u"\u591a\u9009", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonSelectMore.setText("")
#if QT_CONFIG(tooltip)
        self.ButtonAddFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonAddFolder.setText("")
#if QT_CONFIG(tooltip)
        self.ButtonDelFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#endif // QT_CONFIG(tooltip)
        self.ButtonDelFolder.setText("")
        self.ButtonPlay.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6e38\u620f", None))
        self.AboutPageTitle.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.SoftwareInfoTitle.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u4fe1\u606f", None))
        self.SoftwarePic.setText("")
        self.SoftwareName.setText(QCoreApplication.translate("MainWindow", u"GameLauncher", None))
        self.SoftwareVersion.setText(QCoreApplication.translate("MainWindow", u"Version\uff1a1.0.0b", None))
        self.DeveloperPic.setText("")
        self.DeveloperName.setText(QCoreApplication.translate("MainWindow", u"ichinoseyuu", None))
        self.DeveloperInfo.setText(QCoreApplication.translate("MainWindow", u"GameLauncher\u7684\u5f00\u53d1\u8005", None))
        self.VersionInfoTitle.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\u4fe1\u606f", None))
        pass
    # retranslateUi

