#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
  This script stores the temperature for the last N seonds to be ploted.
"""

import os
import numpy as np
from time import sleep,time
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.realpath(__file__))
ini = here + '/config.ini'

import common
N,t0,fname = common.read_params(ini)


X,T1,T2 = [],[],[]
told = time()
while not os.path.isfile(here+'/STOP'):
   N,t0,fname = common.read_params(ini)
   com = 'sensors | grep "Core"'
   temps = os.popen(com).read()
   t1,t2 = temps.splitlines()
   t1 = float(t1.split()[2][:-2])
   t2 = float(t2.split()[2][:-2])
   X.append(time())
   T1.append( t1 )
   T2.append( t2 )
   twrite = time()
   #f = open(HOME+'/.temp.dat','w')
   with open(fname,'w') as f:
      for x,t1,t2 in zip(X[-N:],T1[-N:],T2[-N:]):
         f.write(str(x)+'   '+str(t1)+'   '+str(t2)+'\n')
   twrite = time()-twrite
   sleep(max([t0-twrite,0]))
   if len(X) > 7*N: X,T1,T2 = X[-N:],T1[-N:],T2[-N:]
