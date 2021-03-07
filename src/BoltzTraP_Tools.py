#!/usr/bin/env python
#-*- coding : utf-8 -*-
"""
BoltzTraP_Tools is an interface written using Python 2 language.
It allows to parse and plot BoltzTraP output DATA:
       - **.trace**
       - **.condtens**
       - **.trace_fixdoping**
       - **.condtens_fixdoping**

BoltzTraP_Tools can read all ***TRACE*** and ***CONDTENS*** output files.
Therefore, it will be possible to plot the following quantities :
       - Energy level
       - Temperature
       - Seebeck Coiffecients
       - Electrical Conductivity
       - Power Factor
       - Thermal Conductivity
       - Number of Carriers
       - Hall Coefficient
       - Electronic Specific Heat
       - Pauli Magnetic
"""

__author__ = 'Hilal BALOUT'
__credits__ = "Hilal BALOUT"
__maintainer__ = "Hilal BALOUT"
__author_email__ = 'hilal_balout@hotmail.com'
__url__ = 'https://github.com/K4ys4r/BoltzTraP_Tools'
__version__ = '1.0_beta'
__copyright__ = "Copyright 2018, Hilal BALOUT, BoltzTraP_Tools Project"
__license__ = "MIT"

import pylab as p
try:
    input = raw_input
except NameError:
    pass
    
def Labels_Init():
    Plot_Label={  "E"             :    [0,
                                        " $\epsilon-\epsilon_{Fermi}$ ",
                                        " Energy; ",
                                        "input('Energy unit ? > ')",
                                        "input('Energy Scale Factor ? > ')"],

                  "T"             :    [1,
                                        " Temperature ",
                                        " T; ",
                                        " ($K$) ",
                                        1.0],

                  "N"             :    [2,
                                        " Doping Level ",
                                        " N; ",
                                        "input('Carriers unit ? > ')",
                                        "input('Carriers Scale Factor ? > ')"],

                  "DOS"           :    [3,
                                        " n($\mu$) ",
                                        " n($\mu$) ",
                                        "input('DOS unit ? > ')",
                                        "input('DOS Scale Factor ? > ')"],

                  "S"             :    [4,
                                        " Seebeck ",
                                        " $S$; ",
                                        "input('S unit ? > ')",
                                        "input('S Scale Factor ? > ')"],

                  "Sxx"           :    [8,
                                        " Seebeck ",
                                        " $S_{xx}$; "],
                  "Syy"           :    [9,
                                        " Seebeck ",
                                        " $S_{yy}$; "],
                  "Szz"           :    [10,
                                        " Seebeck ",
                                        " $S_{zz}$; "],

                  "Sigma"         :    [5,
                                        " $\sigma / \\tau$ ",
                                        " $\sigma $; ",
                                        "input('Sigma unit ? > ')",
                                        "input('Sigma Scale Factor ? > ')"],

                  "Sigmaxx"       :    [11,
                                        " $\sigma / \\tau$ ",
                                        " $\sigma_{xx} $ ; " ],
                  "Sigmayy"       :    [12,
                                        " $\sigma / \\tau$ ",
                                        " $\sigma_{yy} $ ; " ],
                  "Sigmazz"       :    [13,
                                        " $\sigma / \\tau$ ",
                                        " $\sigma_{zz} $ ; "],

                  "PF"            :    [17,
                                        " $S^2 \sigma / \\tau$ ",
                                        " $PF$ ; ",
                                        "input('PF unit ? > ')",
                                        "input('PF Scale Factor ? > ')"],
                  "PFxx"          :    [18,
                                        " $S^2 \sigma / \\tau$ ",
                                        " $PF_{xx}$ ; "],
                  "PFyy"          :    [19,
                                        " $S^2 \sigma / \\tau$ ",
                                        " $PF_{yy}$ ; "],
                  "PFzz"          :    [20,
                                        " $S^2 \sigma / \\tau$ ",
                                        " $PF_{zz}$ ; "],

                  "Kappa"         :    [7,
                                        " $\kappa$ ",
                                        " $\kappa$; ",
                                        "input('Kappa unit ? > ')",
                                        "input('Kappa Scale Factor ? > ')"],
                  "Kappaxx"       :    [14,
                                        " $\kappa$ ",
                                        " $\kappa_{xx}$; "],
                  "Kappayy"       :    [15,
                                        " $\kappa$ ",
                                        " $\kappa_{yy}$; "],
                  "Kappazz"       :    [16,
                                        " $\kappa$ ",
                                        " $\kappa_{zz}$; "],

                  "R_H"           :    [6,
                                        " $R_H$ ",
                                        " $R_H$; ",
                                        "input('Hall coefficient (R_H) unit ? > ')",
                                        "input('Hall coefficient (R_H) Scale Factor ? > ')"],

                  "c"             :    [8,
                                        " $c$ ",
                                        " $c$; ",
                                        "input('Electronic Specific Heat (c) unit ? > ')",
                                        "input('Electronic Specific Heat (c) Scale Factor ? > ')"],

                  "chi"           :    [9,
                                        " $\chi$ ",
                                        " $\chi$; ",
                                        "input('Pauli magnetic (chi) unit ? > ')",
                                        "input('Pauli magnetic (chi) Scale Factor ? > ')"],

                   }
    return Plot_Label

