# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notepad.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 568)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(6, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.languageComboBox = QComboBox(self.widget_4)
        self.languageComboBox.setObjectName(u"languageComboBox")

        self.verticalLayout_6.addWidget(self.languageComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.genderComboBox = QComboBox(self.widget_4)
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.verticalLayout_4.addWidget(self.genderComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.enginesComboBox = QComboBox(self.widget_4)
        self.enginesComboBox.setObjectName(u"enginesComboBox")

        self.verticalLayout_7.addWidget(self.enginesComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)

        self.voicesComboBox = QComboBox(self.widget_4)
        self.voicesComboBox.setObjectName(u"voicesComboBox")

        self.verticalLayout_8.addWidget(self.voicesComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.resultTableWidget = QTableWidget(self.widget_5)
        if (self.resultTableWidget.columnCount() < 5):
            self.resultTableWidget.setColumnCount(5)
        self.resultTableWidget.setObjectName(u"resultTableWidget")
        self.resultTableWidget.setMinimumSize(QSize(150, 0))
        self.resultTableWidget.setMaximumSize(QSize(550, 16777215))
        self.resultTableWidget.setFrameShape(QFrame.StyledPanel)
        self.resultTableWidget.setLineWidth(1)
        self.resultTableWidget.setMidLineWidth(0)
        self.resultTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultTableWidget.setDragEnabled(True)
        self.resultTableWidget.setAlternatingRowColors(True)
        self.resultTableWidget.setSortingEnabled(True)
        self.resultTableWidget.setRowCount(0)
        self.resultTableWidget.setColumnCount(5)
        self.resultTableWidget.horizontalHeader().setStretchLastSection(True)
        self.resultTableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_5.addWidget(self.resultTableWidget)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(70, 0))
        self.widget_3.setMaximumSize(QSize(70, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.voicePushButton = QPushButton(self.widget_3)
        self.voicePushButton.setObjectName(u"voicePushButton")

        self.verticalLayout_3.addWidget(self.voicePushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.debugPushButton = QPushButton(self.widget_3)
        self.debugPushButton.setObjectName(u"debugPushButton")

        self.verticalLayout_3.addWidget(self.debugPushButton)


        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sprache", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Geschlecht", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Modus", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stimme", None))
        self.voicePushButton.setText(QCoreApplication.translate("MainWindow", u"Voice", None))
        self.debugPushButton.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
    # retranslateUi

