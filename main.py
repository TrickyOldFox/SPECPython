# This Python file uses the following encoding: utf-8
'''
ToDoList :
    Определить скорость обновления данных и количество данных подгружаемых в график
    Разобраться с автоскэйлом, привязать не к центру а к максимальному значению по оси
    Написать ЭЙДиСи модуль
    Добавить лэйблы или список для отображения других каналов сбоку
'''

from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import plot
import pyqtgraph as pg
import mainwindow_design
import os
import sys
from random import randint
import numpy as np
import AnalizeTool
import subprocess

def copy(s):
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        subprocess.Popen(['clip'], stdin=subprocess.PIPE, encoding='utf8').communicate(s)
    else:
        raise Exception('Platform not supported')

global Channels

Channels = []

def update_channels():
    Channel_Names = ['Current', 'Signal', 'MX']
    Channels = []
    for i in Channel_Names: Channel.create_channel(i)



class Channel():  
        Chart1=False
        Chart2=False
        Data=[0,]
        Name=' '
    
        def trigerred_action_chart1(self):
            if not self.Chart1:
                for i in Channels:
                    if i!=self: i.Chart1=False 
                self.Chart1=True
            
        def trigerred_action_chart2(self):
            if not self.Chart2:
                self.Chart2=False
                for i in Channels:
                    if i!=self: i.Chart2=False 
                self.Chart2=True
                
        def create_channel(name):
            a = Channel()
            Channels.append(a);
            a.Name = name
                 
                    