def Scaling_DATA(Plot_Label):
    conv=input("Setting of Units and Scale Factors (y/n) ? > ")
    if conv=="y":
       for i in ["S","Sigma","PF","Kappa","E","N","c","chi","DOS","R_H"]:
           Plot_Label[i][4]=float(eval(Plot_Label[i][4]))
           Plot_Label[i][3]=eval(Plot_Label[i][3])
       for i in ["Sxx","Syy","Szz"]:
           Plot_Label[i].append(Plot_Label["S"][3])
           Plot_Label[i].append(Plot_Label["S"][4])
       for i in ["Sigmaxx","Sigmayy","Sigmazz"]:
           Plot_Label[i].append(Plot_Label["Sigma"][3])
           Plot_Label[i].append(Plot_Label["Sigma"][4])
       for i in ["PFxx","PFyy","PFzz"]:
           Plot_Label[i].append(Plot_Label["PF"][3])
           Plot_Label[i].append(Plot_Label["PF"][4])
       for i in ["Kappaxx","Kappayy","Kappazz"]:
           Plot_Label[i].append(Plot_Label["Kappa"][3])
           Plot_Label[i].append(Plot_Label["Kappa"][4])
    elif conv=="n":
        units={"S"     : " ($V/K$) ",
               "Sigma" : " ($1/(\Omega . cm . s)$) ",
               "PF"    : " ($W/(K^2 . cm . s)$ ",
               "Kappa" : " ($W/(m. K . s)$) ",
               "E"     : " ($Ry$) ",
               "N"     : " ($e/uc$) ",
               "chi"   : " ($m^3/mol$) ",
               "c"     : " ($J/(mol . K)$) ",
               "DOS"   : " ($e/uc$) ",
               "R_H"   : " ($m^3/C$) "
               }
        for i in ["S","Sigma","PF","Kappa","E","N","c","chi","DOS","R_H"]:
            Plot_Label[i][4]=1.0
            Plot_Label[i][3]=units[i]
        for i in ["Sxx","Syy","Szz"]:
            Plot_Label[i].append(Plot_Label["S"][3])
            Plot_Label[i].append(Plot_Label["S"][4])
        for i in ["Sigmaxx","Sigmayy","Sigmazz"]:
            Plot_Label[i].append(Plot_Label["Sigma"][3])
            Plot_Label[i].append(Plot_Label["Sigma"][4])
        for i in ["PFxx","PFyy","PFzz"]:
            Plot_Label[i].append(Plot_Label["PF"][3])
            Plot_Label[i].append(Plot_Label["PF"][4])
        for i in ["Kappaxx","Kappayy","Kappazz"]:
            Plot_Label[i].append(Plot_Label["Kappa"][3])
            Plot_Label[i].append(Plot_Label["Kappa"][4])

def File_Read(Type):
    cmd=Type+" File name ? > "
    inp=input("%50s"%cmd)
    ef=float(input("%50s"%"Fermi Level Value in Ry ? > "))
    d=p.loadtxt(inp)
    return d,ef

def Write2File(InfosData2Save,Data2Save,inpf):
    f=open(inpf,"w")
    f.write("# This file has been generated by BoltzTraP_Tools scripts\n")
    [f.write("%s   "%info.replace(" ","")) for info in InfosData2Save]
    f.write("\n")
    for i in range(Data2Save.shape[2]):
        for j in xrange(Data2Save.shape[0]):
            if j==0:
                f.write("%16.8e %16.8e "%(Data2Save[j,0,i],Data2Save[j,1,i]))
            else:
                f.write("%16.8e "%Data2Save[j,1,i])
        f.write("\n")        
    f.close()
    print("\nData has been saved to "+inpf+" file\n")
            

