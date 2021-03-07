from BoltzTraP_Tools import *
try:
    input = raw_input
except NameError:
    pass

labels=Labels_Init()
Scaling_DATA(labels)
Analyse=input("File Extension (Trace, Condtens, N-Trace, or  N-Condtens) ? > ")
File_DATA,Ef=File_Read(Analyse)
DATA_Process(Analyse,File_DATA,Ef,labels)