class mainwindow(QtWidgets.QMainWindow, mainwindow_design.Ui_MainWindow):
    
    delay=15
    Pen=(255,0,0)
    update_channels()
    
    #File Channels and variables
    fname=" "
    fname2=" "
    FileChannel =[]
    FileChannel2 = []
    FileChannelInterpolated = []
    FileData = []
    FileData2 = []
    InterpolationPoints = []
    InterpolationList = []
    InterpolationListFiltered = []
    LinesToSearch = []
    LinesToDelete = []
    PossibleLines = []
    AverageFon = []
    AverageDeriviative = []
    AverageFluctuation = 0
    AVG = 20
    Precision = 5e-3
    Filter = 1 + 1e-2
    FilterRangeMultiplier = 5
    LinesSearchRange = 2
    LinesDeleteRange = 6
    FonSearchRange = 1000
    PointImpact = 1
    state = 0
    ParametresOfSearchEngine = [AVG,Precision,LinesSearchRange,LinesDeleteRange,Filter,PointImpact]
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        
        #Tables
        self.pushButton_3.clicked.connect(self.ClearTable_3)
        self.pushButton_4.clicked.connect(self.Interpolation)
        
        self.pushButton_6.clicked.connect(self.ClearTable_2)
        self.pushButton_10.clicked.connect(self.ClearTable)
    
        self.pushButton_8.clicked.connect(self.SearchLinesInSpectreInit)
        self.pushButton_5.clicked.connect(self.DeleteLinesFromSpectreInit)
        self.pushButton_9.clicked.connect(self.RestoreParametresOfSearchEngine)
        self.pushButton_12.clicked.connect(self.UpdateParametresOfSearchEngine)
        
        self.pushButton_15.clicked.connect(self.ChangeToInterpolate)
        self.pushButton_14.clicked.connect(self.ChangeToSearch)
        self.pushButton_13.clicked.connect(self.ChangeToDelete)
        
        #ADC 
        self.ADC_on = False
        self.actionStart_ADC.triggered.connect(self.ADC_init)
        self.actionStop_ADC.triggered.connect(self.ADC_stop)
        self.RestoreParametresOfSearchEngine()
        
        self.data_line = self.graphicsView.plot([0,],[0,],pen=self.Pen)
        self.graphicsView.showGrid(x=True,y=True)
        self.data_line_2 = self.graphicsView_2.plot([0,],[0,],pen=self.Pen)
        self.graphicsView_2.showGrid(x=True,y=True)
        self.data_line_3 = self.graphicsView_3.plot([0,],[0,],pen=self.Pen)
        self.graphicsView_3.showGrid(x=True,y=True)
        self.data_line_5 = self.graphicsView_3.plot([0,],[0,],pen=(0,0,255)) 
        
        self.actionOpen.triggered.connect(self.Open_action)
        self.actionSave_as.triggered.connect(self.Save_as_action)
        self.actionCompete.triggered.connect(self.Compete_action)
        # 1-st Chart
        self.graphicsView.setBackground('w')
        
        # 2-nd Chart
        self.graphicsView_2.setBackground('w')
        self.channel_switcher()
        
        self.graphicsView_3.setBackground('w')
        self.p = self.graphicsView_3.getPlotItem()
        self.graphicsView_3.scene().sigMouseClicked.connect(self.GetInterpolationPoint)
        # Timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.delay)
        self.timer.timeout.connect(self.update_data)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        
    def ChangeToSearch(self):
        self.state = 2
        
    def ChangeToDelete(self):
        self.state = 1
        
    def ChangeToInterpolate(self):    
        self.state = 0
        
    def UpdateParametresOfSearchEngine(self):
        try:
            self.AVG = (int(self.tableWidget_4.item(0,0).text()))
        except:
            print("Wrong type of input")
        try:
            self.Precision = (float(self.tableWidget_4.item(1,0).text()))
        except:
            print("Wrong type of input")
        try:
            self.LinesSearchRange = (int(self.tableWidget_4.item(2,0).text()))
        except:
            print("Wrong type of input")
        try:
            self.LinesDeleteRange = (int(self.tableWidget_4.item(3,0).text()))
        except:
            print("Wrong type of input")
        try:
            self.Filter = (float(self.tableWidget_4.item(4,0).text()))
        except:
            print("Wrong type of inputh")
        try:
            self.PointImpact = (int(self.tableWidget_4.item(5,0).text()))
        except:
            print("Wrong type of input")
        
    def RestoreParametresOfSearchEngine(self):
        self.ParametresOfSearchEngine[0] = self.AVG
        self.ParametresOfSearchEngine[1] = self.Precision
        self.ParametresOfSearchEngine[2] = self.LinesSearchRange
        self.ParametresOfSearchEngine[3] = self.LinesDeleteRange
        self.ParametresOfSearchEngine[4] = self.Filter
        self.ParametresOfSearchEngine[5] = self.PointImpact
        for i in range(len(self.ParametresOfSearchEngine)):
            item = QtGui.QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, self.ParametresOfSearchEngine[i])
            self.tableWidget_4.setItem(i,0,item)
        
    def DeleteLinesFromSpectreInit(self):
        self.LinesToDelete = []
        if self.FileChannel == []:
            print("There is no data file openned")
        else:
            Text = self.plainTextEdit_2.toPlainText()
            Text = Text.splitlines()
            print(Text)
            for i in range(len(Text)):
                try:
                    self.LinesToDelete.append(float(Text[i]))
                except:
                    print("Wrong type of input in Lines to Search")
            if self.LinesToDelete == []: print("Lines to Delete list is empty") 
            else:
                self.LinesToDelete = sorted(self.LinesToDelete)
                if self.LinesToDelete[0] < self.FileChannel[0][0] or self.LinesToDelete[-1] > self.FileChannel[0][-1]:
                    print("Lines to Delete are out of bounds")
                else:
                    self.LinesToSearch = self.LinesToDelete
                    self.AverageDeriviative, self.AverageFon, self.AverageFluctuation, self.FileChannel, self.PossibleLines = \
                                AnalizeTool.SearchLinesInSpectre(self.FileChannel, self.AVG, self.Precision, self.FilterRangeMultiplier, self.Filter, self.LinesSearchRange, self.LinesToSearch)
                    if len(self.PossibleLines)!=0:
                        self.FilChannel = AnalizeTool.DeleteLinesFromSpectre(self.PossibleLines, self.FileChannel, self.LinesDeleteRange, self.PointImpact, self.AverageFluctuation)
                        self.data_line_3.setData(self.FileChannel[0],self.FileChannel[1])
                        self.Plot_from_file2()
                    
    def PlotLinesToSearch(self):
        for i in self.PossibleLines:
            a=i[1]
            b=i[2]
            PlotX=[]
            PlotY=[]
            while a>b:
                PlotX.append(i[0])
                PlotY.append(b)
                b+=0.0001
                self.data_line_4 = self.graphicsView_3.plot(PlotX,PlotY,pen=(0,255,0))
        print("Lines to Search plotting is complete")
        
    def SearchLinesInSpectreInit(self):
        self.LinesToSearch = []
        if self.FileChannel == []:
            print("There is no data file openned")
        else:
            Text = self.plainTextEdit.toPlainText()
            Text = Text.splitlines()
            print(Text)
            for i in range(len(Text)):
                try:
                    self.LinesToSearch.append(float(Text[i]))
                except:
                    print("Wrong type of input in Lines to Search")
            print(self.LinesToSearch)
            self.LinesToSearch = sorted(self.LinesToSearch)
            while (self.LinesToSearch[0] < self.FileChannel[0][0]):
                self.LinesToSearch = self.LinesToSearch[1:len(self.LinesToSearch)]
            while (self.LinesToSearch[-1] > self.FileChannel[0][-1]):
                self.LinesToSearch = self.LinesToSearch[0:len(self.LinesToSearch)-1]
            if self.LinesToSearch == []: print("Lines to Search list is empty")
            else:             
                self.AverageDeriviative, self.AverageFon, self.AverageFluctuation, self.FileChannel, self.PossibleLines = \
                    AnalizeTool.SearchLinesInSpectre(self.FileChannel, self.AVG, self.Precision, self.FilterRangeMultiplier, self.Filter, self.LinesSearchRange, self.LinesToSearch)
                    #self.PlotLinesToSearch()
                DataToClipBoard = ""
                for i in self.PossibleLines:
                    DataToClipBoard += "%.1f" % i[0]
                    DataToClipBoard += "\t"   
                    DataToClipBoard += "%.4f" % (i[1]-i[2])
                    DataToClipBoard += "\n"
                print(DataToClipBoard)
                copy(DataToClipBoard)
        
    def Interpolation(self):
        if self.FileChannel == []:
            print("There is no data file openned")
        else: 
            self.InterpolationList = []
            self.InterpolationListFiltered = []
            for i in range(self.tableWidget_3.rowCount()):
                if self.tableWidget_3.item(i,0) != None and self.tableWidget_3.item(i,1) != None:    
                    self.InterpolationList.append((self.tableWidget_3.item(i,0).text(),self.tableWidget_3.item(i,1).text()))
                
            for i in range(len(self.InterpolationList)):
                try:
                    self.InterpolationListFiltered.append((float(self.InterpolationList[i][0]),float(self.InterpolationList[i][1])))
                except:
                    print("A wrong type of data in Lines field")        
            if len(self.InterpolationListFiltered) < 2:
                print("Not enough points to Scan and Fit")
            else:
                self.getInterpolatedPoints()
                self.ClearTable_3()
                for element in self.InterpolationListFiltered:
                    print(element)
                    rows = self.tableWidget_3.rowCount()
                    self.tableWidget_3.setRowCount(rows+1)
                    item = QtGui.QTableWidgetItem()
                    item.setData(QtCore.Qt.EditRole, element[1])
                    self.tableWidget_3.setItem(rows,0,item)
                print("Points were read just fine")

    def getInterpolatedPoints(self):
        self.InterpolationListFiltered = sorted(self.InterpolationListFiltered)
        print(self.InterpolationListFiltered)
        b = self.FileChannel[0][0]
        k = 0           
        for i in range(len(self.InterpolationListFiltered)-1):
            a = self.InterpolationListFiltered[i+1][0] - self.InterpolationListFiltered[i][0]
            c = self.InterpolationListFiltered[i+1][1] - self.InterpolationListFiltered[i][1]
            while b < self.InterpolationListFiltered[i+1][0]:
                b = self.FileChannel[0][k]
                self.FileChannel[0][k] = self.InterpolationListFiltered[i][1] + (c/a)*(self.FileChannel[0][k]-self.InterpolationListFiltered[i][0])
                k+=1
        for i in range(len(self.FileChannel[0])-k):
            self.FileChannel[0][k+i] = self.InterpolationListFiltered[-1][1] + (c/a)*(self.FileChannel[0][k+i]-self.InterpolationListFiltered[-1][0])
        self.Plot_from_file()
        self.Plot_from_file2()
        for i in range(self.tableWidget.rowCount()):
            item = QtGui.QTableWidgetItem()
            item.setData(QtCore.Qt.EditRole, self.InterpolationListFiltered[i][1])
            self.tableWidget_3.setItem(i,0,item)
        print("Scan and Fit process complete")
            
    def ClearTable_3(self):
        self.tableWidget_3.setRowCount(0) 
        self.InterpolationPoints = []
    def ClearTable_2(self):
        self.plainTextEdit_2.clear()
        self.LinesToDelete = []
    def ClearTable(self):
        self.plainTextEdit.clear()
        self.LinesToSearch = []
        
    def GetInterpolationPoint(self, event):
        #Interpolate
        if self.state == 0:
            if event.buttons() == QtCore.Qt.MidButton:
                Point = self.p.vb.mapSceneToView(event.scenePos())
                self.InterpolationPoints.append((Point.x(),Point.y()))
                rows = self.tableWidget_3.rowCount()
                self.tableWidget_3.setRowCount(rows+1)
                element = self.InterpolationPoints[-1]
                item = QtGui.QTableWidgetItem()
                item.setData(QtCore.Qt.EditRole, element[0])
                self.tableWidget_3.setItem(rows,0,item)
                print("The point has been captured")
        #Delete
        if self.state == 1:
            if event.buttons() == QtCore.Qt.MidButton:
                Point = self.p.vb.mapSceneToView(event.scenePos())
                self.plainTextEdit_2.appendPlainText("%.1f" % Point.x()) 
                print("The point has been captured")
        #Search
        if self.state == 2:
            if event.buttons() == QtCore.Qt.MidButton:
                Point = self.p.vb.mapSceneToView(event.scenePos())
                self.plainTextEdit.appendPlainText("%.1f" % Point.x()) 
                print("The point has been captured")
    
    def Open_action(self):
        self.ADC_stop
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "*.csv" )
        if len(self.fname[0])!=0:
            self.stackedWidget.setCurrentIndex(1)
            self.FileData, self.FileChannel = AnalizeTool.csv_open(self.fname[0])
            #print(self.FileChannel)
        if self.FileData == 0:
            print("Error acured during read from file")
            self.fname = " "
        self.Plot_from_file()
        
    def Save_as_action(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, "Save", "", "csv Files (*.csv)")
        if len(self.fname[0])!=0:
            AnalizeTool.csv_save(fileName[0], self.FileChannel)
            print(fileName);
    
    def Compete_action(self):
        if self.fname2 == " ":
            self.fname2 = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', "*.csv" )
            if len(self.fname[0])!=0:
                self.stackedWidget.setCurrentIndex(1)
                self.FileData2, self.FileChannel2 = AnalizeTool.csv_open(self.fname2[0])
                #print(self.FileChannel)
            if self.FileData2 == 0: 
                print("Error acured during read from file")
                self.fname2 = " "
            else: 
                self.Plot_from_file2()
        else:
            self.fname2 = " "
            self.Plot_from_file()
    
    def Plot_from_file2(self):
        if self.fname2 != " ":
            self.data_line_4 = self.graphicsView_3.plot(self.FileChannel2[0],self.FileChannel2[1], pen=(0,0,255))
   
    def Plot_from_file(self):
        self.graphicsView_3.clear()
        if self.fname != " ":
            self.data_line_3 = self.graphicsView_3.plot(self.FileChannel[0],self.FileChannel[1],pen=self.Pen)
        
    #ADC Moadule
    def ADC_init(self):
        self.ADC_on = True
        self.stackedWidget.setCurrentIndex(0)
        # Data Threads
        self.t = np.array([0,])
        for i in Channels: i.Data = np.array([0,])
        print("ADC initialising")
        
    def ADC_stop(self):
        self.ADC_on = False
        
    #Checkbox Evaluation Module
    def channel_switcher(self):
        self.actionCurrent.triggered.connect(Channels[0].trigerred_action_chart1)
        self.actionCurrent_2.triggered.connect(Channels[0].trigerred_action_chart2)
        self.actionSignal.triggered.connect(Channels[1].trigerred_action_chart1)
        self.actionSignal_2.triggered.connect(Channels[1].trigerred_action_chart2)
        self.actionMX.triggered.connect(Channels[2].trigerred_action_chart1)
        self.actionMX_2.triggered.connect(Channels[2].trigerred_action_chart2)
            
    #Data Update Module     
    def update_data(self):
        if self.ADC_on:
            self.t = np.append(self.t, self.t[-1]+self.delay/1000)  # Add a new time value
            for i in Channels:
                i.Data = np.append(i.Data, randint(0,100))# Add a new random value        
    def update_plot(self):
        if self.ADC_on:
            for i in Channels:
                if i.Chart1:
                    self.data_line.setData(self.t, i.Data)# Update the data.
                if i.Chart2:
                    self.data_line_2.setData(self.t, i.Data)# Update the data.
                
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