def PLOT_DATA(arr,Xplot,Yplot,lb,Ef,Log,Plot_Label,Data2Save):
    p.xlabel(Plot_Label[Xplot][1]+Plot_Label[Xplot][3])
    p.ylabel(Plot_Label[Yplot][1]+Plot_Label[Yplot][3])
    p.title(Plot_Label[Yplot][1]+" as a function of "+Plot_Label[Xplot][1])
    if Xplot=="E":
       x=(arr[:,Plot_Label[Xplot][0]]-Ef)*float(Plot_Label[Xplot][4])
    else:
       x=arr[:,Plot_Label[Xplot][0]]*float(Plot_Label[Xplot][4])
    if Yplot=="E":
       y=(arr[:,Plot_Label[Yplot][0]]-Ef)*float(Plot_Label[Yplot][4])
    else:
       y=arr[:,Plot_Label[Yplot][0]]*float(Plot_Label[Yplot][4])
    if Xplot=="N" and Log=="y":
       indn=p.where(x<0)
       indp=p.where(x>0)
       pp=input("Plot electron or hole ? > ")
       if pp=="electron":
          p.semilogx(abs(x[indn]),y[indn],label=lb+"$ ; n-Type$")
       elif pp=="hole":
          p.semilogx(x[indp],y[indp],label=lb+"$ ; p-Type $")
    elif Yplot=="N" and Log=="y":
       indn=p.where(y<0)
       indp=p.where(y>0)
       pp=input("Plot electron or hole ?? > ")
       if pp=="electron":
          p.semilogy(x[indn],abs(y[indn]),label=lb+"$ ; n-Type$")
       elif pp=="hole":
          p.semilogy(x[indp],y[indp],label=lb+"$ ; p-Type$")
    else:
       p.plot(x,y,label=lb)

    if len(Data2Save) == 0 and len(x) != 0:
       Data2Save = p.array([[x,y]])
    elif len(Data2Save) != 0:
       Data2Save = p.append(Data2Save,[[x,y]],axis=0)      
    return Data2Save

def Get_DATA(File_DATA,Type,f):
    if f!="N":
       Tmin,Tmax,dT=File_DATA[0,1],File_DATA[-1,1],File_DATA[1,1]-File_DATA[0,1]
       Emin,Emax,dE=File_DATA[0,0],File_DATA[-1,0],File_DATA[int((Tmin+Tmax)/dT),0]-File_DATA[0,0]
       p_label={"E" : [0,"Give a Energy Value : "," Ry",Emin,Emax,dE],
                "T" : [1,"Give a Temperature Value : "," K",Tmin,Tmax,dT]}
       Val=eval(input("\n%s\n   MIN=%f ; MAX=%f ; Delta=%f (unit: %s)  > "\
                %(p_label[f][1],p_label[f][3],p_label[f][4],p_label[f][5],p_label[f][2])))
       print(Val)
       if Type=="Trace":
          d=File_DATA[p.where(File_DATA[:,p_label[f][0]]==Val)]
          DATA=p.zeros((len(d),18))
          DATA[:,:10]=d[:,:10]
          DATA[:,17]=DATA[:,4]*DATA[:,4]*DATA[:,5]
       elif Type=="Condtens":
          d=File_DATA[p.where(File_DATA[:,p_label[f][0]]==Val)]
          DATA=p.zeros((len(d),21))
          DATA[:,:3]=d[:,:3]
          DATA[:,4]=(d[:,12]+d[:,16]+d[:,20])/3.
          DATA[:,5]=(d[:,3]+d[:,7]+d[:,11])/3.
          DATA[:,7]=(d[:,21]+d[:,25]+d[:,29])/3.
          DATA[:,8],DATA[:,9],DATA[:,10]=d[:,12],d[:,16],d[:,20]
          DATA[:,11],DATA[:,12],DATA[:,13]=d[:,3],d[:,7],d[:,11]
          DATA[:,14],DATA[:,15],DATA[:,16]=d[:,21],d[:,25],d[:,29]
          DATA[:,17]=DATA[:,4]*DATA[:,4]*DATA[:,5]
          DATA[:,18]=DATA[:,8]*DATA[:,8]*DATA[:,11]
          DATA[:,19]=DATA[:,9]*DATA[:,9]*DATA[:,12]
          DATA[:,20]=DATA[:,10]*DATA[:,10]*DATA[:,13]
       Val=str(Val)+p_label[f][2]
    elif f=="N":
       Doping=p.unique(File_DATA[:,1])
       print("Doping Carrier Concentrations (/uc) : ",Doping)
       Val=float(input("Give a Doping Value from above > "))
       print(Val)
       if Type=="N-Trace":
          d=File_DATA[p.where(File_DATA[:,1]==Val)]
          DATA=p.zeros((len(d),18))
          DATA[:,0]=d[:,-1]
          DATA[:,1:10]=d[:,0:9]
          DATA[:,17]=DATA[:,4]*DATA[:,4]*DATA[:,5]
       elif Type=="N-Condtens":
            d=File_DATA[p.where(File_DATA[:,1]==Val)]
            DATA=p.zeros((len(d),21))
            DATA[:,:3]=d[:,[-1,0,1]]
            DATA[:,4]=(d[:,11]+d[:,15]+d[:,19])/3.
            DATA[:,5]=(d[:,2]+d[:,6]+d[:,10])/3.
            DATA[:,7]=(d[:,20]+d[:,24]+d[:,28])/3.
            DATA[:,8],DATA[:,9],DATA[:,10]=d[:,11],d[:,15],d[:,19]
            DATA[:,11],DATA[:,12],DATA[:,13]=d[:,2],d[:,6],d[:,10]
            DATA[:,14],DATA[:,15],DATA[:,16]=d[:,20],d[:,24],d[:,28]
            DATA[:,17]=DATA[:,4]*DATA[:,4]*DATA[:,5]
            DATA[:,18]=DATA[:,8]*DATA[:,8]*DATA[:,11]
            DATA[:,19]=DATA[:,9]*DATA[:,9]*DATA[:,12]
            DATA[:,20]=DATA[:,10]*DATA[:,10]*DATA[:,13]
       cm3=float(input("Give the Cell Volume in cm^3 to convert N ; else give 1.0) > "))
       if Val<0:
          if cm3==1: Val="$n =$ "+str("%.3e"%abs(Val))+" $e/uc$"
          elif cm3>0: Val="$n =$ "+str("%.3e"%float(abs(Val)/cm3))+" $e/cm^3$"
       elif Val>0:
          if cm3==1: Val="$h =$ "+str("%.3e"%abs(Val))+" $h/uc$"
          elif cm3>0: Val="$h =$ "+str("%.3e"%float(abs(Val)/cm3))+" $h/cm^3$"
    return DATA,Val



