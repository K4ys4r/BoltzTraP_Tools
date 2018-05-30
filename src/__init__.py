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

More infos :
       User Guide :  https://github.com/K4ys4r/BoltzTraP_Tools/doc/UserGuide.pdf
       Tutorials  :  https://github.com/K4ys4r/BoltzTraP_Tools/doc/Tutorials.pdf
"""

__author__ = 'Hilal BALOUT'
__credits__ = "Hilal BALOUT"
__maintainer__ = "Hilal BALOUT"
__author_email__ = 'hilal_balout@hotmail.com'
__url__ = 'https://github.com/K4ys4r/BoltzTraP_Tools'
__version__ = '1.0_beta'
__copyright__ = "Copyright 2018, Hilal BALOUT, BoltzTraP_Tools Project"
__license__ = "MIT"

from .BoltzTraP_Tools import *
