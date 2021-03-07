#!/usr/bin/python
from BoltzTraP_Tools import *

try:
    input = raw_input
except NameError:
    pass

labels=Labels_Init()
Scaling_DATA(labels)
labels["S"][4]=1e6
labels["S"][3]=' ($\mu V/K$) '
Analyse=input("File Extension (Trace, Condtens, N-Trace, or  N-Condtens) ? > ")
File_DATA,Ef=File_Read(Analyse)
DATA_Process(Analyse,File_DATA,Ef,labels)
