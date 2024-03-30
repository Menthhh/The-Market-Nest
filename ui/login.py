# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(892, 655)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.gridLayout_16 = QGridLayout(self.loginPage)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Container = QWidget(self.loginPage)
        self.Container.setObjectName(u"Container")
        self.gridLayout_2 = QGridLayout(self.Container)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Container)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 230, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.widget_26 = QWidget(self.widget)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 50))
        self.gridLayout_33 = QGridLayout(self.widget_26)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_26)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.gridLayout_5 = QGridLayout(self.widget_5)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Josefin Sans SemiBold"])
        font.setPointSize(18)
        font.setWeight(QFont.DemiBold)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 18pt \"Josefin Sans SemiBold\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_5, 1, 0, 1, 1)


        self.gridLayout_33.addWidget(self.widget_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_26, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.Container)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(75, 85, 189);")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.gridLayout_14 = QGridLayout(self.widget_3)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(8, 8, 8, 8)
        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_13 = QGridLayout(self.widget_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_12)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(200, 25))
        font1 = QFont()
        font1.setFamilies([u"Josefin Sans Medium"])
        font1.setPointSize(9)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        font1.setKerning(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")
        self.pushButton.setFlat(False)

        self.gridLayout_13.addWidget(self.pushButton, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)


        self.gridLayout_14.addWidget(self.widget_12, 3, 0, 1, 1)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 10, 0, 10)
        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_15 = QGridLayout(self.widget_13)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Josefin Sans Medium"])
        font2.setPointSize(11)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Josefin Sans Medium"])
        font3.setPointSize(19)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.verticalSpacer_4, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_13, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_11 = QGridLayout(self.widget_10)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_10)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_10 = QGridLayout(self.widget_7)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_8 = QGridLayout(self.widget_8)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setFrame(False)

        self.gridLayout_8.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_8, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_9 = QGridLayout(self.widget_9)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.widget_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 25))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setFrame(False)

        self.gridLayout_9.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_9, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(16777215, 30))
        self.gridLayout_12 = QGridLayout(self.widget_11)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.signupLabel = QLabel(self.widget_11)
        self.signupLabel.setObjectName(u"signupLabel")
        self.signupLabel.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Josefin Sans Medium"])
        font4.setPointSize(10)
        self.signupLabel.setFont(font4)
        self.signupLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.signupLabel, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_11, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_10, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)


        self.gridLayout_16.addWidget(self.Container, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.loginPage)
        self.signupPage = QWidget()
        self.signupPage.setObjectName(u"signupPage")
        self.gridLayout_17 = QGridLayout(self.signupPage)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.signupPage)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_18 = QGridLayout(self.widget_14)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.widget_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_22 = QGridLayout(self.widget_15)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(-1, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        self.gridLayout_21 = QGridLayout(self.widget_19)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setHorizontalSpacing(0)
        self.gridLayout_21.setVerticalSpacing(10)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_19)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_19 = QGridLayout(self.widget_17)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icon/icon/logo.ico"))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_17, 0, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_19)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 30))
        self.gridLayout_20 = QGridLayout(self.widget_18)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(81, 82, 108);\n"
