#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from time import time
import os
here = os.path.dirname(os.path.realpath(__file__))
ini = here+'/config.ini'

import common
N,t0,fname = common.read_params(ini)


X,T1,T2 = np.loadtxt(fname, unpack=True)
X -= time()


N = 49
from scipy.signal import savgol_filter
x  = savgol_filter(X, N,3)   #[np.mean(x) for x in np.array_split(X,N)]
t1 = savgol_filter(T1,N,3)   #[np.mean(x) for x in np.array_split(T1,N)]
t2 = savgol_filter(T2,N,3)   #[np.mean(x) for x in np.array_split(T2,N)]

fig, ax = plt.subplots(figsize=(15,3))
l, = ax.plot(X,T1,lw=3,alpha=0.3)
ax.plot(x,t1,color=l.get_color(),lw=3)
l, = ax.plot(X,T2,lw=3,alpha=0.3)
ax.plot(x,t2,color=l.get_color(),lw=3)
ax.set_ylabel('T (°C)')
ax.set_xlabel('t (s)')
ax.set_xlim([min(X),max(X)])
#ax.set_ylim(ymin=min([60,min(T1),min(T2)]))
fig.tight_layout()
plt.show()
