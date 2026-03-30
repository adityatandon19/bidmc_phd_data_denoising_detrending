"""Least mean squares filter"""
import numpy as np

def lms_filter(signal, order = 4, mu = 0.05 ):
    weight = np.zeros(order) # initial weight, the system model
    length = len(signal) #find train signal length
    estimate = [] # LSM filter output
    er = [] # error list
    for i in range(length-order):
        x_signal = list(signal[i:i+order])# slice input signal
        x_signal.reverse() #transform sliced signal to timeline
        x_signal = np.transpose(x_signal) # x_signal transpose
        y_current = signal[i] #current signal point
        y_estimate = np.dot(weight, x_signal) #use LSM estamate current signal
        estimate.append(y_estimate) # filter output
        error = y_current - y_estimate
        er.append(error)
        weight = weight + mu * error * x_signal
    return estimate, weight,er


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb

data = pd.read_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/BIDMC dataset/bidmc-ppg-and-respiration-dataset-1.0.0/bidmc_csv/bidmc_01_Signals.csv', index_col=None)

# RESP Signal:
y_resp = data.drop(['Time [s]', ' PLETH', ' V', ' AVR', ' II'], axis = 1)
t = data['Time [s]']
y_resp = y_resp.values.flatten()
t = t.values.flatten()
pure = np.linspace(-1, 1, 60001)
noise = np.random.normal(0, 1, 60001)
noise.shape
y_resp = y_resp + noise
plt.plot(y_resp,'b', label= 'Signal with Noise')

np_resp,weight_resp,er_resp = lms_filter(y_resp,5,0.08)
# np,weight,er = nlms_filter.nlms_filter(y,5,1)
plt.plot(np_resp,'r', label= 'LMS_RESP')
plt.plot(er_resp,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()


# PLETH Signal:
y_pleth = data[' PLETH']
y_pleth = y_pleth.values.flatten()
y_pleth = y_pleth + noise
plt.plot(y_pleth,'b', label= 'Signal with Noise')

np_pleth,weight_pleth,er_pleth = lms_filter(y_pleth,5,0.08)
plt.plot(np_pleth,'r', label= 'LMS_PLETH')
plt.plot(er_pleth,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()


# V Signal:
y_v = data[' V']
y_v = y_v.values.flatten()
y_v = y_v + noise
plt.plot(y_v,'b', label= 'Signal with Noise')

np_v,weight_v,er_v = lms_filter(y_v,5,0.08)
plt.plot(np_v,'r', label= 'LMS_V')
plt.plot(er_v,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()

# AVR Signal:
y_avr = data[' AVR']
y_avr = y_avr.values.flatten()
y_avr = y_avr + noise
plt.plot(y_avr,'b', label= 'Signal with Noise')

np_avr,weight_avr,er_avr = lms_filter(y_avr,5,0.08)
plt.plot(np_avr,'r', label= 'LMS_AVR')
plt.plot(er_avr,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()

# II Signal:
y_ii = data[' II']
y_ii = y_ii.values.flatten()
y_ii = y_ii + noise
plt.xlim(0, 60000)
plt.plot(y_ii,'b', label= 'Signal with Noise')

np_ii,weight_ii,er_ii = lms_filter(y_ii,5,0.08)
plt.plot(np_ii,'r', label= 'LMS_II')
plt.plot(er_ii,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()

lms_fil = pd.DataFrame([np_resp, np_pleth, np_v, np_avr, np_ii])
lms_fil = lms_fil.T
lms_fil.rename(columns = {0:'RESP', 1:'PLETH', 2:'V', 3:'AVR', 4:'II'}, inplace=True)
lms_fil.to_csv('/home/soft23/soft23/soft23/python/Dataset-PPG/LMS_Filtered(01-11-22).csv')