"font: 600 18pt \"Josefin Sans SemiBold\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.label_9, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.widget_18, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.widget_19, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_5, 0, 0, 1, 1)


        self.gridLayout_18.addWidget(self.widget_15, 0, 0, 1, 1)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy1.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy1)
        self.widget_16.setStyleSheet(u"background-color: rgb(75, 85, 189);")
        self.gridLayout_34 = QGridLayout(self.widget_16)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_23 = QGridLayout(self.widget_20)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, -1, 0)
        self.label_10 = QLabel(self.widget_20)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 500 19pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_10, 0, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_20, 0, 0, 1, 1)

        self.widget_21 = QWidget(self.widget_16)
        self.widget_21.setObjectName(u"widget_21")
        self.gridLayout_29 = QGridLayout(self.widget_21)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.gridLayout_24 = QGridLayout(self.widget_22)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_11 = QLabel(self.widget_22)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_24.addWidget(self.label_11, 0, 0, 1, 1)

        self.usernameInput = QLineEdit(self.widget_22)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.usernameInput.setFrame(False)

        self.gridLayout_24.addWidget(self.usernameInput, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_22, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_25 = QGridLayout(self.widget_23)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.emailInput = QLineEdit(self.widget_23)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.emailInput.setFrame(False)

        self.gridLayout_25.addWidget(self.emailInput, 1, 0, 1, 1)

        self.label_12 = QLabel(self.widget_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_25.addWidget(self.label_12, 0, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_23, 1, 0, 1, 1)

        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName(u"widget_24")
        self.gridLayout_26 = QGridLayout(self.widget_24)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_13 = QLabel(self.widget_24)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_26.addWidget(self.label_13, 0, 0, 1, 1)

        self.phoneInput = QLineEdit(self.widget_24)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.phoneInput.setFrame(False)

        self.gridLayout_26.addWidget(self.phoneInput, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_24, 2, 0, 1, 1)

        self.widget_25 = QWidget(self.widget_21)
        self.widget_25.setObjectName(u"widget_25")
        self.gridLayout_27 = QGridLayout(self.widget_25)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_14 = QLabel(self.widget_25)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_27.addWidget(self.label_14, 0, 0, 1, 1)

        self.passInput = QLineEdit(self.widget_25)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.passInput.setFrame(False)

        self.gridLayout_27.addWidget(self.passInput, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_25, 3, 0, 1, 1)

        self.widget_27 = QWidget(self.widget_21)
        self.widget_27.setObjectName(u"widget_27")
        self.gridLayout_28 = QGridLayout(self.widget_27)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_15 = QLabel(self.widget_27)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 500 11pt \"Josefin Sans Medium\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_28.addWidget(self.label_15, 0, 0, 1, 1)

        self.confirmPassInput = QLineEdit(self.widget_27)
        self.confirmPassInput.setObjectName(u"confirmPassInput")
        self.confirmPassInput.setStyleSheet(u"background-color: rgb(63, 70, 170);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.confirmPassInput.setFrame(False)

        self.gridLayout_28.addWidget(self.confirmPassInput, 1, 0, 1, 1)


        self.gridLayout_29.addWidget(self.widget_27, 4, 0, 1, 1)


        self.gridLayout_34.addWidget(self.widget_21, 1, 0, 1, 1)

        self.widget_28 = QWidget(self.widget_16)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setEnabled(True)
        self.gridLayout_32 = QGridLayout(self.widget_28)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(200)
        self.gridLayout_32.setVerticalSpacing(0)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.gridLayout_30 = QGridLayout(self.widget_29)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.cancelBtn = QPushButton(self.widget_29)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(0, 25))
        self.cancelBtn.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_30.addWidget(self.cancelBtn, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.widget_29, 0, 0, 1, 1)

        self.widget_30 = QWidget(self.widget_28)
        self.widget_30.setObjectName(u"widget_30")
        self.gridLayout_31 = QGridLayout(self.widget_30)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.signupConfirmBtn = QPushButton(self.widget_30)
        self.signupConfirmBtn.setObjectName(u"signupConfirmBtn")
        self.signupConfirmBtn.setMinimumSize(QSize(0, 25))
        self.signupConfirmBtn.setStyleSheet(u"background-color: rgb(249, 97, 125);\n"
"font: 500 9pt \"Josefin Sans Medium\";\n"
"color: white;\n"
"border-radius: 5px;")

        self.gridLayout_31.addWidget(self.signupConfirmBtn, 0, 1, 1, 1)


        self.gridLayout_32.addWidget(self.widget_30, 0, 1, 1, 1)


        self.gridLayout_34.addWidget(self.widget_28, 2, 0, 1, 1)


        self.gridLayout_18.addWidget(self.widget_16, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.widget_14, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.signupPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"MarketNest", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Sign in to your Account", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Welcome Back", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.signupLabel.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("Dialog", u"MarketNest", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Registration", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.signupConfirmBtn.setText(QCoreApplication.translate("Dialog", u"Signup", None))
    # retranslateUi

