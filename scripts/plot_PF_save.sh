#!/bin/bash
<<:
This Script Excute the Script and outputs the plot of
Power Factor PF at 300,500 and 800 K as a function of Energy.
:

python Script_S_scaling.py <<EOF
n
Trace
../tests/CoSb3/CoSb3.trace
0.55475
T
n
E
PF
300
yes
500
yes
800
no
save
PF_300-500-800K.data
no
EOF
