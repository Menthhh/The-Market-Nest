# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 549)
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#widget_2{\n"
"	background-color: rgb(240, 244, 245);\n"
"}\n"
"\n"
"#full_menu_widget, #icon_only_widget{\n"
"	background-color: rgb(240, 244, 245);\n"
"}\n"
"\n"
"#main{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#full_menu_widget QPushButton{\n"
"	text-align:left;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_menu_widget.sizePolicy().hasHeightForWidth())
        self.full_menu_widget.setSizePolicy(sizePolicy)
        self.full_menu_widget.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_4 = QLabel(self.full_menu_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(35, 35))
        self.label_4.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.full_menu_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Josefin Sans SemiBold"])
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.homeBtn_2 = QPushButton(self.full_menu_widget)
        self.homeBtn_2.setObjectName(u"homeBtn_2")
        self.homeBtn_2.setFocusPolicy(Qt.WheelFocus)
        self.homeBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn_2.setInputMethodHints(Qt.ImhMultiLine)
        icon = QIcon()
        icon.addFile(u":/icon/icon/home.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setCheckable(True)
        self.homeBtn_2.setAutoExclusive(True)
        self.homeBtn_2.setAutoDefault(False)
        self.homeBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.homeBtn_2)

        self.favBtn_2 = QPushButton(self.full_menu_widget)
        self.favBtn_2.setObjectName(u"favBtn_2")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/heart3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.favBtn_2.setIcon(icon1)
        self.favBtn_2.setCheckable(True)
        self.favBtn_2.setAutoExclusive(True)
        self.favBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.favBtn_2)

        self.profileBtn_2 = QPushButton(self.full_menu_widget)
        self.profileBtn_2.setObjectName(u"profileBtn_2")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/store.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn_2.setIcon(icon2)
        self.profileBtn_2.setCheckable(True)
        self.profileBtn_2.setAutoExclusive(True)
        self.profileBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.profileBtn_2)

        self.accountBtn_2 = QPushButton(self.full_menu_widget)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/profile.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn_2.setIcon(icon3)
        self.accountBtn_2.setCheckable(True)
        self.accountBtn_2.setAutoExclusive(True)
        self.accountBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.accountBtn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(117, 509, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitBtn_2 = QPushButton(self.full_menu_widget)
        self.exitBtn_2.setObjectName(u"exitBtn_2")
        font1 = QFont()
        font1.setFamilies([u"Josefin Sans Medium"])
        self.exitBtn_2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/logout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn_2.setIcon(icon4)
        self.exitBtn_2.setFlat(True)

        self.verticalLayout_4.addWidget(self.exitBtn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMaximumSize(QSize(50, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 20)
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(35, 35))
        self.label.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeBtn_1 = QPushButton(self.icon_only_widget)
        self.homeBtn_1.setObjectName(u"homeBtn_1")
        self.homeBtn_1.setIcon(icon)
        self.homeBtn_1.setCheckable(True)
        self.homeBtn_1.setAutoExclusive(True)
        self.homeBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.homeBtn_1)

        self.favBtn_1 = QPushButton(self.icon_only_widget)
        self.favBtn_1.setObjectName(u"favBtn_1")
        self.favBtn_1.setIcon(icon1)
        self.favBtn_1.setCheckable(True)
        self.favBtn_1.setAutoExclusive(True)
        self.favBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.favBtn_1)

        self.profileBtn_1 = QPushButton(self.icon_only_widget)
        self.profileBtn_1.setObjectName(u"profileBtn_1")
        self.profileBtn_1.setIcon(icon2)
        self.profileBtn_1.setCheckable(True)
        self.profileBtn_1.setAutoExclusive(True)
        self.profileBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.profileBtn_1)

        self.accountBtn_1 = QPushButton(self.icon_only_widget)
        self.accountBtn_1.setObjectName(u"accountBtn_1")
        self.accountBtn_1.setIcon(icon3)
        self.accountBtn_1.setCheckable(True)
        self.accountBtn_1.setAutoExclusive(True)
        self.accountBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.accountBtn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(47, 509, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitBtn_1 = QPushButton(self.icon_only_widget)
        self.exitBtn_1.setObjectName(u"exitBtn_1")
        self.exitBtn_1.setIcon(icon4)
        self.exitBtn_1.setFlat(True)

        self.verticalLayout_3.addWidget(self.exitBtn_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.main = QWidget(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.main)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.main)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setStyleSheet(u"#pushButton_3 {\n"
"	background-color: rgb(9, 20, 68);\n"
"    border: rgb(9, 20, 68);\n"
"	color: white;\n"
"	border-radius: 3px;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.changeBtn_1 = QPushButton(self.widget)
        self.changeBtn_1.setObjectName(u"changeBtn_1")
        self.changeBtn_1.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.changeBtn_1.setIcon(icon5)
        self.changeBtn_1.setCheckable(True)
        self.changeBtn_1.setFlat(True)

        self.horizontalLayout_4.addWidget(self.changeBtn_1)

        self.horizontalSpacer = QSpacerItem(233, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchInput_1 = QLineEdit(self.widget)
        self.searchInput_1.setObjectName(u"searchInput_1")

        self.horizontalLayout.addWidget(self.searchInput_1)

        self.searchBtn_1 = QPushButton(self.widget)
        self.searchBtn_1.setObjectName(u"searchBtn_1")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn_1.setIcon(icon6)
        self.searchBtn_1.setFlat(True)

        self.horizontalLayout.addWidget(self.searchBtn_1)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(233, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.sellBtn_1 = QPushButton(self.widget)
        self.sellBtn_1.setObjectName(u"sellBtn_1")
        self.sellBtn_1.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_4.addWidget(self.sellBtn_1)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#cart,home,order,search,user{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.sell = QWidget()
        self.sell.setObjectName(u"sell")
        self.gridLayout_22 = QGridLayout(self.sell)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.sell)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_44 = QGridLayout(self.widget_11)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_11)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_39 = QGridLayout(self.widget_24)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setHorizontalSpacing(10)
        self.gridLayout_39.setVerticalSpacing(0)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.gridLayout_37 = QGridLayout(self.widget_25)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_25)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_37.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_25, 0, 0, 1, 1)

        self.widget_26 = QWidget(self.widget_24)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_38 = QGridLayout(self.widget_26)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.widget_26)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 100))
        self.plainTextEdit.setAutoFillBackground(False)

        self.gridLayout_38.addWidget(self.plainTextEdit, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_26, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_24, 4, 0, 1, 1)

        self.widget_30 = QWidget(self.widget_11)
        self.widget_30.setObjectName(u"widget_30")
        self.gridLayout_43 = QGridLayout(self.widget_30)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setHorizontalSpacing(36)
        self.gridLayout_43.setVerticalSpacing(0)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_32 = QWidget(self.widget_30)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_42 = QGridLayout(self.widget_32)
        self.gridLayout_42.setSpacing(0)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.widget_32)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_42.addWidget(self.lineEdit_4, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.widget_32, 0, 1, 1, 1)

        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.gridLayout_41 = QGridLayout(self.widget_31)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_31)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_41.addWidget(self.label_21, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.widget_31, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.widget_30, 6, 0, 1, 1)

        self.widget_15 = QWidget(self.widget_11)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_28 = QGridLayout(self.widget_15)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(69)
        self.gridLayout_28.setVerticalSpacing(0)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy)
        self.widget_16.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_26 = QGridLayout(self.widget_16)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_16)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)

        self.gridLayout_26.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_16, 0, 0, 1, 1)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_27 = QGridLayout(self.widget_17)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget_17)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_27.addWidget(self.comboBox, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_17, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_15, 1, 0, 1, 1)

        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_25 = QGridLayout(self.widget_12)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(50)
        self.gridLayout_25.setVerticalSpacing(0)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_23 = QGridLayout(self.widget_13)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_23.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_24 = QGridLayout(self.widget_14)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget_14)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_24.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.widget_14, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_12, 0, 0, 1, 1)

        self.widget_21 = QWidget(self.widget_11)
        self.widget_21.setObjectName(u"widget_21")
        self.gridLayout_34 = QGridLayout(self.widget_21)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setHorizontalSpacing(39)
        self.gridLayout_34.setVerticalSpacing(0)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.gridLayout_32 = QGridLayout(self.widget_22)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_22)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_32.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_22, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_33 = QGridLayout(self.widget_23)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_23)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_33.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_23, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_21, 3, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_11)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_31 = QGridLayout(self.widget_18)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(91)
        self.gridLayout_31.setVerticalSpacing(0)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_29 = QGridLayout(self.widget_19)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_19)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_29.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.widget_19, 0, 0, 1, 1)

        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_30 = QGridLayout(self.widget_20)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget_20)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_30.addWidget(self.lineEdit_2, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.widget_20, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_18, 2, 0, 1, 1)

        self.widget_27 = QWidget(self.widget_11)
        self.widget_27.setObjectName(u"widget_27")
        self.gridLayout_40 = QGridLayout(self.widget_27)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setHorizontalSpacing(70)
        self.gridLayout_40.setVerticalSpacing(0)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_35 = QGridLayout(self.widget_28)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_28)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_35.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_28, 0, 0, 1, 1)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_36 = QGridLayout(self.widget_29)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.widget_29)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_36.addWidget(self.lineEdit_3, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_29, 0, 1, 1, 1)


        self.gridLayout_44.addWidget(self.widget_27, 5, 0, 1, 1)

        self.BtnContainer = QWidget(self.widget_11)
        self.BtnContainer.setObjectName(u"BtnContainer")
        self.gridLayout_49 = QGridLayout(self.BtnContainer)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.widget_37 = QWidget(self.BtnContainer)
        self.widget_37.setObjectName(u"widget_37")
        self.gridLayout_48 = QGridLayout(self.widget_37)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.doneAddBtn_1 = QPushButton(self.widget_37)
        self.doneAddBtn_1.setObjectName(u"doneAddBtn_1")

        self.gridLayout_48.addWidget(self.doneAddBtn_1, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.widget_37, 0, 0, 1, 1)


        self.gridLayout_44.addWidget(self.BtnContainer, 7, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.sell)
        self.viewproduct = QWidget()
        self.viewproduct.setObjectName(u"viewproduct")
        self.gridLayout_13 = QGridLayout(self.viewproduct)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.viewproduct)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_21 = QGridLayout(self.widget_4)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_15 = QGridLayout(self.widget_5)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.product_img = QLabel(self.widget_5)
        self.product_img.setObjectName(u"product_img")

        self.gridLayout_15.addWidget(self.product_img, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_16 = QGridLayout(self.widget_6)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_6)
        self.widget_35.setObjectName(u"widget_35")
        self.gridLayout_47 = QGridLayout(self.widget_35)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.chat = QLabel(self.widget_35)
        self.chat.setObjectName(u"chat")

        self.gridLayout_47.addWidget(self.chat, 0, 0, 1, 1)

        self.phone = QLabel(self.widget_35)
        self.phone.setObjectName(u"phone")

        self.gridLayout_47.addWidget(self.phone, 0, 1, 1, 1)


        self.gridLayout_16.addWidget(self.widget_35, 2, 0, 1, 1)

        self.widget_34 = QWidget(self.widget_6)
        self.widget_34.setObjectName(u"widget_34")
        self.gridLayout_46 = QGridLayout(self.widget_34)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.product_price = QLabel(self.widget_34)
        self.product_price.setObjectName(u"product_price")

        self.gridLayout_46.addWidget(self.product_price, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_34, 1, 0, 1, 1)

        self.widget_33 = QWidget(self.widget_6)
        self.widget_33.setObjectName(u"widget_33")
        self.gridLayout_45 = QGridLayout(self.widget_33)
        self.gridLayout_45.setSpacing(0)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.widget_33)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy2)
        self.gridLayout_50 = QGridLayout(self.widget_36)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_36)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/heart2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)

        self.gridLayout_50.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.product_name = QLabel(self.widget_36)
        self.product_name.setObjectName(u"product_name")

        self.gridLayout_50.addWidget(self.product_name, 0, 0, 1, 1)


        self.gridLayout_45.addWidget(self.widget_36, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_33, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_6, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_20 = QGridLayout(self.widget_7)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_18 = QGridLayout(self.widget_8)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_18.addWidget(self.label_10, 0, 2, 1, 1)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_18.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_17 = QGridLayout(self.widget_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_17.addWidget(self.label_12, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.gridLayout_20.addWidget(self.widget_9, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_19 = QGridLayout(self.widget_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_13 = QLabel(self.widget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_19.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.widget_10)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_14.setWordWrap(True)

        self.gridLayout_19.addWidget(self.label_14, 0, 1, 2, 1)


        self.gridLayout_20.addWidget(self.widget_10, 2, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_7, 1, 0, 1, 2)


        self.gridLayout_13.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewproduct)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.gridLayout_5 = QGridLayout(self.search)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.search)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.search)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"#widget_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_9 = QGridLayout(self.home)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.home_container = QWidget(self.home)
        self.home_container.setObjectName(u"home_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home_container.sizePolicy().hasHeightForWidth())
        self.home_container.setSizePolicy(sizePolicy3)
        self.home_container.setStyleSheet(u"#widget_3, #widget_5, #widget_6{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_8 = QGridLayout(self.home_container)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.home_wrapper = QWidget(self.home_container)
        self.home_wrapper.setObjectName(u"home_wrapper")
        self.gridLayout_7 = QGridLayout(self.home_wrapper)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.home_wrapper)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollHome = QWidget()
        self.scrollHome.setObjectName(u"scrollHome")
        self.scrollHome.setGeometry(QRect(0, 0, 570, 486))
        self.gridLayout_2 = QGridLayout(self.scrollHome)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollHome)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_14 = QGridLayout(self.widget_3)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Banner = QWidget(self.widget_3)
        self.Banner.setObjectName(u"Banner")
        self.gridLayout_11 = QGridLayout(self.Banner)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.Banner)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_12 = QGridLayout(self.widget_2)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Aksaramatee"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.gridLayout_12.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.Banner, 0, 0, 1, 1)

        self.categoryWrap = QWidget(self.widget_3)
        self.categoryWrap.setObjectName(u"categoryWrap")
        self.gridLayout_10 = QGridLayout(self.categoryWrap)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.categoryWrap)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.categoryWrap, 1, 0, 1, 1)

        self.productlist = QWidget(self.widget_3)
        self.productlist.setObjectName(u"productlist")

        self.gridLayout_14.addWidget(self.productlist, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollHome)

        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.home_wrapper, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.home_container, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.favourite = QWidget()
        self.favourite.setObjectName(u"favourite")
        self.gridLayout_51 = QGridLayout(self.favourite)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_38 = QWidget(self.favourite)
        self.widget_38.setObjectName(u"widget_38")
        self.gridLayout_53 = QGridLayout(self.widget_38)
        self.gridLayout_53.setSpacing(0)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 5)
        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.gridLayout_52 = QGridLayout(self.widget_39)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_22 = QLabel(self.widget_39)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_52.addWidget(self.label_22, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.widget_39, 0, 0, 1, 1)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.gridLayout_54 = QGridLayout(self.widget_40)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.scrollArea_2 = QScrollArea(self.widget_40)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 552, 429))
        self.gridLayout_55 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.favoriteList = QWidget(self.scrollAreaWidgetContents)
        self.favoriteList.setObjectName(u"favoriteList")

        self.gridLayout_55.addWidget(self.favoriteList, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_54.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout_53.addWidget(self.widget_40, 1, 0, 1, 1)


        self.gridLayout_51.addWidget(self.widget_38, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.favourite)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.gridLayout_6 = QGridLayout(self.profile)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.profile)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.profile)
        self.acc = QWidget()
        self.acc.setObjectName(u"acc")
        self.gridLayout_3 = QGridLayout(self.acc)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.acc)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.acc)
        self.order = QWidget()
        self.order.setObjectName(u"order")
        self.gridLayout_4 = QGridLayout(self.order)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.order)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.order)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.changeBtn_1.toggled.connect(self.icon_only_widget.setVisible)
        self.changeBtn_1.toggled.connect(self.full_menu_widget.setHidden)
        self.homeBtn_1.toggled.connect(self.homeBtn_2.setChecked)
        self.homeBtn_2.toggled.connect(self.homeBtn_1.setChecked)
        self.exitBtn_2.clicked.connect(MainWindow.close)
        self.exitBtn_1.clicked.connect(MainWindow.close)
        self.favBtn_1.toggled.connect(self.favBtn_2.setChecked)
        self.favBtn_2.toggled.connect(self.favBtn_1.setChecked)
        self.profileBtn_1.toggled.connect(self.profileBtn_2.setChecked)
        self.accountBtn_1.toggled.connect(self.accountBtn_2.setChecked)
        self.profileBtn_2.toggled.connect(self.profileBtn_1.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn_1.setChecked)

        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MarketNest", None))
        self.homeBtn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.favBtn_2.setText(QCoreApplication.translate("MainWindow", u"Favorite", None))
        self.profileBtn_2.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"Edit Account", None))
        self.exitBtn_2.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label.setText("")
        self.homeBtn_1.setText("")
        self.favBtn_1.setText("")
        self.profileBtn_1.setText("")
        self.accountBtn_1.setText("")
        self.exitBtn_1.setText("")
        self.changeBtn_1.setText("")
        self.searchBtn_1.setText("")
        self.sellBtn_1.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Product Description", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Product Title", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Product Photo", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"+ Upload Photo", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.doneAddBtn_1.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.product_img.setText(QCoreApplication.translate("MainWindow", u"img", None))
        self.chat.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.phone.setText(QCoreApplication.translate("MainWindow", u"Tel: 000-000-0000", None))
        self.product_price.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.pushButton_3.setText("")
        self.product_name.setText(QCoreApplication.translate("MainWindow", u"product name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Seller", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Product Specification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa"
                        "[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;[;]fa[];fe[;", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"a banner", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Caregory", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"My Favorites", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"profile", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"acc", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Order Page", None))
    # retranslateUi

