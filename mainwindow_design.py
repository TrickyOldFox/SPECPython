# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1343, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView = PlotWidget(self.page)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 181))
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_6.addWidget(self.graphicsView)
        self.graphicsView_2 = PlotWidget(self.page)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(0, 181))
        self.graphicsView_2.setMaximumSize(QtCore.QSize(16777215, 311))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_6.addWidget(self.graphicsView_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView_3 = PlotWidget(self.page_2)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_5.addWidget(self.graphicsView_3)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(191, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(251, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 171, 20))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 2, 181, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(2, 215, 181, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(0, 0, 241, 601))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_8.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_3.setLineWidth(1)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 1, 241, 271))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.layoutWidget2)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(1)
        self.tableWidget_4.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        self.verticalLayout_7.addWidget(self.tableWidget_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_10.addWidget(self.pushButton_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_12.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_12.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_12.addWidget(self.pushButton_15)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1343, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuChart_1_View = QtWidgets.QMenu(self.menubar)
        self.menuChart_1_View.setObjectName("menuChart_1_View")
        self.menuChart_2_View = QtWidgets.QMenu(self.menubar)
        self.menuChart_2_View.setObjectName("menuChart_2_View")
        self.menuChart_2_View_2 = QtWidgets.QMenu(self.menubar)
        self.menuChart_2_View_2.setObjectName("menuChart_2_View_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionStart_ADC = QtWidgets.QAction(MainWindow)
        self.actionStart_ADC.setObjectName("actionStart_ADC")
        self.actionStop_ADC = QtWidgets.QAction(MainWindow)
        self.actionStop_ADC.setObjectName("actionStop_ADC")
        self.actionCurrent = QtWidgets.QAction(MainWindow)
        self.actionCurrent.setCheckable(False)
        self.actionCurrent.setEnabled(True)
        self.actionCurrent.setObjectName("actionCurrent")
        self.actionSignal = QtWidgets.QAction(MainWindow)
        self.actionSignal.setCheckable(False)
        self.actionSignal.setEnabled(True)
        self.actionSignal.setObjectName("actionSignal")
        self.actionMX = QtWidgets.QAction(MainWindow)
        self.actionMX.setCheckable(False)
        self.actionMX.setEnabled(True)
        self.actionMX.setObjectName("actionMX")
        self.actionCurrent_2 = QtWidgets.QAction(MainWindow)
        self.actionCurrent_2.setCheckable(False)
        self.actionCurrent_2.setEnabled(True)
        self.actionCurrent_2.setObjectName("actionCurrent_2")
        self.actionSignal_2 = QtWidgets.QAction(MainWindow)
        self.actionSignal_2.setCheckable(False)
        self.actionSignal_2.setEnabled(True)
        self.actionSignal_2.setObjectName("actionSignal_2")
        self.actionMX_2 = QtWidgets.QAction(MainWindow)
        self.actionMX_2.setCheckable(False)
        self.actionMX_2.setEnabled(True)
        self.actionMX_2.setObjectName("actionMX_2")
        self.actionCompete = QtWidgets.QAction(MainWindow)
        self.actionCompete.setObjectName("actionCompete")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionCompete)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuChart_1_View.addAction(self.actionStart_ADC)
        self.menuChart_1_View.addAction(self.actionStop_ADC)
        self.menuChart_2_View.addAction(self.actionCurrent)
        self.menuChart_2_View.addAction(self.actionSignal)
        self.menuChart_2_View.addAction(self.actionMX)
        self.menuChart_2_View_2.addAction(self.actionCurrent_2)
        self.menuChart_2_View_2.addAction(self.actionSignal_2)
        self.menuChart_2_View_2.addAction(self.actionMX_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChart_1_View.menuAction())
        self.menubar.addAction(self.menuChart_2_View.menuAction())
        self.menubar.addAction(self.menuChart_2_View_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton_8.setText(_translate("MainWindow", "Search Lines"))
        self.pushButton_10.setText(_translate("MainWindow", "Clear"))
        self.pushButton_5.setText(_translate("MainWindow", "Delete Lines"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Coords"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lines"))
        self.pushButton_4.setText(_translate("MainWindow", "Interpolate"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "AVG"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Precision"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "LinesSearchRange"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "LinesDeleteRange"))
        item = self.tableWidget_4.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "FonSearchRange"))
        item = self.tableWidget_4.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "PointImapct"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Values"))
        self.pushButton_9.setText(_translate("MainWindow", "Restore parametres"))
        self.pushButton_12.setText(_translate("MainWindow", "Update parametres"))
        self.pushButton_13.setText(_translate("MainWindow", "Delete"))
        self.pushButton_14.setText(_translate("MainWindow", "Search"))
        self.pushButton_15.setText(_translate("MainWindow", "Interpolate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuChart_1_View.setTitle(_translate("MainWindow", "ADC"))
        self.menuChart_2_View.setTitle(_translate("MainWindow", "Chart 1 View"))
        self.menuChart_2_View_2.setTitle(_translate("MainWindow", "Chart 2 View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionStart_ADC.setText(_translate("MainWindow", "Start ADC"))
        self.actionStop_ADC.setText(_translate("MainWindow", "Stop ADC"))
        self.actionCurrent.setText(_translate("MainWindow", "Current"))
        self.actionSignal.setText(_translate("MainWindow", "Signal"))
        self.actionMX.setText(_translate("MainWindow", "MX"))
        self.actionMX.setToolTip(_translate("MainWindow", "MX"))
        self.actionCurrent_2.setText(_translate("MainWindow", "Current"))
        self.actionSignal_2.setText(_translate("MainWindow", "Signal"))
        self.actionMX_2.setText(_translate("MainWindow", "MX"))
        self.actionMX_2.setToolTip(_translate("MainWindow", "MX"))
        self.actionCompete.setText(_translate("MainWindow", "Compete"))

from pyqtgraph import PlotWidget
