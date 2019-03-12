
## What is BoltzTraP_Tools?

BoltzTraP_Tools is an interface written using Python 2 language.<br>
It allows to parse and plot and/or save BoltzTraP output DATA:
- **.trace**
- **.condtens**
- **.trace_fixdoping**
- **.condtens_fixdoping**

Numpy and Matplotlib (Pylab) Python packages are needed.<br>

BoltzTraP_Tools includes three folders:<br>
- **src**     : includes all python scripts.
- **doc**     : includes the user guide and some tutorials.
- **tests**   : includes the two BoltzTraP examples.
- **scripts** : includes some scripts using BoltzTraP_Tools.

## What BoltzTraP_Tools can do?
BoltzTraP_Tools can read all ***TRACE*** and ***CONDTENS*** output files.<br>
Therefore, it will be possible to plot the following quantities :<br>
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

More infos :<br>
- User Guide :  https://github.com/K4ys4r/BoltzTraP_Tools/blob/master/doc/UserGuide.pdf
- Tutorials  :  https://github.com/K4ys4r/BoltzTraP_Tools/blob/master/doc/Tutorials.pdf
- Update     :  plotted data can be saved to file. See example in : *scripts/plot_{S,Sigma,PF,}_save.sh*

