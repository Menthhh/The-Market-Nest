# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminUi.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)
import resource_rc

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(1160, 706)
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_23 = QGridLayout(self.centralwidget)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.fullWid = QWidget(self.centralwidget)
        self.fullWid.setObjectName(u"fullWid")
        self.gridLayout_4 = QGridLayout(self.fullWid)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.fullWid)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_2 = QGridLayout(self.widget_6)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 20)
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_6, 0, 0, 1, 1)

        self.admiBtn_2 = QPushButton(self.fullWid)
        self.admiBtn_2.setObjectName(u"admiBtn_2")
        self.admiBtn_2.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"text-align: left;\n"
"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/icon/icon/profile.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.admiBtn_2.setIcon(icon)
        self.admiBtn_2.setCheckable(True)
        self.admiBtn_2.setAutoExclusive(True)
        self.admiBtn_2.setFlat(True)

        self.gridLayout_4.addWidget(self.admiBtn_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 365, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.logoutBtn_2 = QPushButton(self.fullWid)
        self.logoutBtn_2.setObjectName(u"logoutBtn_2")
        self.logoutBtn_2.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"text-align: left;\n"
"background-color: transparent;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/logout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn_2.setIcon(icon1)
        self.logoutBtn_2.setFlat(True)

        self.gridLayout_4.addWidget(self.logoutBtn_2, 5, 0, 1, 1)

        self.mtnBtn_2 = QPushButton(self.fullWid)
        self.mtnBtn_2.setObjectName(u"mtnBtn_2")
        self.mtnBtn_2.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"text-align: left;\n"
"background-color: transparent;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/maintenace.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.mtnBtn_2.setIcon(icon2)
        self.mtnBtn_2.setCheckable(True)
        self.mtnBtn_2.setAutoExclusive(True)
        self.mtnBtn_2.setFlat(True)

        self.gridLayout_4.addWidget(self.mtnBtn_2, 2, 0, 1, 1)

        self.dashBtn_2 = QPushButton(self.fullWid)
        self.dashBtn_2.setObjectName(u"dashBtn_2")
        self.dashBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.dashBtn_2.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"text-align: left;\n"
"background-color: transparent;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/dashboard.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.dashBtn_2.setIcon(icon3)
        self.dashBtn_2.setCheckable(True)
        self.dashBtn_2.setAutoExclusive(True)
        self.dashBtn_2.setFlat(True)

        self.gridLayout_4.addWidget(self.dashBtn_2, 1, 0, 1, 1)


        self.gridLayout_23.addWidget(self.fullWid, 0, 1, 2, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_19 = QGridLayout(self.widget_4)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_7 = QGridLayout(self.widget_5)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_5 = QGridLayout(self.widget_7)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toggleBtn = QPushButton(self.widget_7)
        self.toggleBtn.setObjectName(u"toggleBtn")
        self.toggleBtn.setStyleSheet(u"background-color: transparent;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleBtn.setIcon(icon4)
        self.toggleBtn.setCheckable(True)
        self.toggleBtn.setFlat(True)

        self.gridLayout_5.addWidget(self.toggleBtn, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_7, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(320, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.widget_8, 0, 2, 1, 1)


        self.gridLayout_19.addWidget(self.widget_5, 0, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget_4, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: 0px")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_21 = QGridLayout(self.dashboard)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dashboard)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 984, 682))
        self.gridLayout_20 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget_20 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_18 = QGridLayout(self.widget_20)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 40))
        self.label_15.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 16pt \"Josefin Sans SemiBold\";")

        self.gridLayout_18.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget_20, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_10 = QGridLayout(self.widget_9)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 30))
        self.gridLayout_12 = QGridLayout(self.widget_10)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_10)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(131, 16777215))
        self.gridLayout_8 = QGridLayout(self.widget_15)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 13pt \"Josefin Sans SemiBold\";")

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_16 = QWidget(self.widget_10)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_11 = QGridLayout(self.widget_16)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.showTotalAcc = QLabel(self.widget_16)
        self.showTotalAcc.setObjectName(u"showTotalAcc")
        self.showTotalAcc.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 9pt \"Josefin Sans SemiBold\";")

        self.gridLayout_11.addWidget(self.showTotalAcc, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_16, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_10, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 200))
        self.gridLayout_9 = QGridLayout(self.widget_11)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_13 = QGridLayout(self.widget_12)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 13pt \"Josefin Sans SemiBold\";")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)

        self.showBuySell = QFrame(self.widget_12)
        self.showBuySell.setObjectName(u"showBuySell")

        self.gridLayout_13.addWidget(self.showBuySell, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_12, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.widget_11)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_14 = QGridLayout(self.widget_14)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 13pt \"Josefin Sans SemiBold\";")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_14.addWidget(self.label_10, 0, 0, 1, 1)

        self.showAvgProduct = QFrame(self.widget_14)
        self.showAvgProduct.setObjectName(u"showAvgProduct")
        self.showAvgProduct.setFrameShape(QFrame.StyledPanel)
        self.showAvgProduct.setFrameShadow(QFrame.Raised)

        self.gridLayout_14.addWidget(self.showAvgProduct, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_14, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget_11, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget_9, 1, 0, 1, 1)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_17 = QGridLayout(self.widget_17)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_16 = QGridLayout(self.widget_18)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 13pt \"Josefin Sans SemiBold\";")

        self.gridLayout_16.addWidget(self.label_11, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_18, 0, 0, 1, 1)

        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_15 = QGridLayout(self.widget_19)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.categoryBar = QFrame(self.widget_19)
        self.categoryBar.setObjectName(u"categoryBar")
        self.categoryBar.setMaximumSize(QSize(600, 600))
        self.categoryBar.setStyleSheet(u"item-align: center;")
        self.categoryBar.setFrameShape(QFrame.StyledPanel)
        self.categoryBar.setFrameShadow(QFrame.Raised)

        self.gridLayout_15.addWidget(self.categoryBar, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_19, 1, 0, 1, 1)


        self.gridLayout_20.addWidget(self.widget_17, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_21.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.dashboard)
        self.maintenance = QWidget()
        self.maintenance.setObjectName(u"maintenance")
        self.gridLayout_22 = QGridLayout(self.maintenance)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.maintenance)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 984, 682))
        self.gridLayout_24 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.scrollAreaWidgetContents)
        self.widget_21.setObjectName(u"widget_21")
        self.gridLayout_29 = QGridLayout(self.widget_21)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_25 = QGridLayout(self.widget_22)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_22)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 16pt \"Josefin Sans SemiBold\";")

        self.gridLayout_25.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_22, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_28 = QGridLayout(self.widget_23)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.widget_24 = QWidget(self.widget_23)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 35))
        self.gridLayout_26 = QGridLayout(self.widget_24)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_17 = QLabel(self.widget_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 13pt \"Josefin Sans SemiBold\";")

        self.gridLayout_26.addWidget(self.label_17, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_24, 0, 0, 1, 1)

        self.widget_25 = QWidget(self.widget_23)
        self.widget_25.setObjectName(u"widget_25")
        self.gridLayout_27 = QGridLayout(self.widget_25)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_18 = QLabel(self.widget_25)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_27.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.widget_25, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_23, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_21, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_22.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.maintenance)
        self.administration = QWidget()
        self.administration.setObjectName(u"administration")
        self.gridLayout_30 = QGridLayout(self.administration)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.scrollArea_3 = QScrollArea(self.administration)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 966, 664))
        self.gridLayout_32 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_32.setSpacing(0)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_31 = QGridLayout(self.widget_26)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_26)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 16pt \"Josefin Sans SemiBold\";")

        self.gridLayout_31.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.widget_26, 0, 0, 1, 1)

        self.widget_27 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_27.setObjectName(u"widget_27")

        self.gridLayout_32.addWidget(self.widget_27, 1, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_30.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.administration)

        self.gridLayout_23.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.iconOnly = QWidget(self.centralwidget)
        self.iconOnly.setObjectName(u"iconOnly")
        self.gridLayout = QGridLayout(self.iconOnly)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.iconOnly)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 20)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        self.dashBtn_1 = QPushButton(self.iconOnly)
        self.dashBtn_1.setObjectName(u"dashBtn_1")
        self.dashBtn_1.setStyleSheet(u"background-color: transparent;\n"
"")
        self.dashBtn_1.setIcon(icon3)
        self.dashBtn_1.setCheckable(True)
        self.dashBtn_1.setAutoExclusive(True)
        self.dashBtn_1.setFlat(True)

        self.gridLayout.addWidget(self.dashBtn_1, 1, 0, 1, 1)

        self.mtnBtn_1 = QPushButton(self.iconOnly)
        self.mtnBtn_1.setObjectName(u"mtnBtn_1")
        self.mtnBtn_1.setStyleSheet(u"background-color: transparent;\n"
"")
        self.mtnBtn_1.setIcon(icon2)
        self.mtnBtn_1.setCheckable(True)
        self.mtnBtn_1.setAutoExclusive(True)
        self.mtnBtn_1.setFlat(True)

        self.gridLayout.addWidget(self.mtnBtn_1, 2, 0, 1, 1)

        self.admiBtn_1 = QPushButton(self.iconOnly)
        self.admiBtn_1.setObjectName(u"admiBtn_1")
        self.admiBtn_1.setStyleSheet(u"background-color: transparent;\n"
"")
        self.admiBtn_1.setIcon(icon)
        self.admiBtn_1.setCheckable(True)
        self.admiBtn_1.setAutoExclusive(True)
        self.admiBtn_1.setFlat(True)

        self.gridLayout.addWidget(self.admiBtn_1, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 365, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.logoutBtn_1 = QPushButton(self.iconOnly)
        self.logoutBtn_1.setObjectName(u"logoutBtn_1")
        self.logoutBtn_1.setStyleSheet(u"font: 500 8pt \"Josefin Sans Medium\";\n"
"color: rgb(0,0,0);\n"
"text-align: center;\n"
"background-color: transparent;")
        self.logoutBtn_1.setIcon(icon1)
        self.logoutBtn_1.setFlat(True)

        self.gridLayout.addWidget(self.logoutBtn_1, 5, 0, 1, 1)


        self.gridLayout_23.addWidget(self.iconOnly, 0, 0, 2, 1)

        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        self.toggleBtn.toggled.connect(self.iconOnly.setVisible)
        self.toggleBtn.toggled.connect(self.fullWid.setHidden)
        self.dashBtn_1.toggled.connect(self.dashBtn_2.setChecked)
        self.mtnBtn_1.toggled.connect(self.mtnBtn_2.setChecked)
        self.admiBtn_1.toggled.connect(self.admiBtn_2.setChecked)
        self.dashBtn_2.toggled.connect(self.dashBtn_1.setChecked)
        self.mtnBtn_2.toggled.connect(self.mtnBtn_1.setChecked)
        self.admiBtn_2.toggled.connect(self.admiBtn_1.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.admiBtn_2.setText(QCoreApplication.translate("AdminWindow", u"Administration", None))
        self.logoutBtn_2.setText(QCoreApplication.translate("AdminWindow", u"Logout", None))
        self.mtnBtn_2.setText(QCoreApplication.translate("AdminWindow", u"Maintenance", None))
        self.dashBtn_2.setText(QCoreApplication.translate("AdminWindow", u"Dashboard", None))
        self.toggleBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"Logo", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"Admin", None))
        self.label_15.setText(QCoreApplication.translate("AdminWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("AdminWindow", u"Total Account:", None))
        self.showTotalAcc.setText(QCoreApplication.translate("AdminWindow", u"Amount Placeholder", None))
        self.label_8.setText(QCoreApplication.translate("AdminWindow", u"Account with product posted", None))
        self.label_10.setText(QCoreApplication.translate("AdminWindow", u"Average item selling per account", None))
        self.label_11.setText(QCoreApplication.translate("AdminWindow", u"Category", None))
        self.label_16.setText(QCoreApplication.translate("AdminWindow", u"Maintenance", None))
        self.label_17.setText(QCoreApplication.translate("AdminWindow", u"Banner", None))
        self.label_18.setText(QCoreApplication.translate("AdminWindow", u"Show banner", None))
        self.label_19.setText(QCoreApplication.translate("AdminWindow", u"Administration", None))
        self.label.setText("")
        self.dashBtn_1.setText("")
        self.mtnBtn_1.setText("")
        self.admiBtn_1.setText("")
        self.logoutBtn_1.setText("")
    # retranslateUi