def DATA_Process(Analyse,File_DATA,Ef,Plot_Label):
    Data2Save = p.array([])
    InfosData2Save = []
    RESTART=True
    PLOT=True
    print("="*80)
    while RESTART:
        p.rcParams["font.family"] = "serif"
        p.figure(figsize=(10,6))
        p.rcParams.update({"font.size": 14})
        if Analyse=="Trace" or Analyse=="Condtens":
           f=input("Parse at fixed Temperature or Energy ? (T/E) > ")
           Log=input("Log Scale for Carrier Concentration ? (y/n) > ")
        elif Analyse=="N-Trace" or Analyse=="N-Condtens":
             f="N"
             Log=None
        if Analyse=="Trace" or Analyse=="N-Trace":
           Xplot=input("Xplot (E, T, N, DOS, S, Sigma, PF, R_H, Kappa, C or Chi ) ? > ")
           Yplot=input("Yplot (E, T, N, DOS, S, Sigma, PF, R_H, Kappa, C or Chi ) ? > ")
        elif Analyse=="Condtens" or Analyse=="N-Condtens":
           Xplot=input("Xplot (E, T, N, S, Sxx, Syy, Szz, Sigma, Sigmaxx, Sigmayy,Sigmazz, PF, PFxx, PFyy, PFzz, Kappa, Kappaxx, Kappayy or Kappazz) ? > ")
        while PLOT:
              DATA,Val=Get_DATA(File_DATA,Analyse,f)
              if Analyse=="Condtens" or Analyse=="N-Condtens":
                 Yplot=input("Yplot (E, T, N, S, Sxx, Syy, Szz, Sigma, Sigmaxx, Sigmayy,Sigmazz, PF, PFxx, PFyy, PFzz, Kappa, Kappaxx, Kappayy or Kappazz) ? > ")
              if (Xplot in Plot_Label) and (Yplot in Plot_Label):
                 Data2Save=PLOT_DATA(DATA,Xplot,Yplot,Plot_Label[Yplot][2]+str(Val),Ef,Log,Plot_Label,Data2Save)
                 InfosData2Save.append(Plot_Label[Yplot][2]+str(Val))
              else:
                 print("\n    Error in Xplot or Yplot Label!!..\n")
                 PLOT=False
                 break
              Todo=input("Plot Other Quantities ? (yes/no)? > ")
              if Todo=="yes":
                 PLOT=True
                 continue
              else:
                 PLOT=False
                 p.legend(loc="best")
                 p.show()
        ToSave = input("To Save Data to a file write 'save' >  ")
        if ToSave == "save":
          InfosData2Save.insert(0,"# "+Xplot)  
          inpf = input("Give a file name > ").replace(" ","")
          if inpf == "" : inpf = "SaveData.data"
          Write2File(InfosData2Save,Data2Save,inpf)
         
        Todo2=input("To restart write 'restart' , else no >  ")
        if Todo2=="restart":
           p.close()
           Data2Save = p.array([])
           PLOT=True
        else:
           RESTART=False
           print("\n    Exit!..\n")
    print("="*80)
