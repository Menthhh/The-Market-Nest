# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAppUi.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1282, 803)
        MainWindow.setFocusPolicy(Qt.TabFocus)
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
        self.label.setPixmap(QPixmap(u":/ico/icon/sms.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeBtn_1 = QPushButton(self.icon_only_widget)
        self.homeBtn_1.setObjectName(u"homeBtn_1")
        icon = QIcon()
        icon.addFile(u":/ico/icon/home.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn_1.setIcon(icon)
        self.homeBtn_1.setCheckable(True)
        self.homeBtn_1.setAutoExclusive(True)
        self.homeBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.homeBtn_1)

        self.profileBtn_1 = QPushButton(self.icon_only_widget)
        self.profileBtn_1.setObjectName(u"profileBtn_1")
        icon1 = QIcon()
        icon1.addFile(u":/ico/icon/store.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn_1.setIcon(icon1)
        self.profileBtn_1.setCheckable(True)
        self.profileBtn_1.setAutoExclusive(True)
        self.profileBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.profileBtn_1)

        self.accountBtn_1 = QPushButton(self.icon_only_widget)
        self.accountBtn_1.setObjectName(u"accountBtn_1")
        icon2 = QIcon()
        icon2.addFile(u":/ico/icon/profile.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn_1.setIcon(icon2)
        self.accountBtn_1.setCheckable(True)
        self.accountBtn_1.setAutoExclusive(True)
        self.accountBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.accountBtn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(47, 509, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitBtn_1 = QPushButton(self.icon_only_widget)
        self.exitBtn_1.setObjectName(u"exitBtn_1")
        icon3 = QIcon()
        icon3.addFile(u":/ico/icon/logout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exitBtn_1.setIcon(icon3)
        self.exitBtn_1.setFlat(True)

        self.verticalLayout_3.addWidget(self.exitBtn_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

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
        self.label_4.setPixmap(QPixmap(u":/ico/icon/logo.ico"))
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
        self.homeBtn_2.setFocusPolicy(Qt.TabFocus)
        self.homeBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.homeBtn_2.setStyleSheet(u"font-family: \"Josefin Sans Medium\";\n"
"font-size: 15px;\n"
"color: #51526C;")
        self.homeBtn_2.setInputMethodHints(Qt.ImhMultiLine)
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setCheckable(True)
        self.homeBtn_2.setAutoExclusive(True)
        self.homeBtn_2.setAutoDefault(False)
        self.homeBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.homeBtn_2)

        self.profileBtn_2 = QPushButton(self.full_menu_widget)
        self.profileBtn_2.setObjectName(u"profileBtn_2")
        self.profileBtn_2.setStyleSheet(u"font-family: \"Josefin Sans Medium\";\n"
"font-size: 15px;\n"
"color: #51526C;")
        self.profileBtn_2.setIcon(icon1)
        self.profileBtn_2.setCheckable(True)
        self.profileBtn_2.setAutoExclusive(True)
        self.profileBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.profileBtn_2)

        self.accountBtn_2 = QPushButton(self.full_menu_widget)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        self.accountBtn_2.setStyleSheet(u"font-family: \"Josefin Sans Medium\";\n"
"font-size: 15px;\n"
"color: #51526C;")
        self.accountBtn_2.setIcon(icon2)
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
        self.exitBtn_2.setStyleSheet(u"font-family: \"Josefin Sans Medium\";\n"
"font-size: 13px;\n"
"color: #51526C;")
        self.exitBtn_2.setIcon(icon3)
        self.exitBtn_2.setFlat(True)

        self.verticalLayout_4.addWidget(self.exitBtn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

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
        icon4 = QIcon()
        icon4.addFile(u":/ico/icon/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.changeBtn_1.setIcon(icon4)
        self.changeBtn_1.setCheckable(True)
        self.changeBtn_1.setFlat(True)

        self.horizontalLayout_4.addWidget(self.changeBtn_1)

        self.horizontalSpacer = QSpacerItem(233, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchInput_1 = QLineEdit(self.widget)
        self.searchInput_1.setObjectName(u"searchInput_1")

        self.horizontalLayout.addWidget(self.searchInput_1)

        self.searchBtn_1 = QPushButton(self.widget)
        self.searchBtn_1.setObjectName(u"searchBtn_1")
        icon5 = QIcon()
        icon5.addFile(u":/ico/icon/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn_1.setIcon(icon5)
        self.searchBtn_1.setFlat(True)

        self.horizontalLayout.addWidget(self.searchBtn_1)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer_2 = QSpacerItem(233, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.sellBtn_1 = QPushButton(self.widget)
        self.sellBtn_1.setObjectName(u"sellBtn_1")
        self.sellBtn_1.setMinimumSize(QSize(50, 30))
        self.sellBtn_1.setStyleSheet(u"font-family: \"Josefin Sans Medium\";\n"
"font-size: 12px;\n"
"background-color: #0d1c63;\n"
"color: #ffffff;\n"
"border-radius: 5;")

        self.horizontalLayout_4.addWidget(self.sellBtn_1)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: 0px")
        self.sell = QWidget()
        self.sell.setObjectName(u"sell")
        self.gridLayout_22 = QGridLayout(self.sell)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.sell)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(700, 16777215))
        self.gridLayout_73 = QGridLayout(self.widget_11)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
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
        self.label_15.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_23.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_24 = QGridLayout(self.widget_14)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.productTitle = QLineEdit(self.widget_14)
        self.productTitle.setObjectName(u"productTitle")
        self.productTitle.setMaximumSize(QSize(540, 16777215))
        self.productTitle.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_24.addWidget(self.productTitle, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.widget_14, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_12, 0, 0, 1, 1)

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
        self.label_16.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_26.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_16, 0, 0, 1, 1)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_27 = QGridLayout(self.widget_17)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.productCategory = QComboBox(self.widget_17)
        self.productCategory.setObjectName(u"productCategory")
        self.productCategory.setMaximumSize(QSize(540, 16777215))
        self.productCategory.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_27.addWidget(self.productCategory, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_17, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_15, 1, 0, 1, 1)

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
        self.label_17.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_29.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.widget_19, 0, 0, 1, 1)

        self.widget_20 = QWidget(self.widget_18)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_30 = QGridLayout(self.widget_20)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.productPrice = QLineEdit(self.widget_20)
        self.productPrice.setObjectName(u"productPrice")
        self.productPrice.setMaximumSize(QSize(540, 16777215))
        self.productPrice.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_30.addWidget(self.productPrice, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.widget_20, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_18, 2, 0, 1, 1)

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
        self.label_18.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_32.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_22, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_33 = QGridLayout(self.widget_23)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.uploadPhotoBtn = QPushButton(self.widget_23)
        self.uploadPhotoBtn.setObjectName(u"uploadPhotoBtn")
        self.uploadPhotoBtn.setMinimumSize(QSize(0, 30))
        self.uploadPhotoBtn.setStyleSheet(u"background-color: #e8e8e8;\n"
"border-radius: 5px;\n"
"color: #51526C;\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"\n"
"")

        self.gridLayout_33.addWidget(self.uploadPhotoBtn, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_23, 0, 2, 1, 1)

        self.uploadedPic = QWidget(self.widget_21)
        self.uploadedPic.setObjectName(u"uploadedPic")

        self.gridLayout_34.addWidget(self.uploadedPic, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_21, 3, 0, 1, 1)

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
        self.label_19.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
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
        self.productDesc = QPlainTextEdit(self.widget_26)
        self.productDesc.setObjectName(u"productDesc")
        self.productDesc.setMaximumSize(QSize(540, 100))
        self.productDesc.setAutoFillBackground(False)
        self.productDesc.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_38.addWidget(self.productDesc, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.widget_26, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_24, 4, 0, 1, 1)

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
        self.label_20.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_35.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_28, 0, 0, 1, 1)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_36 = QGridLayout(self.widget_29)
        self.gridLayout_36.setSpacing(0)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.productLocation = QLineEdit(self.widget_29)
        self.productLocation.setObjectName(u"productLocation")
        self.productLocation.setMaximumSize(QSize(540, 16777215))
        self.productLocation.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_36.addWidget(self.productLocation, 0, 0, 1, 1)


        self.gridLayout_40.addWidget(self.widget_29, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_27, 5, 0, 1, 1)

        self.widget_54 = QWidget(self.widget_11)
        self.widget_54.setObjectName(u"widget_54")
        self.gridLayout_44 = QGridLayout(self.widget_54)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_54)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_44.addWidget(self.label_11, 0, 0, 1, 1)

        self.productAmount = QSpinBox(self.widget_54)
        self.productAmount.setObjectName(u"productAmount")
        self.productAmount.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_44.addWidget(self.productAmount, 0, 1, 1, 1)


        self.gridLayout_73.addWidget(self.widget_54, 6, 0, 1, 1)

        self.BtnContainer = QWidget(self.widget_11)
        self.BtnContainer.setObjectName(u"BtnContainer")
        self.gridLayout_49 = QGridLayout(self.BtnContainer)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.widget_37 = QWidget(self.BtnContainer)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_48 = QGridLayout(self.widget_37)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.doneAddBtn_1 = QPushButton(self.widget_37)
        self.doneAddBtn_1.setObjectName(u"doneAddBtn_1")
        self.doneAddBtn_1.setMinimumSize(QSize(0, 30))
        self.doneAddBtn_1.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_48.addWidget(self.doneAddBtn_1, 0, 0, 1, 1)


        self.gridLayout_49.addWidget(self.widget_37, 0, 0, 1, 1)


        self.gridLayout_73.addWidget(self.BtnContainer, 7, 0, 1, 1)


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
        self.widget_4.setMaximumSize(QSize(1000, 16777215))
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_21 = QGridLayout(self.widget_4)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_15 = QGridLayout(self.widget_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.product_img = QLabel(self.widget_5)
        self.product_img.setObjectName(u"product_img")
        self.product_img.setMaximumSize(QSize(200, 200))

        self.gridLayout_15.addWidget(self.product_img, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_16 = QGridLayout(self.widget_6)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.widget_6)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_119 = QGridLayout(self.widget_35)
        self.gridLayout_119.setSpacing(0)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.gridLayout_119.setContentsMargins(0, 0, 0, 0)
        self.widget_96 = QWidget(self.widget_35)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMaximumSize(QSize(220, 16777215))
        self.widget_96.setStyleSheet(u"background-color: rgb(206, 214, 255);\n"
"border-radius: 10;")
        self.gridLayout_42 = QGridLayout(self.widget_96)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.pushButton = QPushButton(self.widget_96)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 16777215))
        self.pushButton.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(13, 28, 99);")
        icon6 = QIcon()
        icon6.addFile(u":/ico/icon/sms.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(True)

        self.gridLayout_42.addWidget(self.pushButton, 0, 0, 1, 1)

        self.emailLabel = QLabel(self.widget_96)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(13, 28, 99);")

        self.gridLayout_42.addWidget(self.emailLabel, 0, 1, 1, 1)


        self.gridLayout_119.addWidget(self.widget_96, 0, 0, 1, 1)

        self.widget_97 = QWidget(self.widget_35)
        self.widget_97.setObjectName(u"widget_97")
        self.widget_97.setMaximumSize(QSize(220, 16777215))
        self.widget_97.setStyleSheet(u"background-color: rgb(206, 214, 255);\n"
"border-radius: 10;")
        self.gridLayout_118 = QGridLayout(self.widget_97)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.label_69 = QLabel(self.widget_97)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(40, 16777215))
        self.label_69.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(13, 28, 99);")
        self.label_69.setPixmap(QPixmap(u":/ico/icon/phone.ico"))
        self.label_69.setAlignment(Qt.AlignCenter)

        self.gridLayout_118.addWidget(self.label_69, 0, 0, 1, 1)

        self.phoneLabel = QLabel(self.widget_97)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setMaximumSize(QSize(16777215, 16777215))
        self.phoneLabel.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(13, 28, 99);")

        self.gridLayout_118.addWidget(self.phoneLabel, 0, 1, 1, 1)


        self.gridLayout_119.addWidget(self.widget_97, 0, 1, 1, 1)


        self.gridLayout_16.addWidget(self.widget_35, 2, 0, 1, 1)

        self.widget_34 = QWidget(self.widget_6)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_46 = QGridLayout(self.widget_34)
        self.gridLayout_46.setSpacing(0)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(20, 0, 0, 0)
        self.product_price = QLabel(self.widget_34)
        self.product_price.setObjectName(u"product_price")
        self.product_price.setStyleSheet(u"font: 500 20pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_46.addWidget(self.product_price, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_34, 1, 0, 1, 1)

        self.widget_33 = QWidget(self.widget_6)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMaximumSize(QSize(16777215, 100))
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
        self.widget_36.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_50 = QGridLayout(self.widget_36)
        self.gridLayout_50.setSpacing(0)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.gridLayout_50.setContentsMargins(20, 0, 0, 0)
        self.product_name = QLabel(self.widget_36)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setStyleSheet(u"font: 500 20pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_50.addWidget(self.product_name, 0, 0, 1, 1)


        self.gridLayout_45.addWidget(self.widget_36, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_33, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_6, 0, 1, 1, 1)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_47 = QGridLayout(self.widget_7)
        self.gridLayout_47.setSpacing(0)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 30, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(241, 243, 246);")
        self.gridLayout_18 = QGridLayout(self.widget_8)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.sellerNameLabel = QLabel(self.widget_8)
        self.sellerNameLabel.setObjectName(u"sellerNameLabel")
        self.sellerNameLabel.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_18.addWidget(self.sellerNameLabel, 0, 2, 1, 1)

        self.sellerProfileLabel = QLabel(self.widget_8)
        self.sellerProfileLabel.setObjectName(u"sellerProfileLabel")
        self.sellerProfileLabel.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.sellerProfileLabel.setPixmap(QPixmap(u":/ico/icon/profile.ico"))

        self.gridLayout_18.addWidget(self.sellerProfileLabel, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)


        self.gridLayout_47.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_20 = QGridLayout(self.widget_10)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_70 = QLabel(self.widget_10)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_20.addWidget(self.label_70, 0, 0, 1, 1)

        self.addressLabel = QLabel(self.widget_10)
        self.addressLabel.setObjectName(u"addressLabel")
        self.addressLabel.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_20.addWidget(self.addressLabel, 0, 1, 1, 1)


        self.gridLayout_47.addWidget(self.widget_10, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_17 = QGridLayout(self.widget_9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_12 = QLabel(self.widget_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 500 13pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"\n"
"")

        self.gridLayout_17.addWidget(self.label_12, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.gridLayout_47.addWidget(self.widget_9, 2, 0, 1, 1)

        self.widget_30 = QWidget(self.widget_7)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self._2 = QGridLayout(self.widget_30)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(-1, -1, -1, 0)
        self.categoryLabel = QLabel(self.widget_30)
        self.categoryLabel.setObjectName(u"categoryLabel")
        sizePolicy2.setHeightForWidth(self.categoryLabel.sizePolicy().hasHeightForWidth())
        self.categoryLabel.setSizePolicy(sizePolicy2)
        self.categoryLabel.setStyleSheet(u"font: 500 9pt \"Josefin Sans Medium\";")
        self.categoryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.categoryLabel.setWordWrap(True)

        self._2.addWidget(self.categoryLabel, 0, 1, 1, 1)

        self.label_13 = QLabel(self.widget_30)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self._2.addWidget(self.label_13, 0, 0, 1, 1)


        self.gridLayout_47.addWidget(self.widget_30, 3, 0, 1, 1)

        self.widget_31 = QWidget(self.widget_7)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setStyleSheet(u"background-color: rgb(247, 249, 252);")
        self.gridLayout_43 = QGridLayout(self.widget_31)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(-1, -1, 0, -1)
        self.label_21 = QLabel(self.widget_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_43.addWidget(self.label_21, 0, 0, 1, 1)

        self.productDescLabel = QLabel(self.widget_31)
        self.productDescLabel.setObjectName(u"productDescLabel")
        self.productDescLabel.setStyleSheet(u"font: 500 9pt \"Josefin Sans Medium\";")

        self.gridLayout_43.addWidget(self.productDescLabel, 0, 1, 1, 1)


        self.gridLayout_47.addWidget(self.widget_31, 4, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_7, 1, 0, 1, 2)


        self.gridLayout_13.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.viewproduct)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.search.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_120 = QGridLayout(self.search)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.widget_99 = QWidget(self.search)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMaximumSize(QSize(800, 45))
        self.gridLayout_19 = QGridLayout(self.widget_99)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_18 = QSpacerItem(652, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_18, 0, 1, 1, 1)

        self.totalItemFound = QLabel(self.widget_99)
        self.totalItemFound.setObjectName(u"totalItemFound")

        self.gridLayout_19.addWidget(self.totalItemFound, 0, 0, 1, 1)


        self.gridLayout_120.addWidget(self.widget_99, 1, 0, 1, 1)

        self.searchItemList = QWidget(self.search)
        self.searchItemList.setObjectName(u"searchItemList")
        self.searchItemList.setMaximumSize(QSize(800, 16777215))

        self.gridLayout_120.addWidget(self.searchItemList, 2, 0, 1, 1)

        self.widget_98 = QWidget(self.search)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setMaximumSize(QSize(800, 30))
        self.gridLayout_5 = QGridLayout(self.widget_98)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_71 = QLabel(self.widget_98)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(67, 16777215))

        self.gridLayout_5.addWidget(self.label_71, 0, 0, 1, 1)

        self.topicSearch = QLabel(self.widget_98)
        self.topicSearch.setObjectName(u"topicSearch")
        self.topicSearch.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.topicSearch, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(647, 9, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)


        self.gridLayout_120.addWidget(self.widget_98, 0, 0, 1, 1)

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
        self.scrollHome.setGeometry(QRect(0, 0, 1050, 410))
        self.gridLayout_2 = QGridLayout(self.scrollHome)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollHome)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(1050, 16777215))
        self.gridLayout_14 = QGridLayout(self.widget_3)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.productlist = QWidget(self.widget_3)
        self.productlist.setObjectName(u"productlist")

        self.gridLayout_14.addWidget(self.productlist, 2, 0, 1, 1)

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
        self.banner = QLabel(self.widget_2)
        self.banner.setObjectName(u"banner")
        font2 = QFont()
        font2.setFamilies([u"Aksaramatee"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.banner.setFont(font2)
        self.banner.setPixmap(QPixmap(u":/pic/pics/banner.ico"))
        self.banner.setScaledContents(True)

        self.gridLayout_12.addWidget(self.banner, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.Banner, 0, 0, 1, 1)

        self.categoryWrap = QWidget(self.widget_3)
        self.categoryWrap.setObjectName(u"categoryWrap")
        self.categoryWrap.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_96 = QGridLayout(self.categoryWrap)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.sports = QWidget(self.categoryWrap)
        self.sports.setObjectName(u"sports")
        self.gridLayout_91 = QGridLayout(self.sports)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.horizontalSpacer_12 = QSpacerItem(15, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.label_42 = QLabel(self.sports)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_91.addWidget(self.label_42, 2, 0, 1, 4)

        self.label_41 = QLabel(self.sports)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(59, 16777215))
        self.label_41.setPixmap(QPixmap(u":/pic/pics/football.ico"))
        self.label_41.setScaledContents(True)

        self.gridLayout_91.addWidget(self.label_41, 1, 2, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(8, 50, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.sports, 0, 4, 1, 1)

        self.gift = QWidget(self.categoryWrap)
        self.gift.setObjectName(u"gift")
        self.gridLayout_102 = QGridLayout(self.gift)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.horizontalSpacer_13 = QSpacerItem(7, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_102.addItem(self.horizontalSpacer_13, 0, 0, 1, 1)

        self.label_62 = QLabel(self.gift)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(57, 16777215))
        self.label_62.setPixmap(QPixmap(u":/pic/pics/gift.ico"))
        self.label_62.setScaledContents(True)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_102.addWidget(self.label_62, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(17, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_102.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.label_61 = QLabel(self.gift)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_102.addWidget(self.label_61, 1, 0, 1, 3)


        self.gridLayout_96.addWidget(self.gift, 1, 6, 1, 1)

        self.automative = QWidget(self.categoryWrap)
        self.automative.setObjectName(u"automative")
        self.gridLayout_94 = QGridLayout(self.automative)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.label_48 = QLabel(self.automative)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(103, 16777215))
        self.label_48.setPixmap(QPixmap(u":/pic/pics/car.ico"))
        self.label_48.setScaledContents(True)

        self.gridLayout_94.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_47 = QLabel(self.automative)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_94.addWidget(self.label_47, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.automative, 0, 7, 1, 1)

        self.groceries = QWidget(self.categoryWrap)
        self.groceries.setObjectName(u"groceries")
        self.gridLayout_98 = QGridLayout(self.groceries)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.label_54 = QLabel(self.groceries)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setPixmap(QPixmap(u":/pic/pics/groceries.ico"))
        self.label_54.setScaledContents(True)

        self.gridLayout_98.addWidget(self.label_54, 0, 0, 1, 1)

        self.label_53 = QLabel(self.groceries)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_98.addWidget(self.label_53, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.groceries, 1, 2, 1, 1)

        self.babyproducts = QWidget(self.categoryWrap)
        self.babyproducts.setObjectName(u"babyproducts")
        self.gridLayout_99 = QGridLayout(self.babyproducts)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.label_56 = QLabel(self.babyproducts)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setPixmap(QPixmap(u":/pic/pics/baby.ico"))
        self.label_56.setScaledContents(True)

        self.gridLayout_99.addWidget(self.label_56, 0, 0, 1, 1)

        self.label_55 = QLabel(self.babyproducts)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.gridLayout_99.addWidget(self.label_55, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.babyproducts, 1, 3, 1, 1)

        self.pet = QWidget(self.categoryWrap)
        self.pet.setObjectName(u"pet")
        self.gridLayout_97 = QGridLayout(self.pet)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.label_49 = QLabel(self.pet)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u":/pic/pics/meo.ico"))
        self.label_49.setScaledContents(True)

        self.gridLayout_97.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_50 = QLabel(self.pet)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_97.addWidget(self.label_50, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.pet, 1, 0, 1, 1)

        self.electronics = QWidget(self.categoryWrap)
        self.electronics.setObjectName(u"electronics")
        self.gridLayout_10 = QGridLayout(self.electronics)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_2 = QLabel(self.electronics)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/pic/pics/electronics.ico"))
        self.label_2.setScaledContents(True)

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_9 = QLabel(self.electronics)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.electronics, 0, 0, 1, 1)

        self.toysNgame = QWidget(self.categoryWrap)
        self.toysNgame.setObjectName(u"toysNgame")
        self.gridLayout_92 = QGridLayout(self.toysNgame)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.label_43 = QLabel(self.toysNgame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setPixmap(QPixmap(u":/pic/pics/toys.ico"))
        self.label_43.setScaledContents(True)

        self.gridLayout_92.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_44 = QLabel(self.toysNgame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_92.addWidget(self.label_44, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.toysNgame, 0, 5, 1, 1)

        self.entertainment = QWidget(self.categoryWrap)
        self.entertainment.setObjectName(u"entertainment")
        self.gridLayout_93 = QGridLayout(self.entertainment)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.horizontalSpacer_15 = QSpacerItem(8, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_93.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.label_45 = QLabel(self.entertainment)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(60, 16777215))
        self.label_45.setPixmap(QPixmap(u":/pic/pics/entertainment.ico"))
        self.label_45.setScaledContents(True)

        self.gridLayout_93.addWidget(self.label_45, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_93.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.label_46 = QLabel(self.entertainment)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_93.addWidget(self.label_46, 1, 0, 1, 3)


        self.gridLayout_96.addWidget(self.entertainment, 0, 6, 1, 1)

        self.travel = QWidget(self.categoryWrap)
        self.travel.setObjectName(u"travel")
        self.gridLayout_101 = QGridLayout(self.travel)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.label_60 = QLabel(self.travel)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setPixmap(QPixmap(u":/pic/pics/travel.ico"))
        self.label_60.setScaledContents(True)

        self.gridLayout_101.addWidget(self.label_60, 0, 0, 1, 1)

        self.label_59 = QLabel(self.travel)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.gridLayout_101.addWidget(self.label_59, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.travel, 1, 5, 1, 1)

        self.arts = QWidget(self.categoryWrap)
        self.arts.setObjectName(u"arts")
        self.gridLayout_100 = QGridLayout(self.arts)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.label_58 = QLabel(self.arts)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setPixmap(QPixmap(u":/pic/pics/brush.ico"))
        self.label_58.setScaledContents(True)

        self.gridLayout_100.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_57 = QLabel(self.arts)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_100.addWidget(self.label_57, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.arts, 1, 4, 1, 1)

        self.homeNgarden = QWidget(self.categoryWrap)
        self.homeNgarden.setObjectName(u"homeNgarden")
        self.gridLayout_89 = QGridLayout(self.homeNgarden)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.label_37 = QLabel(self.homeNgarden)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 16777215))
        self.label_37.setPixmap(QPixmap(u":/pic/pics/house.ico"))
        self.label_37.setScaledContents(True)

        self.gridLayout_89.addWidget(self.label_37, 0, 1, 1, 1)

        self.label_38 = QLabel(self.homeNgarden)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_89.addWidget(self.label_38, 1, 0, 1, 3)


        self.gridLayout_96.addWidget(self.homeNgarden, 0, 2, 1, 1)

        self.fashions = QWidget(self.categoryWrap)
        self.fashions.setObjectName(u"fashions")
        self.gridLayout_88 = QGridLayout(self.fashions)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.label_36 = QLabel(self.fashions)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_88.addWidget(self.label_36, 1, 0, 1, 1)

        self.label_35 = QLabel(self.fashions)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setPixmap(QPixmap(u":/pic/pics/fashions.ico"))
        self.label_35.setScaledContents(True)

        self.gridLayout_88.addWidget(self.label_35, 0, 0, 1, 1)


        self.gridLayout_96.addWidget(self.fashions, 0, 1, 1, 1)

        self.officesupplies = QWidget(self.categoryWrap)
        self.officesupplies.setObjectName(u"officesupplies")
        self.gridLayout_95 = QGridLayout(self.officesupplies)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.label_52 = QLabel(self.officesupplies)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setPixmap(QPixmap(u":/pic/pics/officesupplies.ico"))
        self.label_52.setScaledContents(True)

        self.gridLayout_95.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_51 = QLabel(self.officesupplies)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_95.addWidget(self.label_51, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.officesupplies, 1, 1, 1, 1)

        self.beautyNhealth = QWidget(self.categoryWrap)
        self.beautyNhealth.setObjectName(u"beautyNhealth")
        self.gridLayout_90 = QGridLayout(self.beautyNhealth)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.label_40 = QLabel(self.beautyNhealth)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setPixmap(QPixmap(u":/pic/pics/beauty2.ico"))
        self.label_40.setScaledContents(True)

        self.gridLayout_90.addWidget(self.label_40, 0, 0, 1, 1)

        self.label_39 = QLabel(self.beautyNhealth)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_90.addWidget(self.label_39, 1, 0, 1, 1)


        self.gridLayout_96.addWidget(self.beautyNhealth, 0, 3, 1, 1)


        self.gridLayout_14.addWidget(self.categoryWrap, 1, 0, 1, 1)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
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
        self.profile.setMinimumSize(QSize(0, 0))
        self.gridLayout_6 = QGridLayout(self.profile)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_41 = QWidget(self.profile)
        self.widget_41.setObjectName(u"widget_41")
        self.gridLayout_104 = QGridLayout(self.widget_41)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.widget_84 = QWidget(self.widget_41)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setMaximumSize(QSize(800, 16777215))
        self.gridLayout_62 = QGridLayout(self.widget_84)
        self.gridLayout_62.setSpacing(0)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_4 = QStackedWidget(self.widget_84)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_105 = QGridLayout(self.page)
        self.gridLayout_105.setSpacing(0)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.gridLayout_105.setContentsMargins(0, 0, 0, 0)
        self.widget_42 = QWidget(self.page)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMinimumSize(QSize(0, 70))
        self.widget_42.setMaximumSize(QSize(16777215, 100))
        self.widget_42.setBaseSize(QSize(0, 0))
        self.gridLayout_58 = QGridLayout(self.widget_42)
        self.gridLayout_58.setSpacing(0)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_43 = QWidget(self.widget_42)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(87, 16777215))
        self.gridLayout_56 = QGridLayout(self.widget_43)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_43)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setPixmap(QPixmap(u":/ico/icon/profile.ico"))

        self.gridLayout_56.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_58.addWidget(self.widget_43, 0, 0, 1, 1)

        self.widget_44 = QWidget(self.widget_42)
        self.widget_44.setObjectName(u"widget_44")
        self.gridLayout_57 = QGridLayout(self.widget_44)
        self.gridLayout_57.setSpacing(0)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 0, 0, 0)
        self.accountUsername = QLabel(self.widget_44)
        self.accountUsername.setObjectName(u"accountUsername")
        self.accountUsername.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_57.addWidget(self.accountUsername, 0, 0, 1, 1)


        self.gridLayout_58.addWidget(self.widget_44, 0, 1, 1, 1)


        self.gridLayout_105.addWidget(self.widget_42, 0, 0, 1, 1)

        self.widget_45 = QWidget(self.page)
        self.widget_45.setObjectName(u"widget_45")
        self.gridLayout_61 = QGridLayout(self.widget_45)
        self.gridLayout_61.setSpacing(0)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widget_45)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_59 = QGridLayout(self.widget_46)
        self.gridLayout_59.setSpacing(0)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_46)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 40))
        self.label_25.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_59.addWidget(self.label_25, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.widget_46, 0, 0, 1, 1)

        self.widget_47 = QWidget(self.widget_45)
        self.widget_47.setObjectName(u"widget_47")
        self.gridLayout_60 = QGridLayout(self.widget_47)
        self.gridLayout_60.setSpacing(0)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.sellingList = QWidget(self.widget_47)
        self.sellingList.setObjectName(u"sellingList")
        self.gridLayout_103 = QGridLayout(self.sellingList)
        self.gridLayout_103.setSpacing(0)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.productEditTable = QTableWidget(self.sellingList)
        self.productEditTable.setObjectName(u"productEditTable")

        self.gridLayout_103.addWidget(self.productEditTable, 0, 0, 1, 1)


        self.gridLayout_60.addWidget(self.sellingList, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.widget_47, 1, 0, 1, 1)


        self.gridLayout_105.addWidget(self.widget_45, 1, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page)
        self.editPro = QWidget()
        self.editPro.setObjectName(u"editPro")
        self.gridLayout_115 = QGridLayout(self.editPro)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.label_23 = QLabel(self.editPro)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 16pt \"Josefin Sans SemiBold\";")

        self.gridLayout_115.addWidget(self.label_23, 0, 0, 1, 1)

        self.widget_85 = QWidget(self.editPro)
        self.widget_85.setObjectName(u"widget_85")
        self.gridLayout_106 = QGridLayout(self.widget_85)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.label_24 = QLabel(self.widget_85)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_106.addWidget(self.label_24, 0, 0, 1, 1)

        self.proTitleEdit = QLineEdit(self.widget_85)
        self.proTitleEdit.setObjectName(u"proTitleEdit")
        self.proTitleEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_106.addWidget(self.proTitleEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_85, 1, 0, 1, 1)

        self.widget_86 = QWidget(self.editPro)
        self.widget_86.setObjectName(u"widget_86")
        self.gridLayout_107 = QGridLayout(self.widget_86)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.label_63 = QLabel(self.widget_86)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_107.addWidget(self.label_63, 0, 0, 1, 1)

        self.cateProEdit = QComboBox(self.widget_86)
        self.cateProEdit.setObjectName(u"cateProEdit")
        self.cateProEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_107.addWidget(self.cateProEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_86, 2, 0, 1, 1)

        self.widget_87 = QWidget(self.editPro)
        self.widget_87.setObjectName(u"widget_87")
        self.gridLayout_108 = QGridLayout(self.widget_87)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.label_64 = QLabel(self.widget_87)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_108.addWidget(self.label_64, 0, 0, 1, 1)

        self.priceProEdit = QLineEdit(self.widget_87)
        self.priceProEdit.setObjectName(u"priceProEdit")
        self.priceProEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_108.addWidget(self.priceProEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_87, 3, 0, 1, 1)

        self.widget_90 = QWidget(self.editPro)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMaximumSize(QSize(16777215, 100))
        self.gridLayout_110 = QGridLayout(self.widget_90)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.label_66 = QLabel(self.widget_90)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")
        self.label_66.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_110.addWidget(self.label_66, 0, 0, 1, 1)

        self.descProEdit = QPlainTextEdit(self.widget_90)
        self.descProEdit.setObjectName(u"descProEdit")
        self.descProEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_110.addWidget(self.descProEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_90, 5, 0, 1, 1)

        self.widget_91 = QWidget(self.editPro)
        self.widget_91.setObjectName(u"widget_91")
        self.gridLayout_111 = QGridLayout(self.widget_91)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.label_67 = QLabel(self.widget_91)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_111.addWidget(self.label_67, 0, 0, 1, 1)

        self.locaProEdit = QLineEdit(self.widget_91)
        self.locaProEdit.setObjectName(u"locaProEdit")
        self.locaProEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_111.addWidget(self.locaProEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_91, 6, 0, 1, 1)

        self.widget_92 = QWidget(self.editPro)
        self.widget_92.setObjectName(u"widget_92")
        self.gridLayout_112 = QGridLayout(self.widget_92)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.label_68 = QLabel(self.widget_92)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_112.addWidget(self.label_68, 0, 0, 1, 1)

        self.amountProEdit = QSpinBox(self.widget_92)
        self.amountProEdit.setObjectName(u"amountProEdit")
        self.amountProEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_112.addWidget(self.amountProEdit, 0, 1, 1, 1)


        self.gridLayout_115.addWidget(self.widget_92, 7, 0, 1, 1)

        self.widget_93 = QWidget(self.editPro)
        self.widget_93.setObjectName(u"widget_93")
        self.gridLayout_117 = QGridLayout(self.widget_93)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.gridLayout_117.setVerticalSpacing(7)
        self.widget_95 = QWidget(self.widget_93)
        self.widget_95.setObjectName(u"widget_95")
        self.gridLayout_114 = QGridLayout(self.widget_95)
        self.gridLayout_114.setSpacing(0)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gridLayout_114.setContentsMargins(0, 0, 0, 0)
        self.deleteProduct = QPushButton(self.widget_95)
        self.deleteProduct.setObjectName(u"deleteProduct")
        self.deleteProduct.setMinimumSize(QSize(70, 30))
        self.deleteProduct.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_114.addWidget(self.deleteProduct, 0, 0, 1, 1)


        self.gridLayout_117.addWidget(self.widget_95, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(581, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_117.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)

        self.widget_94 = QWidget(self.widget_93)
        self.widget_94.setObjectName(u"widget_94")
        self.gridLayout_113 = QGridLayout(self.widget_94)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.gridLayout_113.setHorizontalSpacing(40)
        self.cancelProEdit = QPushButton(self.widget_94)
        self.cancelProEdit.setObjectName(u"cancelProEdit")
        self.cancelProEdit.setMinimumSize(QSize(70, 30))
        self.cancelProEdit.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_113.addWidget(self.cancelProEdit, 0, 0, 1, 1)

        self.doneProEdit = QPushButton(self.widget_94)
        self.doneProEdit.setObjectName(u"doneProEdit")
        self.doneProEdit.setMinimumSize(QSize(70, 30))
        self.doneProEdit.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_113.addWidget(self.doneProEdit, 0, 1, 1, 1)


        self.gridLayout_117.addWidget(self.widget_94, 0, 2, 1, 1)


        self.gridLayout_115.addWidget(self.widget_93, 8, 0, 1, 1)

        self.widget_88 = QWidget(self.editPro)
        self.widget_88.setObjectName(u"widget_88")
        self.gridLayout_116 = QGridLayout(self.widget_88)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.widget_89 = QWidget(self.widget_88)
        self.widget_89.setObjectName(u"widget_89")
        self.gridLayout_109 = QGridLayout(self.widget_89)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.label_65 = QLabel(self.widget_89)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 16777215))
        self.label_65.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_109.addWidget(self.label_65, 0, 0, 1, 1)


        self.gridLayout_116.addWidget(self.widget_89, 0, 0, 1, 1)

        self.photoHolder = QWidget(self.widget_88)
        self.photoHolder.setObjectName(u"photoHolder")
        self.photoHolder.setMinimumSize(QSize(100, 100))
        self.photoHolder.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_116.addWidget(self.photoHolder, 0, 1, 1, 1)

        self.uploadEditImg = QPushButton(self.widget_88)
        self.uploadEditImg.setObjectName(u"uploadEditImg")
        self.uploadEditImg.setMinimumSize(QSize(0, 30))
        self.uploadEditImg.setMaximumSize(QSize(116, 16777215))
        self.uploadEditImg.setSizeIncrement(QSize(0, 0))
        self.uploadEditImg.setStyleSheet(u"background-color: #e8e8e8;\n"
"border-radius: 5px;\n"
"color: #51526C;\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"\n"
"")

        self.gridLayout_116.addWidget(self.uploadEditImg, 0, 2, 1, 1)


        self.gridLayout_115.addWidget(self.widget_88, 4, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.editPro)

        self.gridLayout_62.addWidget(self.stackedWidget_4, 0, 0, 1, 1)


        self.gridLayout_104.addWidget(self.widget_84, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_41, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.profile)
        self.acc = QWidget()
        self.acc.setObjectName(u"acc")
        self.gridLayout_3 = QGridLayout(self.acc)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_68 = QWidget(self.acc)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setMaximumSize(QSize(800, 16777215))
        self.gridLayout_84 = QGridLayout(self.widget_68)
        self.gridLayout_84.setSpacing(0)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_84.setContentsMargins(0, 0, 0, 0)
        self.widget_48 = QWidget(self.widget_68)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 100))
        self.gridLayout_67 = QGridLayout(self.widget_48)
        self.gridLayout_67.setSpacing(0)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.gridLayout_65 = QGridLayout(self.widget_49)
        self.gridLayout_65.setSpacing(0)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_49)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 16pt \"Josefin Sans SemiBold\";")

        self.gridLayout_65.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_67.addWidget(self.widget_49, 0, 0, 1, 1)

        self.widget_50 = QWidget(self.widget_48)
        self.widget_50.setObjectName(u"widget_50")
        self.gridLayout_66 = QGridLayout(self.widget_50)
        self.gridLayout_66.setSpacing(0)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setContentsMargins(0, 0, 0, 0)
        self.widget_51 = QWidget(self.widget_50)
        self.widget_51.setObjectName(u"widget_51")
        self.gridLayout_63 = QGridLayout(self.widget_51)
        self.gridLayout_63.setSpacing(0)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.widget_51)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_63.addWidget(self.label_26, 0, 0, 1, 1)

        self.showUsername = QLabel(self.widget_51)
        self.showUsername.setObjectName(u"showUsername")
        self.showUsername.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_63.addWidget(self.showUsername, 0, 1, 1, 1)


        self.gridLayout_66.addWidget(self.widget_51, 0, 0, 1, 1)

        self.widget_52 = QWidget(self.widget_50)
        self.widget_52.setObjectName(u"widget_52")
        self.gridLayout_64 = QGridLayout(self.widget_52)
        self.gridLayout_64.setSpacing(0)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_52)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_64.addWidget(self.label_28, 0, 0, 1, 1)

        self.showID = QLabel(self.widget_52)
        self.showID.setObjectName(u"showID")
        self.showID.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_64.addWidget(self.showID, 0, 1, 1, 1)


        self.gridLayout_66.addWidget(self.widget_52, 1, 0, 1, 1)


        self.gridLayout_67.addWidget(self.widget_50, 0, 1, 1, 1)


        self.gridLayout_84.addWidget(self.widget_48, 0, 0, 1, 1)

        self.widget_53 = QWidget(self.widget_68)
        self.widget_53.setObjectName(u"widget_53")
        self.gridLayout_82 = QGridLayout(self.widget_53)
        self.gridLayout_82.setSpacing(0)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.gridLayout_82.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.widget_53)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.myProfile = QWidget()
        self.myProfile.setObjectName(u"myProfile")
        self.gridLayout_83 = QGridLayout(self.myProfile)
        self.gridLayout_83.setSpacing(0)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setContentsMargins(0, 0, 0, 0)
        self.widget_63 = QWidget(self.myProfile)
        self.widget_63.setObjectName(u"widget_63")
        sizePolicy2.setHeightForWidth(self.widget_63.sizePolicy().hasHeightForWidth())
        self.widget_63.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setStrikeOut(False)
        self.widget_63.setFont(font3)
        self.widget_63.setStyleSheet(u"")
        self.gridLayout_71 = QGridLayout(self.widget_63)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.widget_57 = QWidget(self.widget_63)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setMinimumSize(QSize(0, 70))
        self.widget_57.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_68 = QGridLayout(self.widget_57)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.showName = QLabel(self.widget_57)
        self.showName.setObjectName(u"showName")
        self.showName.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_68.addWidget(self.showName, 0, 1, 1, 1)

        self.label_31 = QLabel(self.widget_57)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(300, 16777215))
        self.label_31.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_68.addWidget(self.label_31, 0, 0, 1, 1)


        self.gridLayout_71.addWidget(self.widget_57, 0, 0, 1, 1)

        self.widget_58 = QWidget(self.widget_63)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setMinimumSize(QSize(0, 70))
        self.widget_58.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_69 = QGridLayout(self.widget_58)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.label_32 = QLabel(self.widget_58)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(300, 16777215))
        self.label_32.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_69.addWidget(self.label_32, 0, 0, 1, 1)

        self.showEmail = QLabel(self.widget_58)
        self.showEmail.setObjectName(u"showEmail")
        self.showEmail.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_69.addWidget(self.showEmail, 0, 1, 1, 1)


        self.gridLayout_71.addWidget(self.widget_58, 1, 0, 1, 1)

        self.widget_60 = QWidget(self.widget_63)
        self.widget_60.setObjectName(u"widget_60")
        self.widget_60.setMinimumSize(QSize(0, 70))
        self.widget_60.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_70 = QGridLayout(self.widget_60)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.label_33 = QLabel(self.widget_60)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(300, 16777215))
        self.label_33.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_70.addWidget(self.label_33, 0, 0, 1, 1)

        self.showBirth = QLabel(self.widget_60)
        self.showBirth.setObjectName(u"showBirth")
        self.showBirth.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_70.addWidget(self.showBirth, 0, 1, 1, 1)


        self.gridLayout_71.addWidget(self.widget_60, 2, 0, 1, 1)

        self.widget_61 = QWidget(self.widget_63)
        self.widget_61.setObjectName(u"widget_61")
        self.widget_61.setMinimumSize(QSize(0, 70))
        self.widget_61.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_72 = QGridLayout(self.widget_61)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.label_34 = QLabel(self.widget_61)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(300, 16777215))
        self.label_34.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_72.addWidget(self.label_34, 0, 0, 1, 1)

        self.showPhone = QLabel(self.widget_61)
        self.showPhone.setObjectName(u"showPhone")
        self.showPhone.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_72.addWidget(self.showPhone, 0, 1, 1, 1)


        self.gridLayout_71.addWidget(self.widget_61, 3, 0, 1, 1)

        self.widget_32 = QWidget(self.widget_63)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMaximumSize(QSize(16777215, 70))
        self.gridLayout_41 = QGridLayout(self.widget_32)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_10 = QLabel(self.widget_32)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(300, 0))
        self.label_10.setMaximumSize(QSize(0, 16777215))
        self.label_10.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_41.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedWidget_3 = QStackedWidget(self.widget_32)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.optPass = QWidget()
        self.optPass.setObjectName(u"optPass")
        self.gridLayout_76 = QGridLayout(self.optPass)
        self.gridLayout_76.setSpacing(0)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setContentsMargins(0, 0, 0, 0)
        self.showPassword = QLabel(self.optPass)
        self.showPassword.setObjectName(u"showPassword")
        self.showPassword.setStyleSheet(u"font: 500 10pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_76.addWidget(self.showPassword, 0, 0, 1, 1)

        self.changePassBtn = QPushButton(self.optPass)
        self.changePassBtn.setObjectName(u"changePassBtn")
        self.changePassBtn.setMaximumSize(QSize(121, 16777215))
        self.changePassBtn.setStyleSheet(u"color: red;\n"
"font: 500 10pt \"Josefin Sans Medium\";")
        self.changePassBtn.setIconSize(QSize(12, 16))
        self.changePassBtn.setFlat(True)

        self.gridLayout_76.addWidget(self.changePassBtn, 0, 1, 1, 1)

        self.stackedWidget_3.addWidget(self.optPass)
        self.changingPass = QWidget()
        self.changingPass.setObjectName(u"changingPass")
        self.gridLayout_87 = QGridLayout(self.changingPass)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.passLineEdit = QLineEdit(self.changingPass)
        self.passLineEdit.setObjectName(u"passLineEdit")
        self.passLineEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_87.addWidget(self.passLineEdit, 0, 0, 1, 1)

        self.widget_62 = QWidget(self.changingPass)
        self.widget_62.setObjectName(u"widget_62")
        self.gridLayout_80 = QGridLayout(self.widget_62)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.gridLayout_80.setHorizontalSpacing(10)
        self.gridLayout_80.setVerticalSpacing(0)
        self.gridLayout_80.setContentsMargins(0, 0, 0, 0)
        self.cancelChangePass = QPushButton(self.widget_62)
        self.cancelChangePass.setObjectName(u"cancelChangePass")
        self.cancelChangePass.setMinimumSize(QSize(70, 30))
        self.cancelChangePass.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_80.addWidget(self.cancelChangePass, 0, 0, 1, 1)

        self.confirmChangePass = QPushButton(self.widget_62)
        self.confirmChangePass.setObjectName(u"confirmChangePass")
        self.confirmChangePass.setMinimumSize(QSize(70, 30))
        self.confirmChangePass.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_80.addWidget(self.confirmChangePass, 0, 1, 1, 1)


        self.gridLayout_87.addWidget(self.widget_62, 0, 1, 1, 1)

        self.stackedWidget_3.addWidget(self.changingPass)

        self.gridLayout_41.addWidget(self.stackedWidget_3, 0, 1, 1, 1)


        self.gridLayout_71.addWidget(self.widget_32, 4, 0, 1, 1)

        self.widget_55 = QWidget(self.widget_63)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setStyleSheet(u"")
        self.gridLayout_74 = QGridLayout(self.widget_55)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.horizontalSpacer_9 = QSpacerItem(685, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_74.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.profileEditBtn = QPushButton(self.widget_55)
        self.profileEditBtn.setObjectName(u"profileEditBtn")
        self.profileEditBtn.setMinimumSize(QSize(70, 30))
        self.profileEditBtn.setMaximumSize(QSize(70, 16777215))
        self.profileEditBtn.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_74.addWidget(self.profileEditBtn, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 212, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_74.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.gridLayout_71.addWidget(self.widget_55, 5, 0, 1, 1)


        self.gridLayout_83.addWidget(self.widget_63, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.myProfile)
        self.editInfo = QWidget()
        self.editInfo.setObjectName(u"editInfo")
        self.gridLayout_81 = QGridLayout(self.editInfo)
        self.gridLayout_81.setSpacing(0)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(0, 0, 0, 0)
        self.widget_56 = QWidget(self.editInfo)
        self.widget_56.setObjectName(u"widget_56")
        self.gridLayout_86 = QGridLayout(self.widget_56)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.widget_69 = QWidget(self.widget_56)
        self.widget_69.setObjectName(u"widget_69")
        self.gridLayout_85 = QGridLayout(self.widget_69)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.cancelEdit = QPushButton(self.widget_69)
        self.cancelEdit.setObjectName(u"cancelEdit")
        self.cancelEdit.setMinimumSize(QSize(0, 30))
        self.cancelEdit.setMaximumSize(QSize(70, 16777215))
        self.cancelEdit.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_85.addWidget(self.cancelEdit, 0, 0, 1, 1)

        self.confirmEdit = QPushButton(self.widget_69)
        self.confirmEdit.setObjectName(u"confirmEdit")
        self.confirmEdit.setMinimumSize(QSize(0, 30))
        self.confirmEdit.setMaximumSize(QSize(70, 16777215))
        self.confirmEdit.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_85.addWidget(self.confirmEdit, 0, 1, 1, 1)


        self.gridLayout_86.addWidget(self.widget_69, 4, 0, 1, 1)

        self.widget_65 = QWidget(self.widget_56)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setMinimumSize(QSize(0, 70))
        self.widget_65.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_78 = QGridLayout(self.widget_65)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.label_29 = QLabel(self.widget_65)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(300, 0))
        self.label_29.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_78.addWidget(self.label_29, 0, 0, 1, 1)

        self.birthEdit = QLineEdit(self.widget_65)
        self.birthEdit.setObjectName(u"birthEdit")
        self.birthEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_78.addWidget(self.birthEdit, 0, 1, 1, 1)


        self.gridLayout_86.addWidget(self.widget_65, 2, 0, 1, 1)

        self.widget_64 = QWidget(self.widget_56)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setMinimumSize(QSize(0, 70))
        self.widget_64.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_77 = QGridLayout(self.widget_64)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.label_27 = QLabel(self.widget_64)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(300, 0))
        self.label_27.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_77.addWidget(self.label_27, 0, 0, 1, 1)

        self.emailEdit = QLineEdit(self.widget_64)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_77.addWidget(self.emailEdit, 0, 1, 1, 1)


        self.gridLayout_86.addWidget(self.widget_64, 1, 0, 1, 1)

        self.widget_59 = QWidget(self.widget_56)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setMinimumSize(QSize(0, 70))
        self.widget_59.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_75 = QGridLayout(self.widget_59)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.label_14 = QLabel(self.widget_59)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(300, 0))
        self.label_14.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_75.addWidget(self.label_14, 0, 0, 1, 1)

        self.nameEdit = QLineEdit(self.widget_59)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_75.addWidget(self.nameEdit, 0, 1, 1, 1)


        self.gridLayout_86.addWidget(self.widget_59, 0, 0, 1, 1)

        self.widget_66 = QWidget(self.widget_56)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setMinimumSize(QSize(0, 70))
        self.widget_66.setMaximumSize(QSize(16777215, 58))
        self.gridLayout_79 = QGridLayout(self.widget_66)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.label_30 = QLabel(self.widget_66)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(300, 0))
        self.label_30.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);")

        self.gridLayout_79.addWidget(self.label_30, 0, 0, 1, 1)

        self.phoneEdit = QLineEdit(self.widget_66)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setStyleSheet(u"background-color: #e8e8e8;\n"
"color: rgb(232, 232, 232);\n"
"border-radius: 5px;\n"
"color: rgb(0,0,0);")

        self.gridLayout_79.addWidget(self.phoneEdit, 0, 1, 1, 1)


        self.gridLayout_86.addWidget(self.widget_66, 3, 0, 1, 1)


        self.gridLayout_81.addWidget(self.widget_56, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.editInfo)

        self.gridLayout_82.addWidget(self.stackedWidget_2, 0, 0, 1, 1)


        self.gridLayout_84.addWidget(self.widget_53, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_68, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.acc)
        self.searchCategory = QWidget()
        self.searchCategory.setObjectName(u"searchCategory")
        self.gridLayout_4 = QGridLayout(self.searchCategory)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_67 = QWidget(self.searchCategory)
        self.widget_67.setObjectName(u"widget_67")
        self.widget_67.setMaximumSize(QSize(900, 16777215))
        self.gridLayout_123 = QGridLayout(self.widget_67)
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.widget_70 = QWidget(self.widget_67)
        self.widget_70.setObjectName(u"widget_70")
        self.widget_70.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_121 = QGridLayout(self.widget_70)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.searchCate = QLabel(self.widget_70)
        self.searchCate.setObjectName(u"searchCate")

        self.gridLayout_121.addWidget(self.searchCate, 0, 0, 1, 1)


        self.gridLayout_123.addWidget(self.widget_70, 0, 0, 1, 1)

        self.widget_71 = QWidget(self.widget_67)
        self.widget_71.setObjectName(u"widget_71")
        self.widget_71.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_122 = QGridLayout(self.widget_71)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.cateItemFound = QLabel(self.widget_71)
        self.cateItemFound.setObjectName(u"cateItemFound")

        self.gridLayout_122.addWidget(self.cateItemFound, 0, 0, 1, 1)


        self.gridLayout_123.addWidget(self.widget_71, 1, 0, 1, 1)

        self.categoryProductList = QWidget(self.widget_67)
        self.categoryProductList.setObjectName(u"categoryProductList")

        self.gridLayout_123.addWidget(self.categoryProductList, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_67, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.searchCategory)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.changeBtn_1.toggled.connect(self.icon_only_widget.setVisible)
        self.changeBtn_1.toggled.connect(self.full_menu_widget.setHidden)
        self.homeBtn_1.toggled.connect(self.homeBtn_2.setChecked)
        self.homeBtn_2.toggled.connect(self.homeBtn_1.setChecked)
        self.profileBtn_1.toggled.connect(self.profileBtn_2.setChecked)
        self.accountBtn_1.toggled.connect(self.accountBtn_2.setChecked)
        self.profileBtn_2.toggled.connect(self.profileBtn_1.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn_1.setChecked)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homeBtn_1.setText("")
        self.profileBtn_1.setText("")
        self.accountBtn_1.setText("")
        self.exitBtn_1.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MarketNest", None))
        self.homeBtn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profileBtn_2.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"Edit Account", None))
        self.exitBtn_2.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.changeBtn_1.setText("")
        self.searchBtn_1.setText("")
        self.sellBtn_1.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Product Title", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Product Photo", None))
        self.uploadPhotoBtn.setText(QCoreApplication.translate("MainWindow", u"+ Upload Photo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Product Description", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.doneAddBtn_1.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.product_img.setText(QCoreApplication.translate("MainWindow", u"img", None))
        self.pushButton.setText("")
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_69.setText("")
        self.phoneLabel.setText(QCoreApplication.translate("MainWindow", u"phone num", None))
        self.product_price.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.product_name.setText(QCoreApplication.translate("MainWindow", u"product name", None))
        self.sellerNameLabel.setText(QCoreApplication.translate("MainWindow", u"Seller", None))
        self.sellerProfileLabel.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.addressLabel.setText(QCoreApplication.translate("MainWindow", u"location", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Product Specification", None))
        self.categoryLabel.setText(QCoreApplication.translate("MainWindow", u"category details", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.productDescLabel.setText(QCoreApplication.translate("MainWindow", u"details", None))
        self.totalItemFound.setText(QCoreApplication.translate("MainWindow", u"total item", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Search for:", None))
        self.topicSearch.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.banner.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Sports and Outdoors", None))
        self.label_41.setText("")
        self.label_62.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Personalized Gifts", None))
        self.label_48.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Automotive", None))
        self.label_54.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.label_56.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Baby Products", None))
        self.label_49.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Pet Supplies", None))
        self.label_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Electronics", None))
        self.label_43.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Toys and Games", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.label_60.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Travel", None))
        self.label_58.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Art and Collectibles", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Home and Garden", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Fashions", None))
        self.label_35.setText("")
        self.label_52.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Office Supplies", None))
        self.label_40.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Beauty and Health", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"My Favorites", None))
        self.label_8.setText("")
        self.accountUsername.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Marketplace", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Edit Product", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Product Title", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.deleteProduct.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.cancelProEdit.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.doneProEdit.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Photo", None))
        self.uploadEditImg.setText(QCoreApplication.translate("MainWindow", u"+ Upload Photo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Edit Account", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.showUsername.setText(QCoreApplication.translate("MainWindow", u"John Doe", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Member ID", None))
        self.showID.setText(QCoreApplication.translate("MainWindow", u"5555555", None))
        self.showName.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.showEmail.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.showBirth.setText(QCoreApplication.translate("MainWindow", u"birthdate", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.showPhone.setText(QCoreApplication.translate("MainWindow", u"phone num", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.showPassword.setText(QCoreApplication.translate("MainWindow", u"pass", None))
        self.changePassBtn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.cancelChangePass.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirmChangePass.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.profileEditBtn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.cancelEdit.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirmEdit.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.searchCate.setText(QCoreApplication.translate("MainWindow", u"cate", None))
        self.cateItemFound.setText(QCoreApplication.translate("MainWindow", u"item num", None))
    # retranslateUi

