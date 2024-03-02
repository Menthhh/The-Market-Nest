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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 765)
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
"\n"
"* {\n"
"	color: #51526C;\n"
"}\n"
"\n"
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
        self.label.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeBtn_1 = QPushButton(self.icon_only_widget)
        self.homeBtn_1.setObjectName(u"homeBtn_1")
        icon = QIcon()
        icon.addFile(u":/icon/icon/home.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn_1.setIcon(icon)
        self.homeBtn_1.setCheckable(True)
        self.homeBtn_1.setAutoExclusive(True)
        self.homeBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.homeBtn_1)

        self.cartBtn_1 = QPushButton(self.icon_only_widget)
        self.cartBtn_1.setObjectName(u"cartBtn_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/heart3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cartBtn_1.setIcon(icon1)
        self.cartBtn_1.setCheckable(True)
        self.cartBtn_1.setAutoExclusive(True)
        self.cartBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.cartBtn_1)

        self.pushButton = QPushButton(self.icon_only_widget)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/store.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton)

        self.profileBtn_1 = QPushButton(self.icon_only_widget)
        self.profileBtn_1.setObjectName(u"profileBtn_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/profile.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn_1.setIcon(icon3)
        self.profileBtn_1.setFlat(True)

        self.verticalLayout.addWidget(self.profileBtn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(47, 509, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exitBtn_1 = QPushButton(self.icon_only_widget)
        self.exitBtn_1.setObjectName(u"exitBtn_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/logout.ico", QSize(), QIcon.Normal, QIcon.Off)
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

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#cart,home,order,search,user{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"#widget_2{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_9 = QGridLayout(self.home)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.home_container = QWidget(self.home)
        self.home_container.setObjectName(u"home_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_container.sizePolicy().hasHeightForWidth())
        self.home_container.setSizePolicy(sizePolicy)
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
        self.scrollHome.setGeometry(QRect(0, 0, 666, 723))
        self.gridLayout_2 = QGridLayout(self.scrollHome)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.scrollHome)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_14 = QGridLayout(self.widget_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Banner = QWidget(self.widget_3)
        self.Banner.setObjectName(u"Banner")
        self.gridLayout_11 = QGridLayout(self.Banner)
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
        font = QFont()
        font.setFamilies([u"Aksaramatee"])
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)

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
        self.cart = QWidget()
        self.cart.setObjectName(u"cart")
        self.gridLayout_3 = QGridLayout(self.cart)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.cart)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.cart)
        self.order = QWidget()
        self.order.setObjectName(u"order")
        self.gridLayout_4 = QGridLayout(self.order)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.order)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.order)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.gridLayout_5 = QGridLayout(self.search)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.search)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.search)
        self.user = QWidget()
        self.user.setObjectName(u"user")
        self.gridLayout_6 = QGridLayout(self.user)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.user)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.user)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main, 0, 2, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.full_menu_widget.sizePolicy().hasHeightForWidth())
        self.full_menu_widget.setSizePolicy(sizePolicy1)
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
        font1 = QFont()
        font1.setFamilies([u"Josefin Sans SemiBold"])
        font1.setBold(True)
        self.label_3.setFont(font1)

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
        self.homeBtn_2.setIcon(icon)
        self.homeBtn_2.setCheckable(True)
        self.homeBtn_2.setAutoExclusive(True)
        self.homeBtn_2.setAutoDefault(False)
        self.homeBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.homeBtn_2)

        self.cartBtn_2 = QPushButton(self.full_menu_widget)
        self.cartBtn_2.setObjectName(u"cartBtn_2")
        self.cartBtn_2.setIcon(icon1)
        self.cartBtn_2.setCheckable(True)
        self.cartBtn_2.setAutoExclusive(True)
        self.cartBtn_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.cartBtn_2)

        self.storeBtn_1 = QPushButton(self.full_menu_widget)
        self.storeBtn_1.setObjectName(u"storeBtn_1")
        self.storeBtn_1.setIcon(icon2)
        self.storeBtn_1.setFlat(True)

        self.verticalLayout_2.addWidget(self.storeBtn_1)

        self.pushButton_2 = QPushButton(self.full_menu_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(117, 509, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exitBtn_2 = QPushButton(self.full_menu_widget)
        self.exitBtn_2.setObjectName(u"exitBtn_2")
        font2 = QFont()
        font2.setFamilies([u"Josefin Sans Medium"])
        self.exitBtn_2.setFont(font2)
        self.exitBtn_2.setIcon(icon4)
        self.exitBtn_2.setFlat(True)

        self.verticalLayout_4.addWidget(self.exitBtn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.changeBtn_1.toggled.connect(self.icon_only_widget.setVisible)
        self.changeBtn_1.toggled.connect(self.full_menu_widget.setHidden)
        self.homeBtn_1.toggled.connect(self.homeBtn_2.setChecked)
        self.homeBtn_2.toggled.connect(self.homeBtn_1.setChecked)
        self.exitBtn_2.clicked.connect(MainWindow.close)
        self.exitBtn_1.clicked.connect(MainWindow.close)
        self.cartBtn_1.toggled.connect(self.cartBtn_2.setChecked)
        self.cartBtn_2.toggled.connect(self.cartBtn_1.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.homeBtn_1.setText("")
        self.cartBtn_1.setText("")
        self.pushButton.setText("")
        self.profileBtn_1.setText("")
        self.exitBtn_1.setText("")
        self.changeBtn_1.setText("")
        self.searchBtn_1.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"a banner", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Caregory", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cart Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Order Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Search Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"User Page", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MarketNest", None))
        self.homeBtn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.cartBtn_2.setText(QCoreApplication.translate("MainWindow", u"Favorite", None))
        self.storeBtn_1.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit Account", None))
        self.exitBtn_2.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
    # retranslateUi

