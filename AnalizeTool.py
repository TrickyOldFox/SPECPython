# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:16:52 2020

@author: karan
"""

import csv
import numpy as np
from datetime import datetime
from random import randint


def csv_open(Path):
    s = tuple(['seconds','values','chanel'])
    seconds = []
    values = []
    with open(Path) as csvFile:
        reader = csv.DictReader(csvFile, fieldnames = s, delimiter = ';',  dialect='excel')
        for row in reader:
            if (row['values'] != None) and (row['seconds'] != None) and (row['chanel'] != None):
                DP = -1
                for i in range(len(row['seconds'])):
                    if row['seconds'][i]=='/':
                        DP = i
                timestring = row['seconds'][DP+1:len(row['seconds'])]
                try:
                    pt = datetime.strptime(timestring,'%H:%M:%S,%f')
                    total_seconds = pt.second + pt.minute*60 + pt.hour*3600 + pt.microsecond/1000000
                except:
                    total_seconds = float(timestring)
                seconds.append(total_seconds)
                valuesstring = row['values']
                for i in range(len(valuesstring)):
                    if valuesstring[i] == ',':
                        valuesstring = valuesstring[0:i]+'.'+valuesstring[i+1:len(valuesstring)]
                values.append(float(valuesstring))
    PlotData = [seconds, values]
    return (reader,PlotData)

def csv_save(Path, FileChannel):
    s = tuple(['seconds','values','chanel'])
    with open(Path, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, s, delimiter = ';')
        for i in range(len(FileChannel[0])):
            writer.writerow({s[0]:str(FileChannel[0][i]),s[1]:str(FileChannel[1][i]),s[2]:'DCV'})


def AnalizeFon(FileChannel, AVG, Precision, FilterRangeMultiplier, Filter):
        A=[]
        Deriviative = []
        AverageDeriviativeAbs = []
        AverageDeriviative = []
        AverageFon = []
        AverageFluctuation = 0
        for i in range(AVG//2):
            AverageFon.append(np.average(FileChannel[1][i:i+AVG]))
        for i in range(len(FileChannel[0])-1):
            Deriviative.append(FileChannel[1][i+1] - FileChannel[1][i])
        
        for i in range(len(Deriviative)-AVG):
            AverageDeriviative.append(np.abs(np.average(Deriviative[i:i+AVG])))
            AverageDeriviativeAbs.append(np.average(np.abs(Deriviative[i:i+AVG])))
        try:
            for i in range(len(FileChannel[0])-1-AVG):
                if AverageDeriviative[i] < Precision*AverageDeriviativeAbs[i]:
                    if i < AVG*FilterRangeMultiplier:
                        if FileChannel[1][i] < Filter*np.average(FileChannel[1][i:i+AVG*FilterRangeMultiplier]):
                            AverageFon.append(np.average(FileChannel[1][i:i+AVG]))
                            A.append((np.max(FileChannel[1][i:i+AVG])-np.min(FileChannel[1][i:i+AVG]))/2)
                            print(AverageFon[-1],A[-1])
                        else: AverageFon.append(0)
                    else: 
                        if i > len(FileChannel[0])-AVG*FilterRangeMultiplier:
                            if FileChannel[1][i] < Filter*np.average(FileChannel[1][i-AVG*FilterRangeMultiplier:i]):
                                AverageFon.append(np.average(FileChannel[1][i:i+AVG]))
                                A.append((np.max(FileChannel[1][i:i+AVG])-np.min(FileChannel[1][i:i+AVG]))/2)
                                print(AverageFon[-1],A[-1])
                            else: AverageFon.append(0)
                        else:
                            if FileChannel[1][i] < Filter*np.average(FileChannel[1][i-AVG*FilterRangeMultiplier//2:i+AVG*FilterRangeMultiplier//2]):
                                AverageFon.append(np.average(FileChannel[1][i:i+AVG]))
                                A.append((np.max(FileChannel[1][i:i+AVG])-np.min(FileChannel[1][i:i+AVG]))/2)
                                print(AverageFon[-1],A[-1])
                            else: AverageFon.append(0)
                else:
                    AverageFon.append(0)
        except ValueError:
            pass
        for i in range(AVG//2+1):
            AverageFon.append(np.average(FileChannel[1][len(FileChannel[0])-i-AVG : len(FileChannel[0])-i]))      
        AverageFon[0] = FileChannel[1][AVG]
        AverageFon[-1] = FileChannel[1][-1]
        print(AverageFon,AverageFluctuation)
        if A!= []: AverageFluctuation = np.average(A)
        else: AverageFluctuation = np.average(AverageFon)
        for i in range(len(AverageFon)):
            if AverageFon[i]==0:
                k=i
                while(AverageFon[k]==0): 
                    k+=1              
                AverageFon[i] = AverageFon[i-1] + (AverageFon[k] - AverageFon[i-1])/(k-i)
        print("Fon Analyzing is complete") 
        
        return AverageDeriviative, AverageFon, AverageFluctuation, FileChannel
    
def SearchLinesInSpectre(FileChannel, AVG, Precision, FilterRangeMultiplier, Filter, LinesSearchRange, LinesToSearch): 
        PossibleLines = []
        AverageDeriviative, AverageFon, AverageFluctuation, FileChannel = \
            AnalizeFon(FileChannel, AVG, Precision, FilterRangeMultiplier, Filter)
        for j in LinesToSearch:
            A=0
            B=0
            C=0
            for i in range(len(FileChannel[0])):
                r=FileChannel[0][i]
                if r > (j-LinesSearchRange/2) and r < (j+LinesSearchRange/2):
                    if FileChannel[1][i] > (AverageFon[i]+AverageFluctuation):
                        if FileChannel[1][i] > B:    
                            A = FileChannel[0][i]
                            B = FileChannel[1][i]
                            C = AverageFon[i]
            if A!=0 and B!=0 : PossibleLines.append((A,B,C))
        print("Lines searching is complete")
        print(PossibleLines, len(PossibleLines))
        
        return AverageDeriviative, AverageFon, AverageFluctuation, FileChannel, PossibleLines

def DeleteLinesFromSpectre(PossibleLines, FileChannel, LinesDeleteRange, PointImpact, AverageFluctuation):
        for i in PossibleLines:
            for j in range(len(FileChannel[0])):
                if (FileChannel[0][j]>i[0]-LinesDeleteRange/2) and (FileChannel[0][j]<i[0]):
                    if j%6 > 3:
                        FileChannel[1][j] = (PointImpact*FileChannel[1][j-1] + i[2])/(PointImpact+1) + randint(0,5)*(-AverageFluctuation)/4
                    else:
                        FileChannel[1][j] = (PointImpact*FileChannel[1][j-1] + i[2])/(PointImpact+1) + randint(0,5)*(AverageFluctuation)/4
            for j in range(len(FileChannel[0])):
                if (FileChannel[0][len(FileChannel[0])-j-1]<i[0]+LinesDeleteRange/2) and (FileChannel[0][len(FileChannel[0])-j-1]>=i[0]):
                    if (len(FileChannel[0])-j-1)%6 > 3:
                        FileChannel[1][len(FileChannel[0])-j-1] = (PointImpact*FileChannel[1][len(FileChannel[0])-j] + i[2])/(PointImpact+1) + randint(0,5)*(-AverageFluctuation)/4
                    else:
                        FileChannel[1][len(FileChannel[0])-j-1] = (PointImpact*FileChannel[1][len(FileChannel[0])-j] + i[2])/(PointImpact+1) + randint(0,5)*(AverageFluctuation)/4                 
        print('Delete Lines From Spectre is complete')
        
        return FileChannel