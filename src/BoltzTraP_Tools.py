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

def Labels_Init():
    Plot_Label={  "E"             :    [0,
                                        " $\epsilon-\epsilon_{Fermi}$ ",
                                        " Energy; ",
                                        "raw_input('Energy unit ? > ')",
                                        "raw_input('Energy Scale Factor ? > ')"],

                  "T"             :    [1,
                                        " Temperature ",
                                        " T; ",
                                        " ($K$) ",
                                        1.0],

                  "N"             :    [2,
                                        " Doping Level ",
                                        " N; ",
                                        "raw_input('Carriers unit ? > ')",
                                        "raw_input('Carriers Scale Factor ? > ')"],

                  "DOS"           :    [3,
                                        " n($\mu$) ",
                                        " n($\mu$) ",
                                        "raw_input('DOS unit ? > ')",
                                        "raw_input('DOS Scale Factor ? > ')"],

                  "S"             :    [4,
                                        " Seebeck ",
                                        " $S$; ",
                                        "raw_input('S unit ? > ')",
                                        "raw_input('S Scale Factor ? > ')"],

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
                                        "raw_input('Sigma unit ? > ')",
                                        "raw_input('Sigma Scale Factor ? > ')"],

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
                                        "raw_input('PF unit ? > ')",
                                        "raw_input('PF Scale Factor ? > ')"],
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
                                        "raw_input('Kappa unit ? > ')",
                                        "raw_input('Kappa Scale Factor ? > ')"],
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
                                        "raw_input('Hall coefficient (R_H) unit ? > ')",
                                        "raw_input('Hall coefficient (R_H) Scale Factor ? > ')"],

                  "c"             :    [8,
                                        " $c$ ",
                                        " $c$; ",
                                        "raw_input('Electronic Specific Heat (c) unit ? > ')",
                                        "raw_input('Electronic Specific Heat (c) Scale Factor ? > ')"],

                  "chi"           :    [9,
                                        " $\chi$ ",
                                        " $\chi$; ",
                                        "raw_input('Pauli magnetic (chi) unit ? > ')",
                                        "raw_input('Pauli magnetic (chi) Scale Factor ? > ')"],

                   }
    return Plot_Label

def Scaling_DATA(Plot_Label):
    conv=raw_input("Setting of Units and Scale Factors (y/n) ? > ")
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
    inp=raw_input("%50s"%cmd)
    ef=float(raw_input("%50s"%"Fermi Level Value in Ry ? > "))
    d=p.loadtxt(inp)
    return d,ef

def PLOT_DATA(arr,Xplot,Yplot,lb,Ef,Log,Plot_Label):
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
       pp=raw_input("Plot electron or hole ? > ")
       if pp=="electron":
          p.semilogx(abs(x[indn]),y[indn],label=lb+"$ ; n-Type$")
       elif pp=="hole":
          p.semilogx(x[indp],y[indp],label=lb+"$ ; p-Type $")
    elif Yplot=="N" and Log=="y":
       indn=p.where(y<0)
       indp=p.where(y>0)
       pp=raw_input("Plot electron or hole ?? > ")
       if pp=="electron":
          p.semilogy(x[indn],abs(y[indn]),label=lb+"$ ; n-Type$")
       elif pp=="hole":
          p.semilogy(x[indp],y[indp],label=lb+"$ ; p-Type$")
    else:
       p.plot(x,y,label=lb)

def Get_DATA(File_DATA,Type,f):
    if f!="N":
       Tmin,Tmax,dT=File_DATA[0,1],File_DATA[-1,1],File_DATA[1,1]-File_DATA[0,1]
       Emin,Emax,dE=File_DATA[0,0],File_DATA[-1,0],File_DATA[int((Tmin+Tmax)/dT),0]-File_DATA[0,0]
       p_label={"E" : [0,"Give a Energy Value : "," Ry",Emin,Emax,dE],
                "T" : [1,"Give a Temperature Value : "," K",Tmin,Tmax,dT]}
       Val=eval(raw_input("\n%s\n   MIN=%f ; MAX=%f ; Delta=%f (unit: %s)  > "\
                %(p_label[f][1],p_label[f][3],p_label[f][4],p_label[f][5],p_label[f][2])))
       print Val
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
       print "Doping Carrier Concentrations (/uc) : ",Doping
       Val=float(raw_input("Give a Doping Value from above > "))
       print Val
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
       cm3=float(raw_input("Give the Cell Volume in cm^3 to convert N ; else give 1.0) > "))
       if Val<0:
          if cm3==1: Val="$n =$ "+str("%.3e"%abs(Val))+" $e/uc$"
          elif cm3>0: Val="$n =$ "+str("%.3e"%float(abs(Val)/cm3))+" $e/cm^3$"
       elif Val>0:
          if cm3==1: Val="$h =$ "+str("%.3e"%abs(Val))+" $h/uc$"
          elif cm3>0: Val="$h =$ "+str("%.3e"%float(abs(Val)/cm3))+" $h/cm^3$"
    return DATA,Val



def DATA_Process(Analyse,File_DATA,Ef,Plot_Label):
    RESTART=True
    PLOT=True
    print "="*80
    while RESTART:
        p.rcParams["font.family"] = "serif"
        p.figure(figsize=(10,6))
        p.rcParams.update({"font.size": 14})
        if Analyse=="Trace" or Analyse=="Condtens":
           f=raw_input("Parse at fixed Temperature or Energy ? (T/E) > ")
           Log=raw_input("Log Scale for Carrier Concentration ? (y/n) > ")
        elif Analyse=="N-Trace" or Analyse=="N-Condtens":
             f="N"
             Log=None
        if Analyse=="Trace" or Analyse=="N-Trace":
           Xplot=raw_input("Xplot (E, T, N, DOS, S, Sigma, PF, R_H, Kappa, C or Chi ) ? > ")
           Yplot=raw_input("Yplot (E, T, N, DOS, S, Sigma, PF, R_H, Kappa, C or Chi ) ? > ")
        elif Analyse=="Condtens" or Analyse=="N-Condtens":
           Xplot=raw_input("Xplot (E, T, N, S, Sxx, Syy, Szz, Sigma, Sigmaxx, Sigmayy,Sigmazz, PF, PFxx, PFyy, PFzz, Kappa, Kappaxx, Kappayy or Kappazz) ? > ")
        while PLOT:
              DATA,Val=Get_DATA(File_DATA,Analyse,f)
              if Analyse=="Condtens" or Analyse=="N-Condtens":
                 Yplot=raw_input("Yplot (E, T, N, S, Sxx, Syy, Szz, Sigma, Sigmaxx, Sigmayy,Sigmazz, PF, PFxx, PFyy, PFzz, Kappa, Kappaxx, Kappayy or Kappazz) ? > ")
              if (Xplot in Plot_Label) and (Yplot in Plot_Label):
                 PLOT_DATA(DATA,Xplot,Yplot,Plot_Label[Yplot][2]+str(Val),Ef,Log,Plot_Label)
              else:
                 print "\n    Error in Xplot or Yplot Label!!..\n"
                 PLOT=False
                 break
              Todo=raw_input("Plot Other Quantities ? (yes/no)? > ")
              if Todo=="yes":
                 PLOT=True
                 continue
              else:
                 PLOT=False
                 p.legend(loc="best")
                 p.show()
        Todo2=raw_input("To restart write 'restart' , else no >  ")
        if Todo2=="restart":
           p.close()
           PLOT=True
        else:
           RESTART=False
           print "\n    Exit!..\n"
    print "="*80
