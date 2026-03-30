import os 
import numpy as np
import pandas as pd
from scipy import signal

from matplotlib import pyplot as plt

lms_fil = pd.read_csv ('/home/soft23/soft23/soft23/python/Dataset-PPG/LMS_Filtered(01-11-22).csv', index_col=0)
lms_resp = lms_fil['RESP']
lms_resp = lms_resp.values.flatten()

# Detrend:
# RESP Signal:
resp_detrend = signal.detrend(lms_resp)

plt.figure(figsize=(5, 4))
plt.xlim(0, 100)
plt.plot(lms_resp, label="RESP")
plt.plot(resp_detrend, label="RESP_Detrended")
plt.legend(loc='best')
plt.grid()
plt.show()

# PLETH Signal:
lms_pleth = lms_fil['PLETH']
lms_pleth = lms_pleth.values.flatten()
pleth_detrend = signal.detrend(lms_pleth)

plt.figure(figsize=(5, 4))
plt.plot(lms_resp, label="PLETH")
plt.plot(resp_detrend, label="PLETH_Detrended")
plt.legend(loc='best')
plt.grid()
plt.show()

# V Signal:
lms_v = lms_fil['V']
lms_v = lms_v.values.flatten()
v_detrend = signal.detrend(lms_v)

plt.figure(figsize=(5, 4))
plt.plot(lms_v, label="V")
plt.plot(v_detrend, label="V_Detrended")
plt.legend(loc='best')
plt.grid()
plt.show()

#AVR Signal:
lms_avr = lms_fil['AVR']
lms_avr = lms_avr.values.flatten()
avr_detrend = signal.detrend(lms_avr)

plt.figure(figsize=(5, 4))
plt.plot(lms_avr, label="AVR")
plt.plot(avr_detrend, label="AVR_Detrended")
plt.legend(loc='best')
plt.grid()
plt.show()

# II Signal:
lms_ii = lms_fil['II']
lms_ii = lms_ii.values.flatten()
ii_detrend = signal.detrend(lms_ii)

plt.figure(figsize=(5, 4))
plt.plot(lms_ii, label="II")
plt.plot(ii_detrend, label="II_Detrended")
plt.legend(loc='best')
plt.grid()
plt.show()


detrended = pd.DataFrame([resp_detrend, pleth_detrend, v_detrend, avr_detrend, ii_detrend])
detrended = detrended.T
detrended.rename(columns = {0:'RESP', 1:'PLETH', 2:'V', 3:'AVR', 4:'II'}, inplace=True)
detrended.to_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/Detrend_Signal(01-11-22).csv')
